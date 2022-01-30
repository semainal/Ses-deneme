import random
import string
import pyaudio
import speech_recognition as sr
from gtts import gTTS


sntc1 = 'Ela lale elele'
sntc2 = 'Ela kekik al'
sntc3 = 'Lale kek al'
sntc4 = 'Ali keklik ile nane al'
sntc5 = 'Nil ile Ela keke nane ekle'

list = [sntc1,sntc2, sntc3, sntc4, sntc5]

rnd_sntc = random.choice(list)

tts = gTTS(rnd_sntc, lang='tr')
tts.save('hi.mp3')

import os
os.system("hi.mp3")


from playsound import playsound
os.system("hi.mp3")



result =rnd_sntc.split()
shuffle = random.sample(result,len(result))
print(shuffle)


yoursntc= input('duyduğunuz cümleyi sırasıyle yazınız..:'  )

if yoursntc == rnd_sntc:
    print('doğru')
else:
    print('yanlış')




