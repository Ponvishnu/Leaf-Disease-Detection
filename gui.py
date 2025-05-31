import tkinter as tk
from tkinter import filedialog
from predict import predict_image

def browse_and_predict():
    path = filedialog.askopenfilename()
    if path:
        result = predict_image(path)
        result_label.config(text=f"Prediction: {result}")

root = tk.Tk()
root.title("Leaf Disease Detector")

tk.Button(root, text="Select Leaf Image", command=browse_and_predict).pack(pady=20)
result_label = tk.Label(root, text="Prediction: ", font=("Arial", 16))
result_label.pack(pady=20)

root.mainloop()
