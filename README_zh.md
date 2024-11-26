简体中文 | [English](README.md)

# glm.openvino Demo

这是如何使用 OpenVINO 部署 glm-edge系列模型示例

## 环境配置

我们推荐您新建一个虚拟环境，然后按照以下安装依赖。
推荐在python3.10以上的环境下运行该示例。

Linux

```
python3 -m venv openvino_env

source openvino_env/bin/activate

python3 -m pip install --upgrade pip

pip install wheel setuptools

pip install -r requirements.txt
```

Windows Powershell

```
python3 -m venv openvino_env

.\openvino_env\Scripts\activate

python3 -m pip install --upgrade pip

pip install wheel setuptools

pip install -r requirements.txt
```

## 模型示例

| 模型类别         | 地址                        |
| ---------------- | --------------------------- |
| 🚀 语言模型       | [glm-edge-chat](./glm-edge-chat/README_zh.md)   |
| 🚀 视觉多模态模型 | [glm-edge-v](./glm-edge-v/README_zh.md) |


## 常见问题

1. 需要安装 OpenVINO C++ 推理引擎吗
   - 不需要

2. 一定要使用 Intel 的硬件吗？
  - 我们仅在 Intel 设备上尝试，我们推荐使用x86架构的英特尔设备，包括但不限制于：
   - 英特尔的CPU，包括个人电脑CPU 和服务器CPU。
   - 英特尔的集成显卡。 例如：Arc™，Iris® 系列。
   - 英特尔的独立显卡。例如：ARC™ A770 显卡。
  
3. 为什么OpenVINO没检测到我系统上的GPU设备？
   - 确保OpenCL驱动是安装正确的。
   - 确保你有足够的权限访问GPU设备
   - 更多信息可以参考[Install GPU drivers](https://github.com/openvinotoolkit/openvino_notebooks/wiki/Ubuntu#1-install-python-git-and-gpu-drivers-optional)

4. 是否支持C++？
   - C++示例可以[参考](https://github.com/openvinotoolkit/openvino.genai/tree/master/src)
