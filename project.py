import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER = "Sir"
print("Initializing Assistant")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
speak("Initializing Assistant")



def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER + ", how may I help you?")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER + ", how may I help you?")
        
    else:
        speak("Good Evening" + MASTER + ", how may I help you?")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("Uh-Oh, say that again please...")
        speak("Uh-Oh, say that again please...")
        query = None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your passwd')
    server.sendmail('reciever email id', to, content)
    server.close()

def main():
    wishMe()
    speak("I am your virtual assistant and will be happy to help!")
    query = takeCommand()

    #Logic for executing tasks
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results) 

    elif 'open youtube' in query.lower():
        url = "youtube.com"
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        url = "google.com"
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open Facebook' in query.lower():
        url = "facebook.com"
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open live' in query.lower():
        url = "lpulive.lpu.in"
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open university management system' in query.lower():
        url = "ums.lpu.in"
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        songs_dir = "D:\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Sir, the time is" + strTime)

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\DELL\\Desktop\\project.py"
        os.startfile(codePath)
    
    elif 'open notepad' in query.lower():
        notePath = "C:\\Users\\DELL\\Desktop\\project.txt"
        os.startfile(notePath)
    
    elif 'tell me a joke' in query.lower():
        speak("A user interface is like a joke; if you have to explain it, then it's not that good!")

    elif 'open github' in query.lower():
        url = "github.com"
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'send mail' in query.lower():
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "reciever's mail id"
            sendEmail(to, content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry" + MASTER + "I was unable to send the email")
    
main()
