#Lab08 Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.

import requests
import time

response = requests.get("https://icanhazdadjoke.com", headers={'Accept': 'application/json'})
data = response.json()

print(data['joke'])