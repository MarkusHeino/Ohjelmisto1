import requests

def get_weather_data(api_key, municipality):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": municipality,
        "appid": api_key,
        "units": "metric"  # lämpötila celciuksina
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    api_key = "8096a9dbf4212bdaea977ed635abbbee"  # API-avain
    municipality = input("Enter a municipality: ")

    weather_data = get_weather_data(api_key, municipality)

    if weather_data:
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        print(f"Weather in {municipality}: {weather_description}")
        print(f"Temperature: {temperature}°C")
    else:
        print("Failed to fetch weather data. Please check the municipality name or API key.")

if __name__ == "__main__":
    main()
