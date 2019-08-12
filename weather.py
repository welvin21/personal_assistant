import pycountry
import geonamescache
import requests
from speaker import Speaker


class Weather : 
    def __init__ (self,weatherData):
        self.main = weatherData["main"]
        self.weather = weatherData["weather"][0]
        self.wind = weatherData["wind"]
        self.location = weatherData["name"]
    def getTemperature(self):
        return str(self.main["temp"])
    def getPressure(self):
        return str(self.main["pressure"])
    def getHumidity(self):
        return str(self.main["humidity"])
    def getDesc(self):
        return self.weather["description"]
    def getWindSpeed(self):
        return str(self.wind["speed"])
    def getPlace(self):
        return self.location
speaker2 = Speaker()

def convert(temperature):
    temperature = str(temperature).split('.')[0] + " point " + str(temperature).split('.')[1]
    return temperature

def getLocation(userCommand):
    for country in pycountry.countries :
        if (country.name.lower() in userCommand) or (country.name.capitalize() in userCommand) :
            return country.name
    cities = geonamescache.GeonamesCache().get_cities()
    for key in cities :
        if (cities[key]['name'].lower() in userCommand.split()) or (cities[key]['name'].capitalize() in userCommand.split()):
            return cities[key]['name'].capitalize()
    return ""
def getWeatherData(userCommand):
    location = getLocation(userCommand)
    url =  f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID=328a3cfff5c381860add146bf8197513"
    response = requests.get(url)
    if(response.status_code!=200):
        return "Sorry sir, location not found"
    return response.json()

def displayWeather(userCommand):
    weatherData = getWeatherData(userCommand)
    if(type(weatherData)==str):
        speaker2.printAndSpeak(weatherData)
        return
    # for key in weatherData:
    #     print(key,weatherData[key])
    weatherData = Weather(weatherData)
    speaker2.printAndSpeak("Showing the weather report in "+weatherData.getPlace()+"\n")
    speaker2.printAndSpeak("Humidity : "+weatherData.getHumidity()+" %")
    print("Temperature : "+str(weatherData.getTemperature())+" degree celsius")
    speaker2.speak("Temperature : "+convert(weatherData.getTemperature())+" degree celsius\n")
    speaker2.printAndSpeak("Pressure : "+weatherData.getPressure()+" hectopascal")
    speaker2.printAndSpeak("Wind speed : "+weatherData.getWindSpeed()+ " meter per second")
    speaker2.printAndSpeak("Status : "+weatherData.getDesc())
