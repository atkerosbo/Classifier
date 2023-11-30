import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras import models

class_names = {
    0: 'airplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck',
}

model = models.load_model('baseline_mariya.keras')

def predict_image(model, path_to_img):
    img = Image.open(path_to_img)
    img = img.convert("RGB")
    img = img.resize((32, 32))
    data = np.asarray(img)
    data = data / 255
    probs = model.predict(np.array([data])[:1])

    top_prob = probs.max()
    top_pred = class_names[np.argmax(probs)]
    
    return top_prob, top_pred

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Classifier")

        self.content_label = tk.Label(root, text="Select an image from your file system")
        self.content_label.pack()

        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.pack()

        self.pred_label = tk.Label(root, text="")
        self.pred_label.pack()

        self.img_label = tk.Label(root)
        self.img_label.pack()

        self.prob_label = tk.Label(root, text="")
        self.prob_label.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            top_prob, top_pred = predict_image(model, file_path)
            self.pred_label.config(text=f"This is a {top_pred}")
            self.prob_label.config(text=f"Probability: {round(top_prob * 100)}%")

            img = Image.open(file_path)
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            self.img_label.config(image=img)
            self.img_label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
