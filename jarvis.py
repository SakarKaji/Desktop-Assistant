import pyttsx3
import speech_recognition as speech_recognition


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voice')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

