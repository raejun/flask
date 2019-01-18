import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_DIR = '.uploads'
ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif','zip'])

app = Flask(__name__)

# >>> import os
# >>> os.urandom(24)
# b"'\xa6\xe8\xd2\xe1\x9e\xdd\xd23P\xf2\xd4Bls\xfer\x18\xac\xe3Nfr\x1d"

app.secret_key = '\xa6\xe8\xd2\xe1\x9e\xdd\xd23P\xf2\xd4Bls\xfer\x18\xac\xe3Nfr\x1d'

app.config['UPLOAD_FOLDER'] = UPLOAD_DIR
app.config['MAX_CONTENT_LENGTH'] = 10*1024*1024 # 최대 10MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in
    ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', method=['GET', 'POST'])
def upload():
    if request.method == 'POST' :
        pass
    else: 

if __name__ == '__main__':
    app.run(debug=True)