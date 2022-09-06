import pyttsx3
import speech_recognition as sr
import webbrowser as browser
import pywhatkit as pwk

assistant = pyttsx3.init("sapi5")
voices = assistant.getProperty("voices")
# print(voices)
assistant.setProperty("voices", voices[0].id)
assistant.setProperty("rate", 170)


def Speak(audio):
    print("   ")
    assistant.say(audio)
    print(f": {audio}")
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


# TaskExecution()
# Speak("Hello Sir, I am Jarvis")
