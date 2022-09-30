import pyttsx3
import speech_recognition
from bs4 import BeautifulSoup
import requests
import datetime
import os
import pyautogui
import webbrowser
import random


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    print("   ")
    engine.say(audio)
    print(f": {audio}")
    print("   ")
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from Features import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "google" in query:
                    from Features import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from Features import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from Features import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temperature in jajpur road"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "weather" in query:
                    search = "temperature in jajpur road"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                elif "open" in query:
                    from Features import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Features import closeappweb
                    closeappweb(query)
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "skip" in query:
                    pyautogui.press("l")
                    speak("video skipped")
                elif "back" in query:
                    pyautogui.press("j")
                    speak("previous video played")
                elif "full screen" in query:
                    pyautogui.press("f")
                    speak("video full screen")
                elif "film mode" in query:
                    pyautogui.press("t")
                    speak("video theater mode")
                elif "volume up" in query:
                    from Features import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from Features import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt", "a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to remember that" + remember.read())
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    # You can choose any number of songs (I have only choosen 3)
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open(
                            "https://www.youtube.com/watch?v=ru0K8uYEZWw")
                    elif b == 2:
                        webbrowser.open(
                            "https://www.youtube.com/watch?v=jZhQOvvV45w")
                    else:
                        webbrowser.open(
                            "https://www.youtube.com/watch?v=rtOvBOTyX00")
