import requests
# Replace with your OpenWeatherMap API key
api_key = "1690a9d407c5b12fa76df1c84f13bcb4"


# Replace with the city and country code for the location you want weather data for
city = "Agadir"

# Build the API request URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Send the GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract and print the temperature (in Kelvin)
    temperature = data["main"]["temp"]
    print(f"Temperature in {city}: {temperature - 273} C")
else:
    print(f"Request failed with status code: {response.status_code}")
