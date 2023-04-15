#simple flask boilerplate
from flask import Flask, render_template, request, redirect, url_for, flash, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audiofile', methods=['GET', 'POST'])
def audiofile():
    #return audio.mp3 file 
    return send_file('speech.mp3', mimetype='audio/mp3')

if __name__ == '__main__':
    app.run(debug=True)
