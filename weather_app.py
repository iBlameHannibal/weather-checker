import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # You can adjust units as needed

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def update_weather():
    city = entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city.")
        return

    api_key = 'YOUR_API_KEY'  # Replace with your API key

    weather_data = get_weather(api_key, city)

    if weather_data:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        result_label.config(text=f'Temperature: {temperature}°C\nDescription: {description}')
    else:
        result_label.config(text='Error fetching weather data.')

# GUI setup
app = tk.Tk()
app.title("World Weather App")

# Design
tk.Label(app, text="Enter city:").pack(pady=10)

entry = tk.Entry(app, width=30)
entry.pack(pady=10)

tk.Button(app, text="Get Weather", command=update_weather).pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Run the GUI
app.mainloop()
