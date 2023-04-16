print("Importing Libraries...")
from transformers import pipeline
from gtts import gTTS

'''
- Can be translated to multiple languages
- Can do OCR tasks
- Can image caption
'''

print("Imports Completed")

url = "https://cdn.discordapp.com/attachments/915276863272800297/1096883706213437510/Screen_Shot_2023-04-15_at_3.44.09_PM.png"
model = "nlpconnect/vit-gpt2-image-captioning"
LANGUAGES = ['en', 'es', 'fr', 'zh-CN']
ACCENTS = [['com.au', 'co.uk', 'us'], ['com.mx', 'es'], ['fr']]
NAME = "speech.mp3"

def image_to_text(image_url):
    print("Translating Text...")
    image_to_text = pipeline("image-to-text", model=model)
    response = image_to_text(image_url)
    return response[0]["generated_text"]

def text_to_file(text, language, accent):
    print("Generating Audio File...")
    obj = gTTS(text=text, lang=language, slow=False, tld=accent)
    obj.save(NAME)
    
    return NAME

def image_to_file(image_url, language, accent):
    text = image_to_text(image_url)
    filename = text_to_file(text, language, accent)
    print("Speech Generated!")
    return filename
