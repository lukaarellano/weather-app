import requests
import json
from tkinter import * #type: ignore

response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Houston/?key=TDYFEERMRS7Y6F5CLGSDLET5R&include=current")

print(response.status_code)

weatherDict = response.json()
temperature = weatherDict["currentConditions"]["temp"]
datetime = weatherDict["currentConditions"]["datetime"]
conditions = weatherDict['currentConditions']['conditions']
temphigh = weatherDict['currentConditions']['tempmax']
tempmin = weatherDict['currentConditions']['tempmin']

def update_weather():
    with open("weather-app/data/data.json", "r+") as json_file:
        data = json.load(json_file)
        data["temperature"] = temperature
        data["datetime"] = datetime
        data["conditions"] = conditions
        data["temphigh"] = temphigh
        data["tempmin"] = tempmin
        
        json_file.seek(0, 0)
        json.dump(data, json_file)
        json_file.truncate()
        
        update_status()

display = Tk()

display.title("Weather App 🌧️")
display.geometry("500x150")

status_text = f"""
Date: {datetime}
Temperature: {temperature}
Conditions: {conditions}
Highest Temperature: {temphigh}
Lowest Temperature: {tempmin}
"""
status = Label(display, text=status_text)
status.pack()

update_stats = Button(display, text='Update Weather', command=update_weather)
update_stats.pack()

def update_status():
    status.config(text=status_text)
    print(status_text)

display.mainloop()