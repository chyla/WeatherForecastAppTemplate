# feel free to modify any part of this file

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import urllib.request
from PIL import Image, ImageTk


def download_web_as_string(url):
    url = url.replace(" ", "%20")
    print("Downloading web page:", url)
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8", "ignore")


class WeatherCondition():
    STORM = 0
    DRIZZLE = 1
    RAIN = 2
    SNOW = 3
    CLOUDS = 4
    SUN = 5
    OTHER = 6


class WeatherInformation():

    def __init__(self, conditions, temperature):
        self.conditions = conditions
        self.temperature = temperature


class ForecastFrame(tk.Frame):

    def __init__(self, weather_icons):
        super().__init__()

        self._weather_icons = weather_icons

        self.master.title("Prognoza pogody ☀")
        self.pack(fill=tk.BOTH, expand=True)

        self.city_selector = ttk.Combobox(self)
        self.city_selector['values'] = ["Wroclaw", "Gdansk"]
        self.city_selector.bind("<<ComboboxSelected>>", self.__on_city_selected)
        self.city_selector.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        self.weather_forecast = tk.Label(self)
        self.weather_forecast.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.weather_temperature = tk.Label(self)
        self.weather_temperature.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    def __on_city_selected(self, *args):
        selected_city_idx = self.city_selector.current()
        selected_city_name = self.city_selector.get()
        print("Selected city:", selected_city_idx, selected_city_name)
        if selected_city_idx < 0:
            raise ValueError("Unknown city.")

        # your code goes here
        weather = WeatherInformation(WeatherCondition.OTHER, 0)
        # your code goes here

        print("Weather conditions:", weather.conditions)
        print("Weather temperature:", weather.temperature)

        self.__show_weather_temperature(weather.temperature)
        self.__show_weather_forecast_image(weather.conditions)

    def __show_weather_temperature(self, temperature):
        self.weather_temperature['text'] = "{}℃".format(temperature)

    def __show_weather_forecast_image(self, weather_conditions):
        image_file_name = "images/" + self._weather_icons[weather_conditions]
        self._image_load = Image.open(image_file_name)
        self._image_render = ImageTk.PhotoImage(self._image_load)

        self.weather_forecast['image'] = self._image_render


weather_icons_theme = {
    WeatherCondition.STORM : "stormyWeather.png",
    WeatherCondition.DRIZZLE : "sunnyRainyWeather.png",
    WeatherCondition.RAIN : "rainyWeather.png",
    WeatherCondition.SNOW : "snowyWeather.png",
    WeatherCondition.CLOUDS : "cloudyWeather.png",
    WeatherCondition.SUN : "sunnyWeather.png",
    WeatherCondition.OTHER : "stormyWeather.png",
}


root = tk.Tk()

frame = ForecastFrame(weather_icons_theme)
root.resizable(True, True)
root.minsize(400, 250)
root.mainloop()

