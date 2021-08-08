#project 1
# Iron man jarvis AI Desktop voice assitant
# it automate tasks


import pyttsx3#pip install pyttsx3
import datetime
import speech_recognition as sr #for speech to string translation(pip install speechRecognition)
import wikipedia#used to search wikipedia(pip install wikipedia)
import webbrowser#used to open webbrowser
import os 
import random




engine = pyttsx3.init("sapi5")  # this is used to get voices in window
# it takes voices which are in your computer
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)  # it set the voice
rate = 150#used to slow down the speed of speaking of program
engine.setProperty("rate",rate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(("Good morning "))
    elif hour >= 12 and hour < 18:
        speak(("good afternoon "))
    else:
        speak(("good evening "))


def takeCommand():
    # it take microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:#for this you have to install pipwin
        #and then "pipwin install pyaudio"
        print("Listening...")
        r.pause_threshold = 1  # it help to not complete it if user stop speaking
        # you can also control voice energy level by r.dynamic energy threshold
        audio =r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        print(e,"please say again")
        return "None"
    return query





if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
       

        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        #login to open youtube
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        
        elif "play music" in query:
            music_dir = "D:\\songs"#give the music directory here
            songs = os.listdir(music_dir)
            song_no = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[song_no]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif "exit" or "stop" in query:
            exit()

        
