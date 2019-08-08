import speech_recognition as sr
import pyttsx3

#Text to speech setup
engine = pyttsx3.init()

r = sr.Recognizer()
with sr.Microphone() as source : 
    print("How may I help you?")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # print(r.recognize_google(audio))
    engine.say(r.recognize_google(audio))
    engine.runAndWait()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
