import pyttsx3
import speech_recognition as sr

assistant = pyttsx3.init("sapi5")
voices = assistant.getProperty("voices")
print(voices)
assistant.setProperty("voices", voices[0].id)


def Speak(audio):
    print("   ")
    assistant.say(audio)
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
