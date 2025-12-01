import requests
import json
import os

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
        
        # Display in user-friendly format (as per expected output)
        print(f"\nCity: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.capitalize()}")
        
        # Display JSON output
        print("\nJSON Output:")
        print(json.dumps(data, indent=4))
        
        # Prepare data to save
        weather_result = {
            "city": city,
            "temp": temperature,
            "humidity": humidity,
            "weather": weather_description.capitalize()
        }
        
        # Save to results.json file
        save_to_file(weather_result)
        
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

def save_to_file(weather_result):
    filename = "results.json"
    
    # Read existing results if file exists
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                results = json.load(f)
            except json.JSONDecodeError:
                # If file is corrupted or empty, start fresh
                results = []
    else:
        results = []
    
    # Append new result
    results.append(weather_result)
    
    # Write back to file with proper formatting
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nWeather data saved to {filename}")

# Get city name from user input
city_input = input("Enter the city name: ")
get_weather_details(city_input)

