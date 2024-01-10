def get_weather(city='Portland, OR'):
    """Function to get the current weather for a particular City"""

    import requests
    import configparser

    from .Speak import speak

    config = configparser.ConfigParser()
    config.read("config.ini")

    api_key = config['weather'].get('api_key')

    params = {
        'access_key': api_key,
        'query': city,
        'units': 'f'
    }

    api_result = requests.get('http://api.weatherstack.com/current', params)

    api_response = api_result.json()

    params['forcast_days'] = 1

    api_result = requests.get('http://api.weatherstack.com/forecast', params).json()

    speak(f"Current temperature in "
          f"{api_response['location']['name']} is {api_response['current']['temperature']} degrees Fahrenheit. The wind"
          f" is blowing at {api_response['current']['wind_speed']} miles an hour, and it feels like "
          f"{api_response['current']['feelslike']}. Overall it is {api_response['current']['weather_descriptions']}")

    # Return the current weather
    return api_response

