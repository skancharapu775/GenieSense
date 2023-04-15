import requests
import pygame

url = 'http://localhost:5000/audiofile'
r = requests.get(url, allow_redirects=True)

#only run if requests is successful
if r.status_code == 200:
    open('audiofile_downloaded.mp3', 'wb').write(r.content)
    pygame.mixer.init()
    pygame.mixer.music.load("audiofile_downloaded.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
else:
    print('Error: status code {}'.format(r.status_code))

