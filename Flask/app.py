#simple flask boilerplate
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from ImageToSpeech import *

app = Flask(__name__)

pic_sent = False

@app.route('/')
def index():
    return render_template('index.html')

#return audio file
@app.route('/audiofile', methods=['GET'])
def audiofile():
    global pic_sent
    #return audio.mp3 file 
    if pic_sent == True:
        return send_file('audio_out.mp3')
        pic_sent = False
    else:
        pic_sent = True
        return "no audio file"

#image file upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    print(file)
    #save file
    file.save(secure_filename(file.filename))

    #take image file.png and create audio file audio.mp3

    image_to_file(file.png, LANGUAGES[0], ACCENTS[0][2])

    return "done"

if __name__ == '__main__':
    app.run(debug=True)