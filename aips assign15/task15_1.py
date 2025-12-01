import requests
import json

def get_weather(city_name):
    api_key = "ba12414ecc2fbdd2d22d91fe289e19f6"  # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    weather_data = response.json()
    
    print(f"\nweather data for: {city_name}")
    print(json.dumps(weather_data, indent=4))

# Get city name from user input
city_name = input("Enter the city name: ")
get_weather(city_name)

