import keys
from transformers import pipeline

'''
JPEG TO TEXT

- Can be translated to multiple languages
- Can do OCR tasks
- Can image caption

pip install transformers
'''

url = "https://thumbs.dreamstime.com/z/man-meadow-14640739.jpg"
model = "nlpconnect/vit-gpt2-image-captioning"

def text(image_url):
    print("Start Process")
    image_to_text = pipeline("image-to-text", model=model)
    response = image_to_text(image_url)
    return response[0]["generated_text"]

print(text(url))

