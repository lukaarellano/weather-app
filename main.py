import requests
import json
from tkinter import * #type: ignore

display = Tk()

display.title("Weather App 🌧️")
display.geometry("500x250")

def update_weather():
    def update_status():
        status.config(text=status_text)
    def update_location():
        global response
        global location_var
        global weatherDict
        location_var.set(location_var.get())
        print(location_var.get())
        response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location_var.get()}/?key=TDYFEERMRS7Y6F5CLGSDLET5R&include=current")
        weatherDict = response.json()
    with open("data/data.json", "r+") as json_file:
        update_location()
        data = json.load(json_file)
        data['location'] = location_var.get()
        data["temperature"] = temperature
        data["datetime"] = datetime
        data['time'] = time
        data["conditions"] = conditions
        data["temphigh"] = temphigh
        data["tempmin"] = tempmin

        json_file.seek(0, 0)
        json.dump(data, json_file)
        json_file.truncate()
        
        update_status()

location_var = StringVar()
location_var.set("Houston")
location_label = Label(display, text='Location:')
location_entry = Entry(display, textvariable=location_var)

response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location_var.get()}/?key=TDYFEERMRS7Y6F5CLGSDLET5R&include=current")

print(response.status_code)

weatherDict = response.json()
temperature = weatherDict['currentConditions']["temp"]
datetime = weatherDict['days'][0]["datetime"]
time = weatherDict['currentConditions']['datetime']
conditions = weatherDict['days'][0]['conditions']
temphigh = weatherDict['days'][0]['tempmax']
tempmin = weatherDict['days'][0]['tempmin']

status_text = f"""
Location: {location_var.get()}
Date: {datetime}
Time: {time}
Temperature: {temperature}
Conditions: {conditions}
Highest Temperature: {temphigh}
Lowest Temperature: {tempmin}"""
status = Label(display, text=status_text)
status.pack()

location_label.pack()
location_entry.pack()

update_stats = Button(display, text='Update Weather', command=update_weather)
update_stats.pack()

display.mainloop()