import matplotlib.pyplot as pt
import pyttsx3
import datetime
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser
import os
import random
import pyautogui
from time import sleep
from pynput.keyboard import Key, Controller
import requests
import wolframalpha
import json
import PyPDF2
import pywhatkit
from bs4 import BeautifulSoup
from time import sleep
from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition
import os
from pydictionary import Dictionary as dictn
from playsound import playsound
import time
import os
from datetime import timedelta
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


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


# query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate", 200)


def speak(audio):
    print("   ")
    engine.say(audio)
    print(f": {audio}")
    print("   ")
    engine.runAndWait()


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


keyboard = Controller()


def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)


def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
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
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

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
    text_to_translate = translator.translate(query, src="auto", dest=b,)
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
    musicName = takeCommand()

    if "off" in musicName:
        os.startfile("D:\\GitHub\\AI-Jarvis\\Off My Face.mp3")
    else:
        pywhatkit.playonyt(musicName)
        speak("Your Song Has Been Started!, Enjoy Sir!")


def Dictionary():
    speak("Opened Dictionary")
    speak("Tell me the word!")
    word = takeCommand()

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
    name = takeCommand()
    if "manager" in name:
        os.startfile("D:\\GitHub\\AI-Jarvis\\The One Minute Manager.pdf")
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
