English | [简体中文](README_zh.md)

# glm.openvino Demo

Here is an example of how to deploy [glm-edge](https://github.com/THUDM/GLM-Edge) series models using OpenVINO

## Environment configuration

We recommend that you create a new virtual environment and then install the dependencies as follows. The 
recommended Python version is `3.10+`.

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

## Examples


| Tasks               | Go                       |
| ------------------- | ------------------------ |
| 🚀 Text generation   | [glm-edge-chat](./glm-egde-chat/README.md)   |
| 🚀 Vision Multimodal | [glm-edge-v](./glm-egde-v/README.md) |


## Common problem

1. Do I need to install the OpenVINO C++ inference engine?
   - Unnecessary

2. Do I have to use Intel hardware?
   - We only tried it on Intel devices, and we recommend using x86 architecture Intel devices, including but not
   limited to:
     - Intel CPU, including personal computer CPU and server CPU.
     - Intel's integrated GPU. For example: Arc™ Series and Iris® Series.
     - Intel's discrete graphics card. For example: ARC™ A770 graphics card.
  
3. Why OpenVINO cannot find GPU device in my system?
   - Ensure OpenCL diivess are installed correctly.
   - Ensure you enabled the right permissions for GPU device
   - More information can be found in [Install GPU drivers](https://github.com/openvinotoolkit/openvino_notebooks/wiki/Ubuntu#1-install-python-git-and-gpu-drivers-optional)

4. Whether support C++?
   - Please refer to this [example](https://github.com/openvinotoolkit/openvino.genai/tree/master/src)
