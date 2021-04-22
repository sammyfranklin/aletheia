import os, os.path, time
from werkzeug.utils import secure_filename
from flask import Flask, request
from effnetb0 import Effnetb0

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.nitf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
model = Effnetb0()

@app.route('/')
def index():
    return 'Aletheia Service: Try uploading an image to /classify to use this model'

@app.route('/classify', methods=['GET', 'POST'])
def classify():
    def is_file_allowed(filename):
        return os.path.splitext(filename)[1].lower() in ALLOWED_EXTENSIONS
    file = request.files.get('file')
    if file == None or file == '':
        return 'No file given'
    elif not is_file_allowed(file.filename):
        return 'File not allowed. Received {0} but was expecting one of types {1}'.format(file.filename, ALLOWED_EXTENSIONS)
    else:
        filename = secure_filename(file.filename)
        save_destination = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_destination)
        pred = model.classify([save_destination])
        return {
            "pred": str(pred[0]),
        }