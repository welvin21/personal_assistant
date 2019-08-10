import speech_recognition as sr
import pyttsx3
from pyowm import OWM
import pycountry
import geonamescache
import webbrowser
import random

# try:
#     userCommand = (r.recognize_google(audio))
# except sr.UnknownValueError:
#     speak("Sorry sir, I could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))
# return userCommand

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
    return None


def findLocation(userCommand):
    for country in pycountry.countries :
        if country.name.lower() in userCommand :
            return country.name
    cities = geonamescache.GeonamesCache().get_cities()
    for key in cities :
        if cities[key]['name'].lower() in userCommand.split():
            return cities[key]['name'].capitalize()
    return None

def printAndSpeak(input):
    print(input)
    speak(input)

def displayWeather(weatherData):
    printAndSpeak("Humidity : "+str(weatherData.get_humidity())+"%\n")
    #convert floating point number to speakable string
    printAndSpeak("Temperature : "+str(weatherData.get_temperature(unit="celsius")["temp"])+"degree celsius\n")
    printAndSpeak("Status : "+weatherData.get_detailed_status())


userCommand = ""
while(True):
    printAndSpeak("How may I help you, sir?")
    # userCommand = handleSpeech(userCommand)
    userCommand=input("Enter your command : ")
    if("bye" in userCommand.lower()):
        speak("Bye sir, see you next time")
        break
    elif(userCommand.lower()=="how are you doing"):
        speak(random.choice(["I am fine","Incredible, Sir","I am feeling great"]))
    elif("open" in userCommand.lower()):
        URL = findURL(userCommand)
        if(URL==None):
            speak("Sorry sir, couldn't find URL")
            continue
        else:
            speak("Ok sir, opening " + URL +", wait a second")
            webbrowser.open(URL,new=2)
    elif("weather" in userCommand.lower()):
        location = findLocation(userCommand.lower())
        if(location==None):
            speak("Sorry sir, I could not find the location you entered")
        else:
            printAndSpeak("Showing the weather report of "+location)
            weatherData = owm.weather_at_place(location).get_weather()
            displayWeather(weatherData)
