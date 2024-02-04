# mahdiam youtube
# madgod.dev instagram
# gtts

from gtts import gTTS
import os

f=open('test.txt')
x=f.read()

language= 'en'

audio= gTTS(text=x, lang=language, slow=False)

audio.save('test.wav')
os.system('test.wav')