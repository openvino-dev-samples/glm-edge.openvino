from transformers import AutoTokenizer
from optimum.intel import OVWeightQuantizationConfig
from optimum.intel.openvino import OVModelForCausalLM
from optimum.exporters.tasks import TasksManager


import os
from pathlib import Path
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h',
                        '--help',
                        action='help',
                        help='Show this help message and exit.')
    parser.add_argument('-m',
                        '--model_id',
                        default='THUDM/glm-edge-1.5b-chat',
                        required=False,
                        type=str,
                        help='orignal model path')
    parser.add_argument('-p',
                        '--precision',
                        required=False,
                        default="int4",
                        type=str,
                        choices=["fp16", "int8", "int4"],
                        help='fp16, int8 or int4')
    parser.add_argument('-o',
                        '--output',
                        required=False,
                        type=str,
                        help='path to save the ir model')
    parser.add_argument('-ms',
                        '--modelscope',
                        action='store_true',
                        help='download model from Model Scope')
    args = parser.parse_args()

    ir_model_path = Path(args.model_id.split(
        "/")[1] + '-ov') if args.output is None else Path(args.output)

    if not ir_model_path.exists():
        os.mkdir(ir_model_path)

    compression_configs = {
        "sym": True,
        "group_size": 128,
        "ratio": 0.8,
    }
    if args.modelscope:
        from modelscope import snapshot_download

        print("====Downloading model from ModelScope=====")
        model_path = snapshot_download(args.model_id, cache_dir='./')
    else:
        model_path = args.model_id

    TasksManager._SUPPORTED_MODEL_TYPE["glm"] = TasksManager._SUPPORTED_MODEL_TYPE["llama"]

    print("====Exporting IR=====")
    if args.precision == "int4":
        ov_model = OVModelForCausalLM.from_pretrained(model_path, export=True,
                                                      compile=False, quantization_config=OVWeightQuantizationConfig(
                                                          bits=4, **compression_configs), trust_remote_code=True)
    elif args.precision == "int8":
        ov_model = OVModelForCausalLM.from_pretrained(model_path, export=True,
                                                      compile=False, load_in_8bit=True, trust_remote_code=True)
    else:
        ov_model = OVModelForCausalLM.from_pretrained(model_path, export=True,
                                                      compile=False, load_in_8bit=False, trust_remote_code=True)

    print("====Saving IR=====")
    ov_model.save_pretrained(ir_model_path)

    print("====Exporting tokenizer=====")
    tokenizer = AutoTokenizer.from_pretrained(
        model_path, trust_remote_code=True)
    tokenizer.save_pretrained(ir_model_path)

    print("====Exporting IR tokenizer=====")
    from optimum.exporters.openvino.convert import export_tokenizer
    export_tokenizer(tokenizer, ir_model_path)
    print("====Finished=====")
