import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os
from googlesearch import search



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)   
    engine.runAndWait()
    
speak("Quick and easy voice solutions, by quick")

def command():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            
            print("Quick is listening...")
            audio=r.listen(source)
            try:    
                query = r.recognize_google(audio)
                print(f"Tester:{query}")
                
                return query
                break
            except:
                print("Try Again")

while True:
    query = command().lower() ## takes user command 
    
    if 'name' in query:
        speak("Aloha! My name is Quick!")
    elif 'are you single' in query:
        speak('I am in a relationship with your mom')
    elif 'hate' in query:
        speak("I hate your wifi speed.")
    elif 'love' in query:
        speak("I love commiting war crimes.")
    ### time
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("It's {time} also know as doomsday.")
    
    elif 'what is your birthday' in query:
        speak("I was birthed out of ashmit's sphaggeti code on 17th of august 2022.")
        
    
    
    ### celebrity
    elif 'who is' in query:
        query = query.replace('who is',"")
        speak(wikipedia.summary(query,2))
    elif 'who was' in query:
        query = query.replace('who was',"")
        speak(wikipedia.summary(query,2))
    elif 'what is' in query:
        query = query.replace('what is',"")
        speak(wikipedia.summary(query,2))
    elif 'what was' in query:
        query = query.replace('what was',"")
        speak(wikipedia.summary(query,2))
    elif 'how much' in query:
        query = query.replace('how much',"")
        speak(wikipedia.summary(query,2))
    elif 'how many' in query:
        query = query.replace('how many',"")
        speak(wikipedia.summary(query,2))
    elif 'when was' in query:
        query = query.replace('when was',"")
        speak(wikipedia.summary(query,2))
    elif 'what was' in query:
        query = query.replace('when is',"")
        speak(wikipedia.summary(query,2))
    elif 'why is' in query:
        query = query.replace('why is',"")
        speak(wikipedia.summary(query,2))
    elif 'why was' in query:
        query = query.replace('why was',"")
        speak(wikipedia.summary(query,2))
    elif 'google' in query:
        query = query.replace('why was',"")
        speak(wikipedia.summary(query,2))
    

    
    
    ### Joke
    elif 'joke' in query:
        speak(pyjokes.get_joke())
    
    ### news
    elif 'news' in query:
            def trndnews(): 
                url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
                page = requests.get(url).json() 
                article = page["articles"] 
                results = [] 
                for ar in article: 
                    results.append(ar["title"]) 
                for i in range(len(results)): 
                    print(i + 1, results[i]) 
                speak("News.")
                speak("Do yo want me to read?")
                reply = command().lower()
                reply = str(reply)
                if reply == "yes":
                    speak(results)
                else:
                    speak('Aight mate...')
                    pass
            trndnews() 


    ### music
    elif 'music' in query:
        music_dir = 'E:\\music'
        songs = os.listdir(music_dir)
        song = random.randint(0,len(songs)-1)
        print(songs[song])  
        speak(f"playing{songs[song]}")
        os.startfile(os.path.join(music_dir, songs[0]))

    elif "bye" in query:
        speak("Famous last words.")
        break
    else:
        speak("I don't understand what you are saying. Background noise may be causing this.")