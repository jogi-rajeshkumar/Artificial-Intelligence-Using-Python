from calendar import month
from email import message
from random import random
from re import search
import pyttsx3 #pip install pyttsx3 == text data into speech using python
import datetime
import pyaudio
import speech_recognition as sr #pip install SpeechRecognition == speech from mic to text
import pyautogui   #pip install pyautogui 
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
import string
import random
import psutil
from nltk.tokenize import *

engine = pyttsx3.init()

def speak(audio):
    engine.say (audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
#    print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("hello this is jarvis")

    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("hello this is Friday")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S") #hour = I minutes = M seconds = S
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("good morning sir")
    elif hour >=12 and hour <18:
        speak("good afternoon sir")
    elif hour >=18 and hour < 24:
        speak ("good evening sir")
    else:
        speak("good Night sir")
def wishme():
    speak("welcome back sir!")
    time()
    date()
    greeting()
    speak("jarvis at your service, please tell me how can i help you")
#while True:
#    voice = int(input("Press 1 for male voice\nPress 2 for female voice\n"))
#    speak(audio)
#    getvoices(voice)
#wishme()

def takeCommandCMD():
    query = input("please tell me how can i help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-IN") #from cloud.google.com/speech-to-text/docs/languges select the language code 
        print(query)
    except Exception as e:
        print(e)
        speak("say that again please...")
        return "None"
    return query

def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(20)
    pyautogui.press('enter')

def searchgoogle():
    speak(' what should i search for?')
    search = takeCommandMic()
    wb.open('http://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key='3e2a41485f6b4b75a7f1f7e672ddefa3')
    speak('what topic you need the news about?')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,
                                    language='en',
                                    page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

#def covid():
#    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
#
#    data = r.json()
#    covid_data = f'confirm cases : {data["cases"]} \n Deaths :{data["deaths"]} \n Recovered :{data["recovered"]}'  
#    print(covid_data)
#    speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\rajes\\Desktop\\Project\\AI\\screenshots\\{name_img}.png'                                            
    img = pyautogui.screenshot(name_img)
    img.show() 

def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 10
    s =[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("okay sir, flipping a coin")
    coin = ['heads','tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("i flipped the coin and you got"+toss)

def roll():
    speak('okay sir, rolling a die for you')
    die = ['1','2','3','4','5','6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("i rolled a die for you and you got"+roll)

def cpu():
    usuage = str(psutil.cpu_percent())
    speak('CPU is at'+ usuage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


#https://api.openweathermap.org/data/2.5/weather?q=vijayawada&units-imperial&appid=171d6f6ee89d70ce7299596ed4da3a42
#https://coronavirus-19-api.herokuapp.com/tabs/tab1

if __name__=="__main__":
    getvoices(1)
    wishme()

    while True:
        query = takeCommandMic().lower()


        if 'time' in query:
            time()     

        elif 'date' in query:
            date()
    
        elif 'message' in query:
            user_name = {
                'home': '+91 88974 54949'
            }
            try:
                speak("To whom you want to send the whats app message?")
                name = takeCommandMic()
                phone_no = user_name[name]
                speak("what is the message?")
                message = takeCommandMic()
                sendwhatsmsg(phone_no,message)
                speak("message has been send")
            except Exception as e:
                print(e)
                speak("unable to send message")

        elif 'wikipedia' in query:
            speak('searching on wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
            
        elif 'search' in query:
            searchgoogle()

        elif 'youtube' in query:
            speak('what should i search for on youtube?')
            topic = takeCommandMic()
            pywhatkit.playonyt(topic)

        elif 'weather' in query:
            city = 'vijayawada'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units-imperial&appid=8bd6e55cf83885ade305620f6459c4ca'

            res = requests.get(url)
            data = res.json()
                    
            weather = data['weather'] [0] ['main']
            temp = data['main']['temp']
            desp = data['weather'][0]['description']
            temp = round(temp - 273.15)
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} city is like')
            speak('Temperature : {} degree celcius'.format(temp))
            speak('climate is {}'.format(desp))

        elif'news' in query:
            news()

        elif 'read' in query:
            text2speech()

        #elif 'covid' in query:
    #        covid()

        #elif 'open' in query:
        # os.system('explorer C://{}'.format(query.replace('Open ',' ')))

        elif 'open code' in query:
            codepath = 'C:\\Users\\rajes\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)
            
        elif 'open download' in query:
            downloadpath = 'C:\\Users\\rajes\\Downloads'
            os.startfile(downloadpath)

        elif 'joke' in query:
            speak(pyjokes.get_jokes())

        elif 'screenshot' in query:
            screenshot()

        elif 'remember' in query:
            speak("what should i remember?")
            data = takeCommandMic()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you told me to remember that "+remember.read())
            
        elif 'password' in query: 
            passwordgen()

        elif 'flip' in query:
            flip()

        elif 'roll' in query:
            roll()

        elif 'cpu' in query:
            cpu()

        elif 'offline' in query:
            quit()