from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Gelsenkirchen"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?' \
                   f'appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weatehr Conditions ***\n')
    city = input("\nPlease input a city name: ")
    # Check for empty strings or empty spaces
    if not bool(city.strip()):
        city = "Gelsenkirchen"

    weather_data = get_current_weather(city)
    pprint(weather_data)

