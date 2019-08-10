import speech_recognition as sr
import pyttsx3
from pyowm import OWM
import webbrowser
import random


#Text to speech setup
engine = pyttsx3.init()

#Open Weather Map object creation
owm = OWM("328a3cfff5c381860add146bf8197513")

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def handleSpeech(userCommand):
    r = sr.Recognizer()
    with sr.Microphone() as source : 
        audio = r.listen(source)
        print("Listening....")

def findURL(userCommand):
    for i,word in enumerate(userCommand.split()):
        if(word=="open"):
            return("http://www."+userCommand.split()[i+1]+".com")
    return "URL not found"
    
    try:
        userCommand = (r.recognize_google(audio))    
    except sr.UnknownValueError:
        speak("Sorry sir, I could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return userCommand

userCommand = ""  
while(True):
    print("How may I help you, sir?")
    speak("How may I help you sir?")
    # userCommand = handleSpeech(userCommand)
    userCommand=input("Enter your command : ")
    if("bye" in userCommand.lower()):
        speak("Bye sir, see you next time")
        break
    elif(userCommand.lower()=="how are you doing"):
        speak(random.choice(["I am fine","Incredible, Sir","I am feeling great"]))
    elif("open" in userCommand.lower()):
        speak("Ok sir, wait a second")
        URL = findURL(userCommand)
        if(URL.lower()=="url not found"):
            speak(URL)
            continue
        else:
            webbrowser.open(URL,new=2)
    elif("weather" in userCommand.lower()):
        weatherData = owm.weather_at_id(2643741)
        print(weatherData.get_weather())
        
        
    

