from transformers import pipeline

'''
JPEG TO TEXT

- Can be translated to multiple languages
- Can do OCR tasks
- Can image caption

pip install transformers
'''

from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

def text(image_url):
    return NotImplementedError