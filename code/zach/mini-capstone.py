from authlib.jose import jwt # https://docs.authlib.org/en/latest/jose/index.html
import time # https://www.systutorials.com/how-to-get-the-epoch-timestamp-in-python/
import requests


def create_key(signature_alg, key_id, team_id, service_id, iat, key_path):
    """This function takes the required information as arguments and returns an encoded key to pass as a parameter for the Apple WeatherKit API."""
    with open(key_path, 'rb') as f:
        key = f.read()
    
    header = {
        "alg": signature_alg,
        "kid": key_id,
        "id": f"{team_id}.{service_id}",
    }
    
    payload = {
        "iss": team_id,
        "iat": iat,
        "exp": iat + 100,
        "sub": service_id
    }

    s = jwt.encode(header, payload, key)

    return s

def get_weather(language='en', latitude=0, longitude=0, web_token):
    response = requests.get(f"https://weatherkit.apple.com/api/v1/weather/{language}/{latitude}/{longitude}", params={
        'Authorization': f'Bearer {web_token}'
    })
    print(response.json())
    
def main():
    web_token = create_key("ES256",
        "74B4NT7KNA",
        "AJAJ8VTADD",
        "com.homedashboard.test",
        int(time.time()),
        "C:/Users/zacha/OneDrive/Coding/Keys/Home_Dashboard/WeatherKit/AuthKey_74B4NT7KNA.p8"
        )

    
    
    
main()