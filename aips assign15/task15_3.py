import requests
import json

API_KEY = "ba12414ecc2fbdd2d22d91fe289e19f6"  # Replace with your actual API key

def get_weather_formatted(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        # Extract specific fields from the API response
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        
        # Display in user-friendly format
        print(f"\nCity: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.capitalize()}")
        
        return data
    except requests.exceptions.Timeout:
        print("Error: API request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your internet.")
    except requests.exceptions.HTTPError:
        print("Error: Invalid city or API key.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    return None

# Get city name from user input
city_name = input("Enter the city name: ")
get_weather_formatted(city_name)

