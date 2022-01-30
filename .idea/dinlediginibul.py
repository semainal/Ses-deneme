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


from playsound import playsound
os.system("hi.mp3")


choice = (random.choice(words),random.choice(words),random.choice(words), text)
shuffle = random.sample(choice,len(choice))




print(shuffle)
result = input('Dinlediğiniz kelime hangisidir?')




if result == text:
    print('doğru')
else:
    print(text)
    print('yanlış')





