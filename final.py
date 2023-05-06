import test
import speech_recognition as sr
from extract import extrct
import simulation

def prog():
    while(1):
        test.record_on_detect('output')
        voice = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = voice.record(source)
            Text = voice.recognize_google(audio)
            Text = Text.lower()
            result = extrct(Text)
        print(result)
        simulation.simulate(result)
        
prog()