import pyttsx3
import speech_recognition as sr
import webbrowser as browser
import pywhatkit as pwk
import os
import wikipedia
import pyautogui as pag
import keyboard
import pyjokes
import datetime
from playsound import playsound
from pydictionary import Dictionary as dict

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


def TaskExecution():
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
        elif "google search" in query:
            Speak("This is what I found for your Search Sir!")
            query = query.replace("google search", "")
            query = query.replace("jarvis", "")
            pwk.search(query)
            Speak("Done Sir!")
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


TaskExecution()
