import urllib.request

class location:
    def __init__(self,name,top,left,mainurl, jsurl):
        self.name = name
        self.top = top
        self.left = left
        self.mainurl = mainurl
        self.condition = checkWeather(jsurl)
def checkWeather(jsurl):
    Page = urllib.request.urlopen(jsurl)
    #opens the page for the indivual town
    theCondition=[]
    finalCondition = ""
    for line in Page:

        if line[:17].decode('utf-8') == "var obCondition =":
            #reads page line by line until it finds the line where condition is found
            theCondition=(line.decode('utf-8').split('\"'))
            finalCondition = theCondition[1]
            if finalCondition == "Mostly Cloudy"  or finalCondition == "Increasing cloudiness" or finalCondition =="Cloudy" or finalCondition =="Partly cloudy" :
                return "cloudy"
            elif finalCondition == "Light Rain" or finalCondition == "Light Rainshower" or finalCondition == "Periods of rain" or finalCondition =="Showers"  or finalCondition == "Chance of showers":
                return "rainy"
            elif finalCondition == "A mix of sun and cloud" or finalCondition =="Clearing" or finalCondition == "Sunny":
                return "sunny"
            else:
                return "lightning"
            #The possible weathers are not fully fleshed out with lightning as a fall back if the weather condition is not one of the options
    return "lightning"
