from flask import Flask, render_template, request, url_for, send_from_directory
from tensorflow.keras import models
from PIL import Image
import numpy as np
import os
from werkzeug.utils import secure_filename

application = Flask(__name__)

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

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

@application.route("/", methods=["GET", "POST"])
def index():
    content = ""
    img_path = ""
    prob = 0
    pred = ""

    if request.method == "POST" and "content" in request.files:
        file = request.files["content"]

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(application.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            content = file_path
            top_prob, top_pred = predict_image(model, file_path)
            prob = round(top_prob * 100)
            pred = "This is a " + top_pred
            img_path = url_for('uploaded_file', filename=filename)

    return render_template("index.html", content=content, img_path=img_path, prob=prob, pred=pred)

@application.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(application.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    application.run(debug=True)