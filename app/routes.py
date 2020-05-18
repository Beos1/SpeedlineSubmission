from app import app
from flask import render_template
from .location import location
@app.route('/')
def test():
    locationList=[]
    Words = []
    tempWord = ""
    while True:
        file = open("app/static/data/locations.txt", "r")
        #reads a text file containing information about the diffrent locations
        for line in file:
            for char in line:
                if char != "|" and char !="\n":
                    tempWord = tempWord + char
                else:
                    Words.append(tempWord)
                    tempWord = ""
        Words.append(tempWord)
        wordCount = 0
        word1, word2 , word3, word4= "", "", "", ""
        for word in Words:
            if wordCount == 0:
                wordCount = wordCount + 1
                word1 = word
            elif wordCount == 1:
                wordCount = wordCount + 1
                word2= word
            elif wordCount == 2:
                wordCount = wordCount + 1
                word3= word
            elif wordCount == 3:
                wordCount = wordCount + 1
                word4 = word
            elif wordCount == 4:
                wordCount = 0
                locationList.append(location(word1, word2, word3, word4, word))

        #reads file adding all locations into a list 
        #the list stores the name or the location as well as the latitude and longitude
        file.close()
        # renders a html page dynamicly creating a link for each location with represented by an icon based on the weather in the location
        return render_template('index.html', title='Home', locations=locationList) 
