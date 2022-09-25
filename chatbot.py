import random

command_1 = [
    "hello", "hi", "wake", "there", "hey", "help"
]
reply_1 = [
    "Hello Sir, Welcome Back!", "Always There for you Sir!", "How can I help you?",
    "Welcome Back Sir, How can I help you?", "Hi sir, Is there anything I can do for you?"
]

command_2 = [
    "bye", "sleep", "go"
]
reply_2 = [
    "Bye Sir", "Bye Sir, Hope to see you soon!", "Bye Sir, Say Wake Up Jarvis if you want me to start again!"
]


def chatbot(Text):
    for word in Text.split():
        if word in command_1:
            return random.choice(reply_1)
        elif word in command_2:
            return random.choice(reply_2)
