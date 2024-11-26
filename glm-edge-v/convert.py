import os
import argparse
from pathlib import Path
import nncf
from glmv_helper import convert_glmv_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h',
                        '--help',
                        action='help',
                        help='Show this help message and exit.')
    parser.add_argument('-m',
                        '--model_id',
                        default='THUDM/glm-4v-9b',
                        required=False,
                        type=str,
                        help='orignal model path')
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

    if args.modelscope:
        from modelscope import snapshot_download

        print("====Downloading model from ModelScope=====")
        model_path = snapshot_download(args.model_id, cache_dir='./')
    else:
        model_path = args.model_id

    compression_configuration = {
        "mode": nncf.CompressWeightsMode.INT4_SYM,
        "group_size": 64,
        "ratio": 0.6,
    }
    convert_glmv_model(model_path, ir_model_path, compression_configuration)
