import requests
import pygame
import pygame
from time import sleep
import pygame.camera

url = 'http://localhost:5000/audiofile'
r = requests.get(url, allow_redirects=True)

#language is hard coded for now
language = 'english'

image_taken = False

while True:
    if image_taken == True and r.status_code == 200:
        open('audiofile_downloaded.mp3', 'wb').write(r.content)
        pygame.mixer.init()
        pygame.mixer.music.load("audiofile_downloaded.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        #if button is pressed, regenerate image
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                image_taken = False
    else:
        print('Error: status code {}'.format(r.status_code))
        pygame.camera.init()
        print(pygame.camera.list_cameras())#Camera detected or not
        cam = pygame.camera.Camera("Logi C270 HD WebCam",(640,480))
        cam.start()
        img = cam.get_image()
        print('pic taken')
        pygame.image.save(img,"camera_shot.jpg")
        #send file to flask api
        url = 'http://localhost:5000/imagefile'
        file = {'file': open('camera_shot.jpg', 'rb'), 'language': language}
        r = requests.post(url, files=file)
        print(r.status_code)
        print(r.text)
        cam.stop()
        pygame.camera.quit()
        #wait for model to generate the text
        sleep(5)
        #download the audio file by setting flag
        image_taken = True


