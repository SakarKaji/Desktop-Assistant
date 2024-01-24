import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk #PyWhatKit is a Simple and Powerful WhatsApp Automation Library with many useful Features
import os

import cv2
import pyautogui
import time
import operator
import requests
import sys


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
        speak("Good morniiiing Vietnaaaaam")

    elif hour >= 12 and hour<18:
         speak("Good eveniiing Vietnaaaaam")

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

        elif 'thank' in query:
            print("yes sir")
            speak("your welcome")

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

        elif 'search on youtube' in query:
            query = query.replace("seach on youtube","")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'close browser' in query:
            os.system("taskkill /f /im msedge.exe") #chrome.exe if it opens(or default browser is) chrome

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        #opening applications
        elif 'open paint' in query:
            npath = "C:\Windows\system32\\mspaint.exe"
            os.startfile(npath)
        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe") 


        # some funcions
        elif "open command prompt" in query:
            os.system("start cmd")
            
        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                 break;
            cap.release()
            cv2.destroyAllWndows()

        elif "go to sleep" in query:
            speak(' alright then, I am switching off')
            sys.exit()

        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot() 
            img.save(f"{name}.png") 
            speak("screenshot saved")

        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listning...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
             return {
            '+' : operator.add,
            '-' : operator.sub,
            'x' : operator.mul,
            'divided' : operator.__truediv__,
            }[op]
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_bianary_expr(*(my_string.split())))

        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")