import pyttsx3

#Text to speech setup
engine = pyttsx3.init()

class Speaker :
    def speak(self,text):
        engine.say(text)
        engine.runAndWait()
    def printAndSpeak(self,text):
        print(text)
        engine.say(text)
        engine.runAndWait()
        