import requests

# respose = requests.get('https://google.com')

# print(respose)
# print(type(respose))
# print(respose.text)
# print(respose.status_code)


# respose = request.get('https://api.chucknorris.io/jokes/random')
respose = request.get('https://api.chucknorris.io/jokes/categories')
# print(respose)
# print(respose.text)


joke = respose.json()
print(joke)
print(joke['value'])