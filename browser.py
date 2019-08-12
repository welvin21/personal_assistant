import webbrowser
from speaker import Speaker

speaker3 = Speaker()
class Browser :
    def __init__(self):
        self.URL = ""   
    def open(self,userCommand):
        for i,word in enumerate(userCommand.split()):
            if(word=="open"):
                self.URL = ("http://www."+userCommand.split()[i+1]+".com")
        if(self.URL==""):
            speaker3.printAndSpeak("Sorry sir, couldn't find URL")
            return
        else:
            speaker3.printAndSpeak("Ok sir, opening " + self.URL +", wait a second")
            webbrowser.open(self.URL,new=2)

