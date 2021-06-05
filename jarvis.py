import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import webbrowser as wb
import os
import pyautogui
import pyjokes

engine=pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
newVoiceRate= 180
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time =datetime.datetime.now().strftime('%I:%M:%S')
    speak('And time right now is '+Time)


def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak('Todays date is')
    speak(date)
    speak(month)
    speak(year)


def wishme():
    hour= datetime.datetime.now().hour
    
    if hour>=6 and hour<12:
        a='Morning'
    elif hour>=12 and hour<18:
        a='Afternoon'
    elif hour>=18 and hour<=24:
        a='Evening'
    else:
        a='Night'

    speak('Good'+a+'mam and sir') 
    speak('hello Pramod, my name is Jaadu, i m an indian siri made by sakshi')
    speak('jaadu at your service, how can i help you?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,'en-US')
        print(query)

    except Exception as e:
        print(e)
        speak('Say that again please...')

        return 'None'

    return query

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test@gmail.com','123@abc')  
    server.sendmail('test@gmail.com', to, content) 
    server.close() 

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\Users\sakshi\Desktop\Jarvis\SS\ss.png")

def jokes():
    speak(pyjokes.get_joke())

if __name__ == '__main__':

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        
        elif "date" in query:
            date()

        elif "offline" in query:
            quit()
        
        elif "wikipedia" in query:
            speak('Searching...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences = 2)
            speak(result)

        elif "send email" in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'xyz@gmail.com'
                #sendmail(to, content)
                speak(content)
                speak('Mail was sent successfully..')

            except Exception as e:
                speak(e)
                speak('Unable to send the message')

        elif "search in chrome" in query:
            speak("What Should i search??")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand.lower()
            wb.get(chromepath).open_new_tab(search+".com")

        elif "logout" in query:
            os.system("shutdown - l")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        
        elif "restart" in query:
            os.system("shutdowwn /r /t 1")

        elif "play songs" in query:
            songs_dir = "F:\Songs"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "remember that" in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("You said to remember that"+ data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "do you remember anything " in query:
            remember = open("data.txt","r")
            speak("You told me to remember that"+ remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done")

        elif "joke" in query:
            jokes()

        







