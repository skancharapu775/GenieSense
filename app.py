#simple flask boilerplate
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#return audio file
@app.route('/audiofile', methods=['GET', 'POST'])
def audiofile():
    #return audio.mp3 file 
    return send_file('audio.mp3', mimetype='audio/mp3')

#image file upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    print(file)
    #save file
    file.save(secure_filename(file.filename))
    return "done"

if __name__ == '__main__':
    app.run(debug=True)


