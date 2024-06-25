import google.genearativeai as genai
import speech_recognition as sr
import pyttsx3
import os
import pyaudio
from datetime import date
import time

#from OpenAI TTS model
from openai import OpenAI
import pygame
client=OpenAI()


pygame.mixer.init()
#os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"

#set the google gemini api key here or a system environmental variable 

#genai.configure(api_key=GOOGLE_API_KEY)

today=str(date.today())

engine=pyttsx3.init()

engine.setProperty('rate',190) #speaking rate 
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id) #0 for male and #1 for female 

model=genai.GenerativeModel('gemini-pro')

openaitts=False

def speak_text(text):
    global openaitts

    if openaitts:

        response=client.audio.speech.create(
            model='tts-1'
            #alloy:man,nova:female 
            voice='nova'
            input=text
          )
        fname='output.mp3'
        mp3file=open(fname,'w+')

        #if os.path.exists(fname):
        # os.remove(fname)

        response.write_to_file(fname)

        try:
            pygame.mixer.music.load(mp3file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.25)

            pygame.mixer.music.stop()
            mp3file.close()

        except KeyboardInterrupt:
            pygame.mixer.music.stop()
            mp3file.close()
            #print('\n Audio playback stopped')
    else :
        engine.say(text)
        #print("AI: "+text)
        engine.runAndWait()

talk=[]

def append2log(text):
    global today
    fname='chatlog-'+today+'.txt' 
    with open(fname,'a') as f :
        f.write(text+'\n')


def main():
      global talk,today,model

      rec=sr.Recongnizer()
      mic=sr.Microphine()
      rec.dynamic_energy_threshold=False
      rec.energy_threshold=400

      sleeping =True

    while True:
         
         with mic as source1:
              rec.adjust_for_ambinet_noise(source1,duration=0.5)
              print("Listening .................")
              





    

