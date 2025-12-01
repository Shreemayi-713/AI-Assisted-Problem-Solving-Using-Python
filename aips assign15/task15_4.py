import requests
import json

API_KEY = "ba12414ecc2fbdd2d22d91fe289e19f6"  # Replace with your actual API key

def get_weather_details(city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=5)
        
        # Check if city is not found (404 status code)
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return None
        
        response.raise_for_status()
        data = response.json()
        # Extract specific fields from the API response
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        
        # Display in user-friendly format
        print(f"\nCity: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.capitalize()}")
        
        return data
    except requests.exceptions.HTTPError:
        print("Error: Invalid city or API key.")
    except requests.exceptions.Timeout:
        print("Error: API request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your internet.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    return None

# Get city name from user input
city_input = input("Enter the city name: ")
get_weather_details(city_input)

