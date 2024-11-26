English | [简体中文](README_zh.md)

# glm-edge text generation

Here is an example of how to deploy text-generation model `glm-edge-chat` using OpenVINO

## 1. Convert model

Since the Huggingface model needs to be converted to an OpenVINO IR model, you need to download the model and convert.

```
python3 convert.py --model_id ZhipuAI/glm-edge-1.5b-chat --precision int4 --output {your_path}/glm-edge-1.5b-chat-ov --modelscope
```

### Parameters that can be selected

* `--model_id` - path (absolute path) to be used from Huggngface_hub (https://huggingface.co/models) or the directory
  where the model is located.
* `--precision` - model precision: fp16, int8 or int4.
* `--output` - the path where the converted model is saved
* `--modelscope` - if downloading the model from Model Scope.

## 2. Run the streaming chatbot

```
python3 chat.py --model_path {your_path}/glm-edge-1.5b-chat-ov --max_sequence_length 4096 --device CPU
```

### Parameters that can be selected

* `--model_path` - The path to the directory where the OpenVINO IR model is located.
* `--max_sequence_length` - Maximum size of output tokens.
* `--device` - The device to run inference on. e.g "CPU","GPU".

### Output example

```
User: Hello
GLM-OpenVINO: Hello! Is there anything I can do to help you?

User: Who are you?
GLM-OpenVINO: I am an artificial intelligence assistant named ChatGLM3-6B, which was developed from a language model jointly trained by Tsinghua University’s KEG Laboratory and Zhipu AI Company in 2023. My role is to provide appropriate responses and support to users' questions and requests.

User: Please tell me an interesting story
ChatGLM3-6B-OpenVINO: Once upon a time, there was a little boy named Xiao Ming who loved animals very much. One day, while walking in the forest, he discovered a very beautiful bird. The bird was injured and could not fly. Xiao Ming felt very distressed and decided to take care of the little bird. Xiao Ming took the bird home, built a small nest for it, and found some soft grass and food. Every day, he feeds the bird and changes its water. Gradually, the bird's injury recovered and began to fly around Xiao Ming's home. They became very good friends. However, one day, Xiao Ming's parents told him that they must send Xiao Ming's little bird to the forest. Xiao Ming was very sad because he had become good friends with Xiaoniao. However, his parents told him that the bird would be more free in the forest and that he could continue to watch the bird's life in the forest. So, Xiao Ming and his parents sent the bird to the forest. The little bird is very happy because it can fly again and has many other little animal friends. Xiao Ming also felt very happy because he knew that even if he could not always have the birds, he could still appreciate their beauty in nature. From then on, Xiao Ming often came to the forest to look for birds.

User: Please give this story a title
GLM-OpenVINO: "The Power of Friendship: Xiao Ming and Bird's Forest Adventure"
```
