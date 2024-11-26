import argparse
from PIL import Image
from transformers import AutoTokenizer, AutoImageProcessor, TextStreamer
from glmv_helper import OvGLMv
import torch


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h',
                        '--help',
                        action='help',
                        help='Show this help message and exit.')
    parser.add_argument('-m',
                        '--model_path',
                        required=True,
                        type=str,
                        help='Required. model path')
    parser.add_argument('-q',
                    '--query',
                    required=True,
                    type=str,
                    help='Required. users query')
    parser.add_argument('-l',
                        '--max_sequence_length',
                        default=256,
                        required=False,
                        type=int,
                        help='maximun length of output')
    parser.add_argument('-i',
                        '--image_path',
                        required=True,
                        type=str,
                        help='Required. image path')
    parser.add_argument('-d',
                        '--device',
                        default='CPU',
                        required=False,
                        type=str,
                        help='device for inference')
    args = parser.parse_args()

    messages = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": args.query}]}]
    image = Image.open(args.image_path)
    
    processor = AutoImageProcessor.from_pretrained(args.model_path, trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
    model = OvGLMv(args.model_path, args.device)

    inputs = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, return_dict=True, tokenize=True, return_tensors="pt"
    ).to("cpu")

    generate_kwargs = {
        **inputs,
        "pixel_values": torch.tensor(processor(image).pixel_values).to("cpu"),
        "max_length": args.max_sequence_length, "do_sample": True, "top_k": 20, "streamer": TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
    }
    output = model.generate(**generate_kwargs)