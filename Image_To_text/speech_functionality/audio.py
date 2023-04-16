"""
Find fast way to convert text to sound
pip install gTTS
"""
from gtts import *
import os

LANGUAGES = ['en']
NAME = "speech.mp3"

# turns text into audio file
def generate_file(text, language):
    obj = gTTS(text=text, lang=language, slow=False)
    obj.save(NAME)
    
    return NAME