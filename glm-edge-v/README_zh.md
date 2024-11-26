简体中文 | [English](README.md)

# glm-edge视觉多模态示例

这是如何使用 OpenVINO 部署`glm-edge-v`视觉多模态的示例

## 1. 转换模型

由于需要将Huggingface模型转换为OpenVINO IR模型，因此您需要下载模型并转换。

```
python3 convert.py --model_id ZhipuAI/glm-edge-v-5b --output {your_path}/glm-edge-v-5b-ov --modelscope
```

### 可以选择的参数

* `--model_id` - 用于从 Huggngface_hub (https://huggingface.co/models) 或 模型所在目录的路径（绝对路径）。
* `--output` - 转换后模型保存的地址。
* `--modelscope` - 通过魔搭社区下载模型。


## 2. 运行流式问答

```
python3 qa.py --model_path {your_path}/glm-edge-v-5b-ov --query "请描述这张图片" --image_path {your_path}/your_test_image.jpg --max_sequence_length 4096 --device CPU
```

### 可以选择的参数

* `--model_path` - OpenVINO IR 模型所在目录的路径。
* `--query` - 用户问题。
* `--max_sequence_length` - 输出标记的最大大小。
* `--image` - 输入图片路径。
* `--device` - 运行推理的设备。例如："CPU","GPU"。

### 输出示例

```
图片中是一辆白色的皮卡车。具体地，这辆皮卡车的外观颜色为白色，带有黑色的轮胎。车的设计看起来实用，适合用于携带货物和工具。皮卡车的挡风玻璃是透明的，可以清晰地看到车内。车窗玻璃为蓝色，车门把手是黑色的。
```