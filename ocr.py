import io
import json
import cv2
import numpy as np
import requests
import urllib.request
import keys

image_url = "https://cdn.discordapp.com/attachments/915276863272800297/1096930577682288780/2Q.png"
req = urllib.request.urlopen(image_url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1) 

height, width, _ = img.shape

url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)


result = requests.post(url_api,
              files = {image_url: file_bytes},
              data = {"apikey": keys.OCR_SPACE_API_KEY,
                      "language": "eng"})

result = result.content.decode()
result = json.loads(result)

parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")
print(text_detected)
