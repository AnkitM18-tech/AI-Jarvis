import pyttsx3
import speech_recognition as sr
import webbrowser as browser
import pywhatkit as pwk
from googletrans import Translator
import os
import sys
from pywikihow import search_wikihow
import requests
from bs4 import BeautifulSoup
import wikipedia
import pyautogui as pag
import keyboard
import pyjokes
import PyPDF2
import time
import chatbot
from gtts import gTTS
import datetime
from playsound import playsound
from pydictionary import Dictionary as dict
from JarvisUI import Ui_JarvisUI
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

assistant = pyttsx3.init("sapi5")
voices = assistant.getProperty("voices")
# print(voices)
assistant.setProperty("voices", voices[0].id)
assistant.setProperty("rate", 170)


def Speak(audio):
    print("   ")
    assistant.say(audio)
    print(f": {audio}")
    print("   ")
    assistant.runAndWait()


def TakeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)
        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language="en-in")
            print(f"You Said : {query}")
        except Exception as Error:
            print("Say that again!")
            return "None"
        return query.lower()


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):

        Speak("Hello, I am Jarvis")
        Speak("How Can I Help You ?")

        def Music():
            Speak("Tell me the Name of the Song!")
            musicName = TakeCommand()

            if "off" in musicName:
                os.startfile("D:\\GitHub\\AI-Jarvis\\Off My Face.mp3")
            else:
                pwk.playonyt(musicName)
            Speak("Your Song Has Been Started!, Enjoy Sir!")

        def Whatsapp():
            Speak("Tell me the Name of the Person!")
            name = TakeCommand()

            if "neha" in name:
                Speak("Tell Me the Message you want to send!")
                msg = TakeCommand()
                Speak("Tell Me the time Sir!")
                Speak("Time in Hour")
                hour = int(TakeCommand())
                Speak("Time in Minutes")
                mins = int(TakeCommand())
                pwk.sendwhatmsg("+919999999999", msg, hour, mins, 20)
                Speak("Ok Sir!, Sending WhatsApp Message!")
            elif "kamakshi" in name:
                Speak("Tell Me the Message you want to send!")
                msg = TakeCommand()
                Speak("Tell Me the time Sir!")
                Speak("Time in Hour")
                hour = int(TakeCommand())
                Speak("Time in Minutes")
                mins = int(TakeCommand())
                pwk.sendwhatmsg("+919999999999", msg, hour, mins, 20)
                Speak("Ok Sir!, Sending WhatsApp Message!")
            else:
                Speak("Tell Me the phone number!")
                phone = int(TakeCommand())
                phNo = "+91" + phone
                Speak("Tell Me the Message you want to send!")
                msg = TakeCommand()
                Speak("Tell Me the time Sir!")
                Speak("Time in Hour")
                hour = int(TakeCommand())
                Speak("Time in Minutes")
                mins = int(TakeCommand())
                pwk.sendwhatmsg(phNo, msg, hour, mins, 20)
                Speak("Ok Sir!, Sending WhatsApp Message!")

        def OpenApp():
            Speak("Ok Sir!, Wait a second")
            if "code" in query:
                os.startfile(
                    "C:\\Users\\ankit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif "sublime" in query:
                os.startfile(
                    "D:\\Sublime Text\\Sublime Text 4\\Sublime Text\\sublime_text.exe")
            elif "github" in query:
                os.startfile(
                    "C:\\Users\\ankit\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
            elif "chrome" in query:
                os.startfile(
                    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            elif "instagram" in query:
                browser.open("https://www.instagram.com/")
            elif "maps" in query:
                browser.open(
                    "https://www.google.com/maps/@20.9425897,86.1242782,15z")
            elif "youtube" in query:
                browser.open("https://www.youtube.com/")

            Speak("Your Command Has been Completed Sir!")

        def CloseApp():
            Speak("Ok Sir!, Wait a second")

            if "youtube" in query:
                os.system("TASKKILL /F /im chrome.exe")
            elif "chrome" in query:
                os.system("TASKKILL /F /im chrome.exe")
            elif "code" in query:
                os.system("TASKKILL /F /im Code.exe")
            elif "sublime" in query:
                os.system("TASKKILL /F /im sublime_text.exe")
            elif "github" in query:
                os.system("TASKKILL /F /im GitHubDesktop.exe")
            elif "instagram" in query:
                os.system("TASKKILL /F /im chrome.exe")

            Speak("Your Command Has been Completed Sir!")

        def Temp():
            search = "temperature in"
            city = input("Enter your city:")
            url = "https://www.google.com/search?q=" + search + " " + city
            result = requests.get(url)
            data = BeautifulSoup(result.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            Speak(f"The Temperature outside is {temp}")

        def AutomateYoutube():
            Speak("What's Your Command Sir?")
            command = TakeCommand()
            if "pause" in command:
                keyboard.press("space bar")
            elif "restart" in command:
                keyboard.press("0")
            elif "mute" in command:
                keyboard.press("m")
            elif "skip" in command:
                keyboard.press("l")
            elif "back" in command:
                keyboard.press("j")
            elif "full screen" in command:
                keyboard.press("f")
            elif "film mode" in command:
                keyboard.press("t")

            Speak("Done Sir!")

        def AutomateChrome():
            Speak("Chrome Automation Launched")
            Speak("What's Your Command Sir?")
            command = TakeCommand()
            if "close this tab" in command:
                keyboard.press_and_release("ctrl + w")
            elif "open new tab" in command:
                keyboard.press_and_release("ctrl + t")
            elif "open new window" in command:
                keyboard.press_and_release("ctrl + n")
            elif "history" in command:
                keyboard.press_and_release("ctrl + h")

        def Dictionary():
            Speak("Opened Dictionary")
            Speak("Tell me the word!")
            word = TakeCommand()

            if "meaning" in word:
                word = word.replace("what is the", "")
                word = word.replace("jarvis", "")
                word = word.replace("of", "")
                word = word.replace("meaning", "")
                word = dict(word)
                result = word.meanings()
                Speak(f"The meanings for {word} is : {result}")
            elif "synonym" in word:
                word = word.replace("what is the", "")
                word = word.replace("jarvis", "")
                word = word.replace("of", "")
                word = word.replace("synonym", "")
                word = dict(word)
                result = word.synonyms()
                Speak(f"The synonyms for {word} is : {result}")
            elif "antonym" in word:
                word = word.replace("what is the", "")
                word = word.replace("jarvis", "")
                word = word.replace("of", "")
                word = word.replace("antonym", "")
                word = dict(word)
                result = word.antonyms()
                Speak(f"The antonyms for {word} is : {result}")

            Speak("Exited Dictionary!")

        def Screenshot():
            Speak("Ok Sir, What should I name this File?")
            file = TakeCommand()
            fileName = file + ".png"
            path = "D:\\GitHub\\AI-Jarvis\\Screenshots\\" + fileName
            ss = pag.screenshot()
            ss.save(path)
            os.startfile("D:\\GitHub\\AI-Jarvis\\Screenshots")
            Speak("Here is your ScreenShot Sir!")

        def TakeHindiCommand():
            command = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                command.pause_threshold = 1
                audio = command.listen(source)
                try:
                    print("Recognizing...")
                    query = command.recognize_google(audio, language="hi")
                    print(f"You Said : {query}")
                except Exception as Error:
                    print("Say that again!")
                    return "none"
                return query.lower()

        def Translate():
            Speak("Tell Me the Line!")
            line = TakeHindiCommand()
            translator = Translator()
            result = translator.translate(line)
            Text = result.text
            Speak(f"The translation for the given line is: {Text}")

        def Reader():
            Speak("Tell me the Name of the Book!")
            name = TakeCommand()
            if "india" in name:
                os.startfile(
                    "D:\\GitHub\\AI-Jarvis\\The One Minute Manager.pdf")
                book = open(
                    "D:\\GitHub\\AI-Jarvis\\The One Minute Manager.pdf", "rb")
                pdfReader = PyPDF2.PdfFileReader(book)
                pages = pdfReader.getNumPages()
                Speak(f"Number Of Pages In this Books Are {pages}")
                Speak("From Which Page I have to start reading ?")
                numPage = int(input("Enter Page number : "))
                page = pdfReader.getPage(numPage)
                text = page.extractText()
                Speak("In Which Language , I have to Read ?")
                lang = TakeCommand()

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
                    Speak(text)
            elif "europe" in name:
                os.startfile(
                    "D:\\GitHub\\AI-Jarvis\\The One Minute Manager.pdf")
                book = open(
                    "D:\\GitHub\\AI-Jarvis\\The One Minute Manager.pdf", "rb")
                pdfReader = PyPDF2.PdfFileReader(book)
                pages = pdfReader.getNumPages()
                Speak(f"Number Of Pages In this Books Are {pages}")
                Speak("From Which Page I have to start reading ?")
                numPage = int(input("Enter Page number : "))
                page = pdfReader.getPage(numPage)
                text = page.extractText()
                Speak("In Which Language , I have to Read ?")
                lang = TakeCommand()

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
                    Speak(text)

        def SpeedTest():
            import speedtest
            Speak("Checking speed...")
            speed = speedtest.Speedtest()
            downloadingSpeedMBPT = speed.download()
            downloadingSpeedMBPS = int(downloadingSpeedMBPT/800000)
            uploadingSpeedMBPT = speed.upload()
            uploadingSpeedMBPS = int(uploadingSpeedMBPT/800000)

            if "uploading" in query:
                Speak(f"The Uploading Speed is : {uploadingSpeedMBPS} MB/s")
            elif "downloading" in query:
                Speak(
                    f"The Downloading Speed is : {downloadingSpeedMBPS} MB/s")
            else:
                Speak(
                    f"The Downloading Speed is : {downloadingSpeedMBPS} MB/s and The Uploading Speed is : {uploadingSpeedMBPS} MB/s")

        def WhatsAppAdv(number, message):
            phNo = '+91' + int(number)
            messageText = message
            open_chat = "https://web.whatsapp.com/send?photo=" + phNo + "&text=" + messageText
            browser.open(open_chat)
            time.sleep(15)
            keyboard.press("enter")

        def WhatsAppAdvGroup(group_id, message):
            open_chat = "https://web.whatsapp.com/accept?code=" + group_id
            browser.open(open_chat)
            time.sleep(15)
            keyboard.write(message)
            time.sleep(2)
            keyboard.press("enter")

        while True:
            query = TakeCommand()
            if "hello" in query:
                Speak("Hello Sir, I am Jarvis.")
                Speak("Your Personal AI Assistant.")
                Speak("How May I Help you?")
            elif "how are you" in query:
                Speak("I am Fine Sir!")
                Speak("What about You?")
            elif "you need a break" in query:
                Speak("Ok Sir, You can call me anytime!")
                Speak("Just Say Wake Up Jarvis!")
                break
            elif "bye" in query:
                Speak("Ok Sir , Bye!")
                break
            elif "youtube search" in query:
                Speak("OK Sir!, This is what I found for Your Search!")
                query = query.replace("jarvis", "")
                query = query.replace("youtube search", "")
                youtube = "https://www.youtube.com/results?search_query=" + query
                browser.open(youtube)
                Speak("Done Sir!")
            # elif "google search" in query:
            #     Speak("This is what I found for your Search Sir!")
            #     query = query.replace("google search", "")
            #     query = query.replace("jarvis", "")
            #     pwk.search(query)
            #     Speak("Done Sir!")
            elif "website" in query:
                Speak("Ok sir! Launching...")
                query = query.replace("jarvis", "")
                query = query.replace("website", "")
                query = query.replace(" ", "")
                website1 = query.replace("open", "")
                website2 = "https://www." + website1 + ".com"
                browser.open(website2)
                Speak("Launched The Website Sir!")
            elif "launch" in query:
                Speak("Tell me the name of the website!")
                name = TakeCommand()
                name = name.replace(" ", "")
                web = "https://www." + name + ".com"
                browser.open(web)
                Speak("Website launched Sir!")
            elif "music" in query:
                Music()
            elif "wikipedia" in query:
                Speak("Searching Wikipedia...")
                query = query.replace("jarvis", "")
                query = query.replace("wikipedia", "")
                wiki = wikipedia.summary(query, 2)
                Speak(f"According to Wikipedia : {wiki}")
            elif "whatsapp message" in query:
                Whatsapp()
            elif "screenshot" in query:
                Screenshot()
            elif "open chrome" in query:
                OpenApp()
            elif "open instagram" in query:
                OpenApp()
            elif "open code" in query:
                OpenApp()
            elif "open sublime text" in query:
                OpenApp()
            elif "open maps" in query:
                OpenApp()
            elif "open youtube" in query:
                OpenApp()
            elif "open github" in query:
                OpenApp()
            elif "close chrome" in query:
                CloseApp()
            elif "close code" in query:
                CloseApp()
            elif "close sublime" in query:
                CloseApp()
            elif "close instagram" in query:
                CloseApp()
            elif "close github" in query:
                CloseApp()
            elif "close youtube" in query:
                CloseApp()
            elif "pause" in query:
                keyboard.press("space bar")
            elif "restart" in query:
                keyboard.press("0")
            elif "mute" in query:
                keyboard.press("m")
            elif "skip" in query:
                keyboard.press("l")
            elif "back" in query:
                keyboard.press("j")
            elif "full screen" in query:
                keyboard.press("f")
            elif "film mode" in query:
                keyboard.press("t")
            elif "pause" in query:
                keyboard.press("k")
            elif "youtube tools" in query:
                AutomateYoutube()
            elif "close this tab" in query:
                keyboard.press_and_release("ctrl + w")
            elif "open new tab" in query:
                keyboard.press_and_release("ctrl + t")
            elif "open new window" in query:
                keyboard.press_and_release("ctrl + n")
            elif "history" in query:
                keyboard.press_and_release("ctrl + h")
            elif "chrome automation" in query:
                AutomateChrome()
            elif "joke" in query:
                joke = pyjokes.get_joke()
                Speak(joke)
            elif "repeat my words" in query:
                Speak("Speak Sir!")
                repeat = TakeCommand()
                Speak(f"You said : {repeat}")
            elif "my location" in query:
                Speak("Ok sir, Wait a second!")
                browser.open(
                    "https://www.google.com/maps/@20.9425897,86.1242782,15z")
            elif "dictionary" in query:
                Dictionary()
            elif "alarm" in query:
                Speak("Enter the time!")
                time = input(": Enter the Time :")

                while True:
                    Time_AC = datetime.datetime.now()
                    now = Time_AC.strftime("%H:%M:%S")

                    if now == time:
                        Speak("Time to wake up Sir!")
                        playsound('spacealarm.mp3')
                        Speak("Alarm Closed")
                    elif now > time:
                        break
            elif "translator" in query:
                Translate()
            elif "remember that" in query:
                rememberMsg = query.replace("remember that", "")
                rememberMsg = rememberMsg.replace("jarvis", "")
                Speak(f"You told me to remind you that : {rememberMsg}")
                remember = open("data.txt", "w")
                remember.write(rememberMsg)
                remember.close()
            elif "what do you remember" in query:
                remember = open("data.txt", "r")
                Speak(f"You told me that : {remember.read()}")
            elif "google search" in query:
                import wikipedia as googleScrape
                query = query.replace("jarvis", "")
                query = query.replace("google search", "")
                query = query.replace("google", "")
                Speak("This is what I found on the Web!")
                pwk.search(query)

                try:
                    result = googleScrape.summary(query, 3)
                    Speak(result)
                except:
                    Speak("No Data Found!")
            elif "temperature" in query:
                Temp()
            elif "read book" in query:
                Reader()
            elif "downloading speed" in query:
                SpeedTest()
            elif "uploading speed" in query:
                SpeedTest()
            elif "internet speed" in query:
                SpeedTest()
            elif "how to" in query:
                Speak("Getting Data From Internet!")
                op = query.replace("jarvis", "")
                max_result = 1
                how_to_function = search_wikihow(op, max_result)
                assert len(how_to_function) == 1
                how_to_function[0].print()
                Speak(how_to_function[0].summary)
            elif "whatsapp message advanced" in query:
                query = query.replace("jarvis", "")
                query = query.replace("send", "")
                query = query.replace("whatsapp message advanced", "")
                query = query.replace("to", "")
                name = query
                if "neha" in name:
                    phNo = "XXXXXXXXXXX"
                    Speak(f"What's the message for {name}")
                    message = TakeCommand()
                    WhatsAppAdv(phNo, message)
                elif "kamakshi" in name:
                    phNo = "XXXXXXXXXXX"
                    Speak(f"What's the message for {name}")
                    message = TakeCommand()
                    WhatsAppAdv(phNo, message)
                elif "family" in name:
                    group_id = "XXXXXXXXXX"
                    Speak(f"What's the message for {name}")
                    message = TakeCommand()
                    WhatsAppAdvGroup(group_id, message)
            elif "chatbot" in query:
                Speak("Your Query Sir!")
                command = input()
                reply = chatbot.chatbot(command)
                Speak(reply)


startFunctions = MainThread()


class GUI_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_JarvisUI()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.pushButton.clicked.connect(self.startFunction)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)

    def startFunction(self):
        self.jarvis_ui.movies_label_2 = QtGui.QMovie(
            ".\\../B.G/Iron_Template_1.gif")
        self.jarvis_ui.label_2.setMovie(self.jarvis_ui.movies_label_2)
        self.jarvis_ui.movies_label_2.start()

        self.jarvis_ui.movies_label_3 = QtGui.QMovie(
            ".\\../VoiceReg/__1.gif")
        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies_label_3)
        self.jarvis_ui.movies_label_3.start()

        self.jarvis_ui.movies_label_4 = QtGui.QMovie(
            ".\\initial.gif")
        self.jarvis_ui.label_4.setMovie(self.jarvis_ui.movies_label_4)
        self.jarvis_ui.movies_label_4.start()

        self.jarvis_ui.movies_label_5 = QtGui.QMovie(
            ".\\Health_Template.gif")
        self.jarvis_ui.label_5.setMovie(self.jarvis_ui.movies_label_5)
        self.jarvis_ui.movies_label_5.start()

        self.jarvis_ui.movies_label_6 = QtGui.QMovie(
            ".\\B.G_Template_1.gif")
        self.jarvis_ui.label_6.setMovie(self.jarvis_ui.movies_label_6)
        self.jarvis_ui.movies_label_6.start()

        startFunctions.start()


Gui_App = QApplication(sys.argv)
Gui_Jarvis = GUI_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())
