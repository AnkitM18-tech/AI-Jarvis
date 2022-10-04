import pyttsx3
import speech_recognition
from bs4 import BeautifulSoup
from pywhatkit.sc import shutdown
import requests
import os
import pyjokes
import keyboard
from pywikihow import search_wikihow
import webbrowser
import random
import speedtest
from plyer import notification
from pygame import mixer
import sys
import matplotlib.pyplot as pt
import pywhatkit
import wikipedia
import webbrowser
import random
import pyautogui
from time import sleep
from pynput.keyboard import Key, Controller
import requests
import wolframalpha
import json
import PyPDF2
from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans
from gtts import gTTS
from pydictionary import Dictionary as dictn
from playsound import playsound
import time
from datetime import timedelta
from datetime import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
from Jarvis2UI import Ui_MainWindow
from dotenv import load_dotenv
load_dotenv()

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


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        def greetMe():
            hour = int(datetime.now().hour)
            if hour >= 0 and hour <= 12:
                speak("Good Morning,sir")
            elif hour > 12 and hour <= 18:
                speak("Good Afternoon ,sir")

            else:
                speak("Good Evening,sir")

            speak("Please tell me, How can I help you ?")

        def searchGoogle(query):
            if "google" in query:
                import wikipedia as googleScrape
                query = query.replace("jarvis", "")
                query = query.replace("google search", "")
                query = query.replace("google", "")
                speak("This is what I found on google")

                try:
                    pywhatkit.search(query)
                    result = googleScrape.summary(query, 1)
                    speak(result)

                except:
                    speak("No speakable output available")

        def searchYoutube(query):
            if "youtube" in query:
                speak("This is what I found for your search!")
                query = query.replace("youtube search", "")
                query = query.replace("youtube", "")
                query = query.replace("jarvis", "")
                web = "https://www.youtube.com/results?search_query=" + query
                webbrowser.open(web)
                pywhatkit.playonyt(query)
                speak("Done, Sir")

        def searchWikipedia(query):
            if "wikipedia" in query:
                speak("Searching from wikipedia...")
                query = query.replace("wikipedia", "")
                query = query.replace("search wikipedia", "")
                query = query.replace("jarvis", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia...")
                print(results)
                speak(results)

        dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword",
                   "excel": "excel", "chrome": "chrome", "vscode": "code", "powerpoint": "powerpnt"}

        def openappweb(query):
            speak("Launching, sir")
            if ".com" in query or ".co.in" in query or ".org" in query:
                query = query.replace("open", "")
                query = query.replace("jarvis", "")
                query = query.replace("launch", "")
                query = query.replace(" ", "")
                webbrowser.open(f"https://www.{query}")
            else:
                keys = list(dictapp.keys())
                for app in keys:
                    if app in query:
                        os.system(f"start {dictapp[app]}")

        def closeappweb(query):
            import pyautogui
            speak("Closing,sir")
            if "one tab" in query or "1 tab" in query:
                pyautogui.hotkey("ctrl", "w")
                speak("All tabs closed")
            elif "2 tab" in query:
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                speak("All tabs closed")
            elif "3 tab" in query:
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                speak("All tabs closed")

            elif "4 tab" in query:
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                speak("All tabs closed")
            elif "5 tab" in query:
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
                pyautogui.hotkey("ctrl", "w")
                speak("All tabs closed")

            else:
                keys = list(dictapp.keys())
                for app in keys:
                    if app in query:
                        os.system(f"taskkill /f /im {dictapp[app]}.exe")

        def volumeup():
            keyboard_c = Controller()
            for i in range(5):
                keyboard_c.press(Key.media_volume_up)
                keyboard_c.release(Key.media_volume_up)
                sleep(0.1)

        def volumedown():
            keyboard_c = Controller()
            for i in range(5):
                keyboard_c.press(Key.media_volume_down)
                keyboard_c.release(Key.media_volume_down)
                sleep(0.1)

        def latestnews():
            API_KEY = os.getenv("NEWS_API_KEY")
            api_dict = {"business": f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}",
                        "entertainment": f"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={API_KEY}",
                        "health": f"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}",
                        "science": f"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={API_KEY}",
                        "sports": f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}",
                        "technology": f"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={API_KEY}"
                        }

            content = None
            url = None
            speak(
                "Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
            field = input("Type field news that you want: ")
            for key, value in api_dict.items():
                if key.lower() in field.lower():
                    url = value
                    print(url)
                    print("url was found")
                    break
                else:
                    url = True
            if url is True:
                print("url not found")

            news = requests.get(url).text
            news = json.loads(news)
            speak("Here is the first news.")

            arts = news["articles"]
            for articles in arts:
                article = articles["title"]
                print(article)
                speak(article)
                news_url = articles["url"]
                print(f"for more info visit: {news_url}")

                a = input("[press 1 to cont] and [press 2 to stop] - ")
                if str(a) == "1":
                    pass
                elif str(a) == "2":
                    break

            speak("thats all")

        def WolfRamAlpha(query):
            apikey = os.getenv("WOLFRAM_API_KEY")
            requester = wolframalpha.Client(apikey)
            requested = requester.query(query)

            try:
                answer = next(requested.results).text
                return answer
            except:
                speak("The value is not answerable")

        def Calculate(query):
            Term = str(query)
            Term = Term.replace("jarvis", "")
            Term = Term.replace("multiply", "*")
            Term = Term.replace("plus", "+")
            Term = Term.replace("minus", "-")
            Term = Term.replace("divide", "/")

            Final = str(Term)
            try:
                result = WolfRamAlpha(Final)
                print(f"{result}")
                speak(result)

            except:
                speak("The value is not answerable")

        def sendMessage():
            strTime = int(datetime.now().strftime("%H"))
            update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))
            speak("Who do you want to message")
            a = int(input('''Neha - 1,Kamakshi - 2 : '''))
            if a == 1:
                speak("Whats the message")
                message = str(input("Enter the message - "))
                pywhatkit.sendwhatmsg("+91000000000", message,
                                      time_hour=strTime, time_min=update)
            elif a == 2:
                speak("Whats the message")
                message = str(input("Enter the message - "))
                pywhatkit.sendwhatmsg("+91000000000", message,
                                      time_hour=strTime, time_min=update)

            speak("Sending Message!")

        def game_play():
            speak("Lets Play ROCK PAPER SCISSORS !!")
            print("LETS PLAYYYYYYYYYYYYYY!!!!!!!!!!!!")
            i = 0
            Me_score = 0
            Com_score = 0
            while (i < 5):
                choose = ("rock", "paper", "scissors")  # Tuple
                com_choose = random.choice(choose)
                query = takeCommand().lower()
                if (query == "rock"):
                    if (com_choose == "rock"):
                        speak("ROCK")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    elif (com_choose == "paper"):
                        speak("paper")
                        Com_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    else:
                        speak("Scissors")
                        Me_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

                elif (query == "paper"):
                    if (com_choose == "rock"):
                        speak("ROCK")
                        Me_score += 1
                        print(
                            f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

                    elif (com_choose == "paper"):
                        speak("paper")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    else:
                        speak("Scissors")
                        Com_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

                elif (query == "scissors" or query == "scissor"):
                    if (com_choose == "rock"):
                        speak("ROCK")
                        Com_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    elif (com_choose == "paper"):
                        speak("paper")
                        Me_score += 1
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                    else:
                        speak("Scissors")
                        print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                i += 1

            print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")

        def focus_graph():
            file = open("focus.txt", "r")
            content = file.read()
            file.close()
            content = content.split(",")
            x1 = []
            for i in range(0, len(content)):
                content[i] = float(content[i])
                x1.append(i)
            print(content)
            y1 = content
            pt.plot(x1, y1, color="red", marker="o")
            pt.title("YOUR FOCUSED TIME", fontsize=16)
            pt.xlabel("Times", fontsize=14)
            pt.ylabel("Focus Time", fontsize=14)
            pt.grid()
            pt.show()

        def translategl(query):
            speak("SURE SIR")
            print(googletrans.LANGUAGES)
            translator = Translator()
            speak("Choose the language in which you want to translate")
            b = input("To_Lang :- ")
            text_to_translate = translator.translate(
                query, src="auto", dest=b,)
            text = text_to_translate.text
            try:
                speakgl = gTTS(text=text, lang=b, slow=False)
                speakgl.save("voice.mp3")
                playsound("voice.mp3")

                time.sleep(5)
                os.remove("voice.mp3")
            except:
                print("Unable to translate")

        def Music():
            speak("Tell me the Name of the Song!")
            musicName = takeCommand().lower()

            if "off" in musicName:
                os.startfile("D:\\GitHub\\AI-Jarvis\\Off My Face.mp3")
            else:
                pywhatkit.playonyt(musicName)
                speak("Your Song Has Been Started!, Enjoy Sir!")

        def Dictionary():
            speak("Opened Dictionary")
            speak("Tell me the word!")
            word = takeCommand().lower()

            if "meaning" in word:
                word = word.replace("what is the", "")
                word = word.replace("jarvis", "")
                word = word.replace("of", "")
                word = word.replace("meaning", "")
                temp_word = word
                word = dictn(word)
                result = word.meanings()
                speak(f"The meanings for {temp_word} is : {result}")
            elif "synonym" in word:
                word = word.replace("what is the", "")
                word = word.replace("jarvis", "")
                word = word.replace("of", "")
                word = word.replace("synonym", "")
                temp_word = word
                word = dictn(word)
                result = word.synonyms()
                speak(f"The synonyms for {temp_word} is : {result}")
            elif "antonym" in word:
                word = word.replace("what is the", "")
                word = word.replace("jarvis", "")
                word = word.replace("of", "")
                word = word.replace("antonym", "")
                temp_word = word
                word = dictn(word)
                result = word.antonyms()
                speak(f"The antonyms for {temp_word} is : {result}")

            speak("Exited Dictionary!")

        def Reader():
            speak("Tell me the Name of the Book!")
            name = takeCommand().lower()
            if "manager" in name:
                os.startfile(
                    "D:\\GitHub\\AI-Jarvis\\The One Minute Manager.pdf")
                book = open(
                    "D:\\GitHub\\AI-Jarvis\\The One Minute Manager.pdf", "rb")
                pdfReader = PyPDF2.PdfFileReader(book)
                pages = pdfReader.getNumPages()
                speak(f"Number Of Pages In this Books Are {pages}")
                speak("From Which Page I have to start reading ?")
                numPage = int(input("Enter Page number : "))
                page = pdfReader.getPage(numPage)
                text = page.extractText()
                speak("In Which Language , Do I have to Read ?")
                lang = takeCommand()

                if "hindi" in lang:
                    translate = Translator()
                    textHindi = translate.translate(text, "hi")
                    textTm = textHindi.text
                    speech = gTTS(text=textTm)
                    try:
                        speech.save("book.mp3")
                        playsound("book.mp3")
                    except:
                        playsound("book.mp3")
                else:
                    speak(text)

        def AutomateChrome():
            import pyautogui
            speak("Chrome Automation Launched")
            speak("What's Your Command Sir?")
            command = takeCommand()
            if "close this tab" in command:
                # keyboard.press_and_release("ctrl + w") # import keyboard
                pyautogui.hotkey("ctrl", "w")
            elif "open new tab" in command:
                # keyboard.press_and_release("ctrl + t")
                pyautogui.hotkey("ctrl", "t")
            elif "open new window" in command:
                # keyboard.press_and_release("ctrl + n")
                pyautogui.hotkey("ctrl", "n")
            elif "history" in command:
                # keyboard.press_and_release("ctrl + h")
                pyautogui.hotkey("ctrl", "h")

        while True:
            query = takeCommand().lower()
            if "wake up" in query:
                # from Features import greetMe
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
                        # from Features import searchGoogle
                        searchGoogle(query)
                    elif "youtube" in query:
                        # from Features import searchYoutube
                        searchYoutube(query)
                    elif "wikipedia" in query:
                        # from Features import searchWikipedia
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
                        # from Features import openappweb
                        openappweb(query)
                    elif "close" in query:
                        # from Features import closeappweb
                        closeappweb(query)
                    elif "set an alarm" in query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,sir")
                    elif "pause" in query:
                        import pyautogui
                        pyautogui.press("k")
                        speak("video paused")
                    elif "play" in query:
                        import pyautogui
                        pyautogui.press("k")
                        speak("video played")
                    elif "mute" in query:
                        import pyautogui
                        pyautogui.press("m")
                        speak("video muted")
                    elif "skip" in query:
                        import pyautogui
                        pyautogui.press("l")
                        speak("video skipped")
                    elif "back" in query:
                        import pyautogui
                        pyautogui.press("j")
                        speak("previous video played")
                    elif "full screen" in query:
                        import pyautogui
                        pyautogui.press("f")
                        speak("video full screen")
                    elif "film mode" in query:
                        import pyautogui
                        pyautogui.press("t")
                        speak("video theater mode")
                    elif "volume up" in query:
                        # from Features import volumeup
                        speak("Turning volume up,sir")
                        volumeup()
                    elif "volume down" in query:
                        # from Features import volumedown
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
                        # from Features import latestnews
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
                        # from Features import WolfRamAlpha
                        # from Features import Calculate
                        query = query.replace("calculate", "")
                        query = query.replace("jarvis", "")
                        Calculate(query)
                    elif "whatsapp" in query:
                        # from Features import sendMessage
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
                        import pyautogui
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
                        # from Features import game_play
                        game_play()
                    elif "screenshot" in query:
                        import pyautogui
                        im = pyautogui.screenshot()
                        name = datetime.now().strftime("%H:%M:%S")
                        name = name.replace(":", "")
                        name = name.replace(" ", "")
                        im.save(f"Screenshots/ss-{name}.jpg")
                        os.startfile("D:\\GitHub\\AI-Jarvis\\Screenshots")
                        speak("Here is your ScreenShot Sir!")
                    elif "click my photo" in query:
                        import pyautogui
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
                        # from Features import focus_graph
                        focus_graph()
                    elif "translate" in query:
                        # from Features import translategl
                        query = query.replace("jarvis", "")
                        query = query.replace("translate", "")
                        translategl(query)
                    elif "music" in query:
                        # from Features import Music
                        Music()
                    elif "dictionary" in query:
                        # from Features import Dictionary
                        Dictionary()
                    elif "read book" in query:
                        # from Features import Reader
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
                        # from Features import AutomateChrome
                        AutomateChrome()


startFunctions = MainThread()


class GUI_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.startbtn.clicked.connect(self.startFunction)
        self.jarvis_ui.exitbtn.clicked.connect(self.close)

    def startFunction(self):
        self.jarvis_ui.gif_foreground = QtGui.QMovie(
            ".\\GUI/ExtraGui/Jarvis_Gui (2).gif")
        self.jarvis_ui.foreground.setMovie(self.jarvis_ui.gif_foreground)
        self.jarvis_ui.gif_foreground.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        startFunctions.start()

    def showTime(self):
        current_time = QTime.currentTime()
        labelTime = current_time.toString("hh:mm:ss")
        showLabel = "Time : " + labelTime
        self.jarvis_ui.textBrowser.setText(showLabel)


Gui_App = QApplication(sys.argv)
Gui_Jarvis = GUI_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())
