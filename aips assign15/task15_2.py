import requests
import json

API_KEY = "ba12414ecc2fbdd2d22d91fe289e19f6"  # Replace with your actual API key

def get_weather_with_errors(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=4))
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
get_weather_with_errors(city_name)

