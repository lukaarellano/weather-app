# Weather App 🌧️

A Python-based script which uses Visual Crossing's weather API to get basic weather details from any City.

## Technlogies 🕹️

`Python`

## Features ✨

* Users can input any city by name in the location entry.
* The display will show an overview of that cities weather, such as it's current conditions, time, and temperature.
* To update the weather after a certain amount of time, simply click the "Update Weather" button.

## The Process 🗺️

The idea of a weather app came from many different sources, but I ultimately decided to do it so I could learn how to interact with APIs. It started with me learning how to read the huge JSON response that the API gives me. After learning how to navigate it, I could then pick and choose simple weather details which would originally be printed in the terminal. Later, I would make a GUI using Tkinter so that users wouldn't need to use the terminal.

## How to Run the Project 💻

1. Clone the repository.
2. Create a folder named "data" in the same directory as the weather-app directory. Then inside of it, create a JSON file named "data.json" and type in or copy + paste this:
   * "{"temperature": 0.0, "date": "2026-1-1", "conditions": "None", "temphigh": 0.0, "tempmin": 0.0, "datetime": "2026-1-1", "time": "00:00:00", "location": "Cupertino"}"
3. Run "`python3 main.py` on MacOS or `python main.py` in the terminal.
4. Interact with the GUI by typing in any city in the location entry, then pressing Update Weather.
   * Also press "Update Weather" if you want to see the most recent changes to that city's weather.
