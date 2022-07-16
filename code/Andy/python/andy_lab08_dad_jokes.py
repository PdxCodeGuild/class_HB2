import requests

url = 'https://icanhazdadjoke.com/'
response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})
print(response)
data = response.json()

print(data['joke'])