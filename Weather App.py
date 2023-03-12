import requests

def get_weather(city):
    # Make the API request
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()

    # Extract the relevant weather data
    temperature = round(data['main']['temp'] - 273.15, 2)
    description = data['weather'][0]['description']

    # Print the weather information
    print(f"The current temperature in {city} is {temperature}°C and the weather is {description}.")

# Get input from the user
city = input("Enter the name of a city to get the current weather: ")

# Get the weather information
get_weather(city)
