import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random
from twilio.rest import Client
import Searches

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    outline = ['nice to see you again','welcome back you to here','i am happy to see you again']
    if hour>=0 and hour<12:
        speak("hello sir, Good Morning!")
        speak(random.choices(outline))

    elif hour>=12 and hour<18:
        speak("hello sir, Good Afternoon! ")   
        speak(random.choices(outline))

    else:
        speak("hello sir, Good Evening!")  
        speak(random.choices(outline))
    try:
        speech = ['where you wanna go','how may i help you','what is todays programme',]
        speak(random.choices(speech))

    except:
        pass 
   

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:
       # print(a)
        print('\nsay again plz...\n\n')    
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
     if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching for Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'your name' in query:

            namecmd = ['my full name is ananya, but you can call me anny','did you forgot me? i am anny']

            speak(random.choices(namecmd))

        elif 'made you' in  query:
            speak('i am created by rahul kumar, his age is 19 and i were coded in visual studio ')


        elif 'open youtube' in query:
            try:
                speak('what you want to search')
                ytcontent = takeCommand()
                url = 'https://www.youtube.com/results?search_query=' +(str(ytcontent))
                speak('opening youtube...')
                webbrowser.open_new_tab(url)

            except:
                speak('sorry i cannot search')

        elif 'open google' in query:
            try:
                speak('What you want to search?')
                content = takeCommand()
                url = "https://www.google.co.in/search?q=" +(str(content))+ "&oq="+(str(content))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
                speak('opening google...')
                webbrowser.open_new_tab(url)
            
            except:
                speak('sorry i can not search')

        elif 'open stackoverflow' in query:
            speak('opening stackoverflow...')
            webbrowser.open("www.stackoverflow.com")   


        elif 'play a song' in query:
            music_dir ='C:\\Users\\rahul\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)   
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open dev cpp' in query:
            dev_dir ='C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe'
            speak('opening dev cpp...')
            os.startfile(dev_dir)

        elif 'open game creator' in query:
            gc_dir ='C:\\Users\\rahul\\Desktop\\UE4'
            gc_path = os.listdir(gc_dir)
            speak('opening game creator ...')
            os.startfile(os.path.join(gc_dir,gc_path[1]))
            
        elif 'open a game' in query:
            saints_dir ='C:\\steam\\Saints Row 3\\SaintsRowTheThird_DX11.exe'
            speak('opening the game...')
            os.startfile(saints_dir) 

        elif 'open discord' in query:
            discord_dir ='C:\\Users\\rahul\\AppData\\Local\\Discord\\Update.exe'
            speak('opening discord...')
            os.startfile(discord_dir)  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('opening visual studio...')
            os.startfile(codePath)

        elif 'open android studio' in query:
            asPath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            speak('opening android studio...')
            os.startfile(asPath)

        elif 'shutdown my pc' in query:
            shut_down_path = 'C:\\Users\\shutdown.bat'
            speak('turning off your pc...')
            os.startfile(shut_down_path)

        elif 'create a file' in query:
            try:
                speak('please tell me a file name')
                filename = takeCommand()
                f = open(filename+'.txt',"w+")
                speak('successfully created a new text file')
                f.close()

            except:
                print('something went wrong...')
