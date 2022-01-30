from enum import auto
from gtts import gTTS
import random
import speech_recognition as sr
import pyaudio



words =  ['el','al','ela','lale','elele','elle','ali','kek','kekik']
text = random.choice(words)


tts = gTTS(text, lang='tr')
tts.save('hi.mp3')

import os
os.system("hi.mp3")

yourword = input('duyduğunuz kelimeyi yazınız..:'  )
from playsound import playsound
os.system("hi.mp3")



if text == yourword:
    print('doğru')
else:
    print('yanlış')











