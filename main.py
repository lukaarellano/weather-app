import requests
import json

response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Houston/?key=TDYFEERMRS7Y6F5CLGSDLET5R&include=current")

print(response.status_code)

weatherDict = response.json()
temperature = weatherDict["currentConditions"]["temp"]
datetime = weatherDict["days"][0]["datetime"]
conditions = weatherDict['days'][0]['conditions']
temphigh = weatherDict['days'][0]['tempmax']
tempmin = weatherDict['days'][0]['tempmin']

with open("data.json", "r+") as json_file:
    data = json.load(json_file)
    data["temperature"] = temperature
    data["datetime"] = datetime
    data["conditions"] = conditions
    data["temphigh"] = temphigh
    data["tempmin"] = tempmin
    
    json_file.seek(0, 0)
    json.dump(data, json_file)
    json_file.truncate()