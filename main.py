import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os
from datetime import date
import time
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# Configure Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

today = str(date.today())

engine = pyttsx3.init()
engine.setProperty('rate', 190)  # speaking rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female

model = genai.GenerativeModel('gemini-pro')

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

talk = []

def append2log(text):
    global today
    fname = 'chatlog-' + today + '.txt'
    with open(fname, 'a') as f:
        f.write(text + '\n')

def main():
    global talk, today, model

    rec = sr.Recognizer()
    mic = sr.Microphone()
    rec.dynamic_energy_threshold = False
    rec.energy_threshold = 400
    sleeping = True

    while True:
        with mic as source1:
            rec.adjust_for_ambient_noise(source1, duration=0.5)
            print("Listening .................")

            try:
                audio = rec.listen(source1, timeout=10, phrase_time_limit=15)
                text = rec.recognize_google(audio)

                if sleeping:
                    if 'jack' in text.lower():
                        request = text.lower().split("jack")[1]
                        sleeping = False
                        append2log(f'_' * 40)
                        talk = []
                        today = str(date.today())

                        if len(request) < 5:
                            speak_text('hi, there, how can I help you?')
                            append2log(f'AI: hi, there, how can I help you?\n')
                            continue
                    else:
                        continue
                else:
                    request = text.lower()

                    if "that's all" in request:
                        append2log(f'You: {request}\n')
                        speak_text('Bye Now')
                        append2log(f"AI: Bye Now.\n")
                        print('bye now')
                        sleeping = True
                        continue

                    if 'jack' in request:
                        request = request.split('jack')[1]

                append2log(f"You: {request}\n")
                print(f'You: {request}\nAI: ')
                talk.append({'role': 'user', 'parts': [request]})

                response = model.generate_content(talk, stream=True)
                for chunk in response:
                    print(chunk.text, end=' ')
                    speak_text(chunk.text.replace("*", ""))

                print('\n')
                talk.append({'role': 'model', 'parts': [response.text]})
                append2log(f'AI: {response.text}\n')
            except Exception as e:
                continue

if __name__ == '__main__':
    main()
