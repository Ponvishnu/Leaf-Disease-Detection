import cv2
import numpy as np
from tensorflow.keras.models import load_model

label_map = {0: 'healthy', 1: 'powdery_mildew', 2: 'rust'}  # match your labels
model = load_model("model/leaf_model.h5")

def predict_image(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (128, 128))
    img = np.expand_dims(img, axis=0) / 255.0
    prediction = model.predict(img)
    class_idx = np.argmax(prediction)
    return label_map[class_idx]

# Example usage
print(predict_image("sample_leaf.jpg"))
