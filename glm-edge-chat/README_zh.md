简体中文 | [English](README.md)

# GLM文本生成模型

这是如何使用 OpenVINO 部署`glm-edge-chat`文本生成模型的示例

## 1. 转换模型

由于需要将Huggingface模型转换为OpenVINO IR模型，因此您需要下载模型并转换。

```
python3 convert.py --model_id ZhipuAI/glm-edge-1.5b-chat --precision int4 --output {your_path}/glm-edge-1.5b-chat-ov --modelscope
```

### 可以选择的参数

* `--model_id` - 用于从 Huggngface_hub (https://huggingface.co/models) 或 模型所在目录的路径（绝对路径）。
* `--precision` - 模型精度：fp16, int8 或 int4。
* `--output` - 转换后模型保存的地址。
* `--modelscope` - 通过魔搭社区下载模型。


## 2. 运行流式聊天机器人

```
python3 chat.py --model_path {your_path}/glm-edge-1.5b-chat-ov --max_sequence_length 4096 --device CPU
```

### 可以选择的参数

* `--model_path` - OpenVINO IR 模型所在目录的路径。
* `--max_sequence_length` - 输出标记的最大大小。
* `--device` - 运行推理的设备。例如："CPU","GPU"。

## 输出示例

```
用户: 你好
GLM-OpenVINO: 你好！有什么我可以帮助你的吗？

用户: 你是谁？     
GLM-OpenVINO: 我是一个名为ChatGLM3-6B的人工智能助手，是由清华大学KEG实验室和智谱AI 公司于2023 年共同训练的语言模型开发而成。我的任务是针对用户的问题和要求提供适当的答复和支持。

用户: 请给我讲一个有趣的故事
ChatGLM3-6B-OpenVINO: 从前，有一个名叫小明的小男孩，他是一个非常喜欢动物的人。有一天，他在森林里散步时，发现了一个非常漂亮的小鸟。小鸟受伤了，无法飞行。小明非常心疼，于是决定照顾这只小鸟。小明带着小鸟回家，为它搭建了一个小小的巢穴，并找来了一些软草和食物。每天，他都会给小鸟喂食，并为它换水。渐渐地，小鸟的伤势好了起来，开始在小明的家里飞来飞去，它们成了非常好的朋友。然而，一天，小明的父母告诉他，他们必须把小明养的小鸟送到森林里去。小明非常伤心，因为他已经和小鸟成为了好朋友。但是，他的父母告诉他，小鸟在森林里会更加自由自在，而且他也可以继续观看小鸟在森林中的生活。于是，小明和他的父母一起将小鸟送到了森林中。小鸟非常高兴，因为它又可以飞行了，并且还有许多其他的小动物朋友。小明也感到非常开心，因为他知道，即使不能一直拥有小鸟，他仍然可以欣赏到它们在自然中的美丽。从此以后，小明常常来到森林中，寻找小鸟。

用户: 请给这个故事起一个标题
GLM-OpenVINO: 《友谊的力量：小明与小鸟的森林冒险》
```
