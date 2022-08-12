import requests

url = 'https://icanhazdadjoke.com/'
response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})
# print(response)
data = response.json()
joke = input('want to hear a joke? y or n: ')
if joke == 'y':
    print(data['joke'])
 



