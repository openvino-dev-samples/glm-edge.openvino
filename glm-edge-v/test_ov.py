import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoProcessor, AutoImageProcessor
import requests
from glmv_helper import OvGLMv


url = "/home/ethan/intel/GLM4/truck.jpg"
messages = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": "describe this image"}]}]
image = Image.open(url)

model_dir = "/home/ethan/intel/glm-edge.openvino/glm-v/glm-edge-v-5b-ov"

processor = AutoImageProcessor.from_pretrained(model_dir, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = OvGLMv(model_dir, "GPU")

inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_dict=True, tokenize=True, return_tensors="pt"
).to("cpu")

generate_kwargs = {
    **inputs,
    "pixel_values": torch.tensor(processor(image).pixel_values).to("cpu")
}
output = model.generate(**generate_kwargs, max_new_tokens=100)
print(tokenizer.decode(output[0][len(inputs["input_ids"][0]):], skip_special_tokens=True))