import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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
    while True:
        query = takeCommand().lower()

        if 'open chrome' in query:
            img = pyautogui.locateCenterOnScreen('screenshot1.png') 
            #[take a screenshot of chrome and crop it, then save the image in jarvis folder]
            pyautogui.doubleClick(img)
            time.sleep(1)
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
            time.sleep(1)
            img1 = pyautogui.locateCenterOnScreen('screenshot2.png') 
            #[take screenshot where you want to make the click]
            pyautogui.click(img1)
            time.sleep(2)
            img2 = pyautogui.locateCenterOnScreen('screenshot3.png')
            pyautogui.click(img2)
            time.sleep(1)
            pyautogui.typewrite('How To Manual',0.1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('esc')
            img3 = pyautogui.locateCenterOnScreen('screenshot4.png')
            pyautogui.click(img3)

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")