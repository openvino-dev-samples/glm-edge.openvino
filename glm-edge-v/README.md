English | [简体中文](README_zh.md)

# glm-edge vision mulimodal

Here is an example of how to deploy vision mulimodal model `glm-edge-v` using OpenVINO

## 1. Convert model

Since the Huggingface model needs to be converted to an OpenVINO IR model, you need to download the model and convert.

```
python3 convert.py --model_id ZhipuAI/glm-edge-v-5b --output {your_path}/glm-edge-v-5b-ov --modelscope
```

### Parameters that can be selected

* `--model_id` - path (absolute path) to be used from Huggngface_hub (https://huggingface.co/models) or the directory
  where the model is located.
* `--output` - the path where the converted model is saved
* `--modelscope` - if downloading the model from Model Scope.

## 2. Run the streaming Q&A

```
python3 qa.py --model_path {your_path}/glm-edge-v-5b-ov --query "Please describe this picture" --image_path {your_path}/your_test_image.jpg --max_sequence_length 4096 --device CPU
```


### Parameters that can be selected

* `--model_path` - The path to the directory where the OpenVINO IR model is located.
* `--query` - User's question.
* `--max_sequence_length` - Maximum size of output tokens.
* `--image_path` - The path to the input image.
* `--device` - The device to run inference on. e.g "CPU","GPU".

### Output example

```
The picture shows a white pickup truck. Specifically, the exterior color of this pickup truck is white with black tires. The design of the vehicle looks practical and suitable for carrying goods and tools. The windshield of the pickup truck is transparent, so you can clearly see into the vehicle. The window glass is blue and the door handles are black.
```