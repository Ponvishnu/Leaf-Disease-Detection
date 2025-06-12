# 🌿 Leaf Disease Detection AI
An intelligent image classification system to detect diseases in plant leaves using a convolutional neural network (CNN). Built with TensorFlow, OpenCV, and scikit-learn, it includes a simple GUI for easy image upload and prediction.

## 🧠 Features
- 🌱 Detects whether a leaf is **Healthy** or **Diseased**
- 🖼️ Upload leaf images through GUI (Tkinter)
- 🤖 Trained using CNN and TensorFlow
- 💾 Uses pre-trained `.h5` model (no need to retrain every time)
- 🔬 Support for expanding to more disease classes

## 🚀 How to Run
1. Make sure the model file `leaf_model.h5` is present in the `model/` folder.
2. Run the GUI:
bash
python gui.py

## 🧪 Requirements
Python 3.10+
tensorflow
opencv-python
scikit-learn
numpy
tk

Install dependencies:
pip install -r requirements.txt
pip install tensorflow opencv-python scikit-learn numpy tk

## 📸 Sample Use
Launch the app.
Click "Upload Image".
View disease prediction instantly.

📜 This project is licensed under the MIT License.
