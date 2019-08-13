import wikipediaapi
from speaker import Speaker

speaker = Speaker()

def isQuestion(userCommand):
    arr = ["who","when","what","where","how"]
    for element in arr : 
        if element in userCommand.lower():
            return True
    return False

class Wikipedia :
    def __init__(self,userCommand):
        self.command = userCommand
        self.keyword = ""
        self.summary = ""
    def findKeyword(self):
        arr,commandSplitted= ["is","are","was","were"],self.command.split()
        for i,element in enumerate(commandSplitted):
            if(element in arr):
                i+=1
                while(i<len(commandSplitted)):
                    self.keyword+=(commandSplitted[i]+" ")
                    i+=1
    def doesPageExist(self):
        if(self.keyword==""):
            return False
        page_py = wikipediaapi.Wikipedia('en').page(self.keyword)
        if(not page_py.exists()):
            return False
        self.summary = (page_py.summary)
        return True
    def displaySummary(self):
        speaker.printAndSpeak(self.summary)






        