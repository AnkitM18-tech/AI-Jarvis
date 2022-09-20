import os
import speech_recognition as sr


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


while True:
    wake_up = TakeCommand()

    if "wake up" in wake_up:
        os.startfile("D:\\GitHub\\AI-Jarvis\\jarvis.py")
    else:
        print("Nothing...")
