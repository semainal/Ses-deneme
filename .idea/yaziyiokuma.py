import pyaudio
import speech_recognition as sr
import gtts
import random

r = sr.Recognizer()

word = ['el','al','ela','lale','elele','elle','ali','kek','kekik','anne']


result = (random.choice(word))
print(result)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    data = r.record(source, duration=2)
    text = r.recognize_google(data,language='tr')
    print(text.lower())

    

if text == result:
    print('doğru')
else:
    print('yanlış')

  
        
