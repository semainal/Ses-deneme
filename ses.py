
from gtts import gTTS


tts = gTTS(text = 'merhaba ben tolga', lang='tr')
tts.save("hi.mp3")

import os 
os.system("hi.mp3")

from playsound import playsound
os.system("user_input.mp3")


