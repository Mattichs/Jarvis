import speech_recognition as sr
from functions.online_ops import play_on_youtube, search_on_google, search_on_wikipedia
from decouple import config
import pyttsx3
from utils import opening_text
from datetime import datetime
from random import choice

# print list of devices
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))




USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('nsss')
# Set Rate
engine.setProperty('rate', 180)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()

# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        audio_data = recognizer.listen(source)

        # Perform speech recognition using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data, language='it')
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service;")

    return text


if __name__ == '__main__':
    while True:
        query = take_user_input().lower()
        #print(query)

        if 'wikipedia' in query:
            speak('What do you want to search on Wikipedia?')
            search_query = take_user_input().lower()
            print("search query: ", search_query)
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
