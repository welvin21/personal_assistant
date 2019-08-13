import random
from recognizer import handleSpeech
from weather import getLocation,getWeatherData,displayWeather
from speaker import Speaker
from browser import Browser
from wikipedia import isQuestion,Wikipedia

browser1 = Browser()
speaker1 = Speaker()
userCommand = ""
while(True):
    speaker1.printAndSpeak("How may I help you, sir?")
    # userCommand = handleSpeech(userCommand)
    userCommand=input("Enter your command : ")
    print("Your command :", userCommand)
    if("bye" in userCommand.lower()):
        speaker1.speak("Bye sir, see you next time")
        break
    elif(userCommand==""):
        speaker1.printAndSpeak("Sorry sir, couldn't understand audio")
    elif(userCommand.lower()=="how are you doing"):
        speaker1.speak(random.choice(["I am fine","Incredible, Sir","I am feeling great"]))
    elif("open" in userCommand.lower()):
        browser1.open(userCommand)
    elif("weather" in userCommand.lower()):
        displayWeather(userCommand)
    elif(isQuestion(userCommand)):
        wiki = Wikipedia(userCommand)
        wiki.findKeyword()
        if(wiki.doesPageExist()):
            wiki.displaySummary()
        else:
            speaker1.printAndSpeak("Sorry sir, couldn't get information ")


     
    