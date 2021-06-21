from pygame import mixer
from time import sleep
from random import randint

mixer.init()
mixer.music.load('ex021.mp3')
print(f'\033[{randint(30, 37)}mPreparando a música...')
sleep(3)
mixer.music.play()
input('Parar de ouvir?  ')
