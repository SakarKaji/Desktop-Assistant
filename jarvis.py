import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk #PyWhatKit is a Simple and Powerful WhatsApp Automation Library with many useful Features



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good morning Vietnaaaaam")

    elif hour >= 12 and hour<18:
         speak("Good evening Vietnaaaaam")

    else:
        speak("Good Evening!")
    
    speak("Ready To Comply. What can i do for you ?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source: #microphone as source
        print("Listening...") #print listening.. which makes sure it is listening
        r.pause_threshold = 1 #pausee threshold 1 sec so that it listens for 1 sec
        audio = r.listen(source) 

    try:
        print("Recognizing...")
        query = r.recognize_google(audio ,language='en')
        print(f"USer said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        #speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'hey rajan' in query:
            print("yes sir")
            speak("yes sir banus")

        elif 'what is' in query:
            speak("Searching Wikipediia...")
            query = query.replace("what is","" )
            results = wikipedia.summary(query, sentences=2)
            speak("ACcording to Wikipedia")
            print(results)
            speak(results)   

        elif 'who is' in query:
            speak("Searching Wikipediia...")
            query = query.replace("who is","")
            results = wikipedia.summary(query, sentences=2)
            speak("ACcording to Wikipedia")
            print(results)
            speak(results)   

        elif 'just open google' in query:
            webbrowser.open('google.com')   

        elif 'open google' in query:
            speak("What should i search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)   

        elif 'just open youtube' in query:
            webbrowser.open('youtube.com') 
        
        elif 'open youtube' in query:
            speak("What woould you like to watch?")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}")