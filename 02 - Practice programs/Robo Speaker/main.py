#pip install pyttsx3
import pyttsx3
text = pyttsx3.init()
i = "Welcome to Robo Speaker 1.1 Created by Anirudh C M"
text.say(i)
print("Welcome to Robo Speaker 1.1 Created by Anirudh C M")

while True:
    a = input("Enter the text which you want me to speak: ")
    if a == "quit":
        break
    text.say(a)
    text.runAndWait() #This will basically wait after saying the words
