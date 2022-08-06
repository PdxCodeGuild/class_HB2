import jwt
import time # https://www.systutorials.com/how-to-get-the-epoch-timestamp-in-python/
import requests

def create_key(signature_alg, key_id, team_id, service_id, iat, key_path):
    """This function takes the required information as arguments and returns an encoded key to pass as a parameter for the Apple WeatherKit API."""
    with open(key_path, 'rb') as f:
        key = f.read()
    
    header = {
        "kid": key_id,
        "id": f"{team_id}.{service_id}",
    }
    
    payload = {
        "iss": team_id,
        "iat": iat,
        "exp": iat + 3600,
        "sub": service_id
    }

    s = jwt.encode(payload, key, algorithm=signature_alg, headers=header)

    return s

def get_weather(language, latitude, longitude, web_token, timezone):
    """This function takes the location data, web token from create_key(), and the timezone to return the current weather condition and temperature from the Apple WeatherKit API."""
    response = requests.get(f"https://weatherkit.apple.com/api/v1/weather/{language}/{latitude}/{longitude}", headers = {
        'Authorization': f'Bearer {web_token}',
        'Accept': 'application/json'
    }, 
    params = {
        'timezone': timezone,
        'dataSets': 'currentWeather'
    })

    weather = response.json()
    
    current_condition = weather['currentWeather']['conditionCode']
    current_temp = weather['currentWeather']['temperature']
    
    return current_condition, current_temp

def temp_converter(temp_celsius):
    return temp_celsius * 1.8 + 32
    
def main():
    web_token = create_key("ES256",
        "74B4NT7KNA",
        "AJAJ8VTADD",
        "com.homedashboard.test",
        int(time.time()),
        "C:/Users/zacha/OneDrive/Coding/Keys/Home_Dashboard/WeatherKit/AuthKey_74B4NT7KNA.p8"
        )
    print(web_token)
    current_condition, current_temp = get_weather('en', 38.933868, -77.177261, web_token, 'America/New_York')
    temp_fahrenheit = temp_converter(current_temp)
    
    print(f'It is currently {current_condition} and {round(temp_fahrenheit, 2)} degrees Fahrenheit ({current_temp} degrees Celsius).')
    
main()