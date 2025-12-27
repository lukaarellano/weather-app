import requests

response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Houston/?key=TDYFEERMRS7Y6F5CLGSDLET5R&include=current")

print(response.status_code)
weatherDict = response.json()
temperature = weatherDict["currentConditions"]["temp"]
precipitation = weatherDict["currentConditions"]["precip"]
print("The temperature is " + str(temperature) + " degrees farenheight.")
print("The percipitation is " + str(precipitation) + "inches.")