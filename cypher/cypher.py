import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")  
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")  
    else:
        speak("Good Evening sir")    
    speak("I am cypher, How may i help you ")     
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")         
        r.pause_threshold = 2
        audio=r.listen(source) 
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")    
    except Exception as e:
        #print(e) 
        print("I cannot hear anything")    
        engine.runAndWait()
        return "None"       
    return query
 
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aksravanth@gmail.com','7842450894')
    server.sendmail('aksravanth@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishme()
    while(True):
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
           
        elif 'hello cypher' in query:
            speak("Hello sir,I Hope everything is going well sir...how was your day?")    
        elif 'who are you' in query:
            speak('I am cypher, An A I created by Sravanth on January 5, 2021...I was created out of his laziness inorder to do some  of his tasks...and Thanks for asking about me ')    

        elif 'open youtube' in query:
            speak('definitely sir...here you go  ')
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            speak('definitely sir...here you go  ')
            webbrowser.open("https://www.google.com/")    
        elif 'open facebook' in query:
            speak('definitely sir...here you go  ')
            webbrowser.open("https://www.facebook.com/")        
        elif 'open wynk' in query:
            speak('definitely sir...here you go  ')
            webbrowser.open("https://wynk.in/music")  

        elif 'joke' in query:
            speak(pyjokes.get_joke()) 

        elif 'history' in query:
            speak("Be careful sir....here we go.....")
            speak("hmmm....sorry sir i was not permitted to peek")
            

        elif 'play' in query:
            song=query.replace('play', '')  
            speak('playing ' + song)   
            pywhatkit.playonyt(song)
            
            
        elif 'play some music' in query:
            random_song=random.randint(0,9)
            music_dir='D:\\cypher\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random_song]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")   
        elif 'open code' in query:
            path= "D:\\cypher\\cypher.py"
            os.startfile(path)
        elif 'email to aritra' in query:
            try:
                speak("What should i say")    
                content=takeCommand()
                to="aritraghosh9599@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")    
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to send this email")    
        elif 'thank you' in query:
            speak("Any time sir")
        elif 'hello jarvis' in query:
            speak("sorry sir,i am not jarvis , my name is cypher")   
        elif 'not good' in query:
            speak("i am here to change your mood...would you like me to play some music")
            query1=takeCommand().lower()      
            if 'yes' in query1:
                speak("here you go")      
                music_dir='D:\\cypher\\music'
                songs=os.listdir(music_dir)
                #print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))   
            else:
                speak("Then take some rest  and get refreshed sir")       
        elif 'send message' in query or 'send a message' in query:
            pywhatkit.sendwhatmsg('+919494189236','Lets play valo- From cypher',15,00)

        elif 'can you do' in query:
            speak("I can help you getting any sort of information from wikipedia, i can boost your mood by playing awesome songs.....,also i can send email for you while you enjoy music........., i can open youtube....facebook and many more... on your command sir")    
        elif 'bye' in query:
            speak("bye sir, have a good day")
            sys.exit()
