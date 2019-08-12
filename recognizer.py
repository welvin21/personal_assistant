import speech_recognition as sr

r = sr.Recognizer()

def handleSpeech(userCommand):
    with sr.Microphone(device_index = 0) as source :
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        audio = r.listen(source)
    try:
        userCommand = (r.recognize_google(audio))
    except sr.UnknownValueError:
        userCommand = ""
    except sr.RequestError as e:
        userCommand = ""
    return userCommand