import pyttsx3
import speech_recognition
from bs4 import BeautifulSoup
from pywhatkit.sc import shutdown
import requests
import datetime
import os
import pyjokes
import keyboard
from pywikihow import search_wikihow
import pyautogui
import webbrowser
import random
import speedtest
from plyer import notification
from pygame import mixer

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i == 2 and a != pw):
        exit()

    elif (a != pw):
        print("Try Again")


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
                elif "news" in query:
                    from Features import latestnews
                    latestnews()
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input(
                        "Do you wish to shutdown your computer? (yes/no) : ")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break
                elif "calculate" in query:
                    from Features import WolfRamAlpha
                    from Features import Calculate
                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calculate(query)
                elif "whatsapp" in query:
                    from Features import sendMessage
                    sendMessage()
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
                elif "schedule my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )
                elif "open by pyauto" in query:
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576  # Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ", download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                elif "game" in query:
                    from Features import game_play
                    game_play()
                elif "screenshot" in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    name = datetime.datetime.now().strftime("%H:%M:%S")
                    name = name.replace(":", "")
                    name = name.replace(" ", "")
                    im.save(f"Screenshots/ss-{name}.jpg")
                    os.startfile("D:\\GitHub\\AI-Jarvis\\Screenshots")
                    speak("Here is your ScreenShot Sir!")
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                    speak("Picture Clicked Sir!")
                elif "focus mode" in query:
                    a = int(input(
                        "Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO] :-  "))
                    if (a == 1):
                        speak("Entering the focus mode....")
                        os.startfile(
                            "D:\\GitHub\\AI-Jarvis\\FocusMode.py")
                        exit()
                    else:
                        pass
                elif "show my focus" in query:
                    from Features import focus_graph
                    focus_graph()
                elif "translate" in query:
                    from Features import translategl
                    query = query.replace("jarvis", "")
                    query = query.replace("translate", "")
                    translategl(query)
                elif "music" in query:
                    from Features import Music
                    Music()
                elif "dictionary" in query:
                    from Features import Dictionary
                    Dictionary()
                elif "read book" in query:
                    from Features import Reader
                    Reader()
                elif "joke" in query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                elif "my location" in query:
                    speak("Ok sir, Wait a second!")
                    webbrowser.open(
                        "https://www.google.com/maps/@20.9425897,86.1242782,15z")
                elif "how to" in query:
                    speak("Getting Data From Internet!")
                    op = query.replace("jarvis", "")
                    max_result = 1
                    how_to_function = search_wikihow(op, max_result)
                    assert len(how_to_function) == 1
                    how_to_function[0].print()
                    speak(how_to_function[0].summary)
                elif "close this tab" in query:
                    keyboard.press_and_release("ctrl + w")
                elif "open new tab" in query:
                    keyboard.press_and_release("ctrl + t")
                elif "open new window" in query:
                    keyboard.press_and_release("ctrl + n")
                elif "history" in query:
                    keyboard.press_and_release("ctrl + h")
                elif "chrome automation" in query:
                    from Features import AutomateChrome
                    AutomateChrome()
