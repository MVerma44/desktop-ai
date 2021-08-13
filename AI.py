import pyttsx3
import datetime
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voice = engine.getProperty("voices")
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 

wish_morning = ["Rise and shine!", "Top of the morning to you!", "Goos day to you", "Have a great day", "Wishing you the best for the day ahead", "How are you this fine morning?",
                "Isn't it a beatuiful day today?", "Look alive!", "What a pleasant morning we are doing", "Morning!", "Good morning", "Good day"]

wish_afternoon = ["Have a good afternoon and a great day!", "You are as bright as the afternoon sun", "Have an awesome afternoon! thank you for sharing a piece of your heart", "Wishing you a splendid afternoon my one and only!",
                  "This afternoon is a beauty, just like you", "Half of the day is over; have a marvelous afternoon and enjoy the rest of the day!", "i Would like to wish you a good afternoon and an even better evening",
                  "Today, there will be a beautiful sunset after you have a good afternoon!"]

wish_evening = ["Have a nice evening", "Good evening", "Good evening Mayank", "Evening boss", "I hope you are having a refreshing evening as i am having here thinking of you"]

wish_night = ["It was nice to meet you, goodnight!", "Goodnight! see you tomorrow", "It was good to meet you", "I'll catch up with you later", "I'll will see you seen", "Ta-Ta for now"]

def wish_me():
    hour = int(datetime.datetime.now().hour)

    if hour>=5 and hour<12:
        speak(random.choice(wish_morning))

    elif hour>=12 and hour<18:
        speak(random.choice(wish_afternoon))

    elif hour>=18 and hour<24:
        speak(random.choice(wish_evening))
    
    else:
        speak("Sir, it's too late, it's time to sleep")

    #speak("Here side Trixy, your personal AI. What can i do for you")


def take_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = .8
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en")
        print(f"You said: {query}")

    except Exception as e:
        print("Please pardon...")
        return "None"
    
    return query

if __name__ == "__main__":

    wish_me()
    wiki = ["wikipedia", "tell me something about", "what do you know about",  "info"]
    while True:
        query = take_command().lower()

 
        if "wikipedia" in query:
            speak("Searching in wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(f"According to wikipedia {results}")
              
        elif "open youtube" in query:
            result = webbrowser.open("youtube.com")

        elif "open google" in query:
            result = webbrowser.open("google.com")

        elif "play music" in query:
            music = "E:\\Music"  
            song = os.listdir(music)
            os.startfile(os.path.join(music, random.choice(song)))   
     
        elif "time" in query:
            t = datetime.datetime.now().strftime("%I:%M:%S")
            speak(t)

        elif "open vs code" in query:
            path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        
        elif "open python" in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
            os.startfile(path)
        
        elif "open discord" in query:
            path = "C:\\Users\\HP\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
            os.startfile(path)

        elif "quit" in query:
            quit()


    














