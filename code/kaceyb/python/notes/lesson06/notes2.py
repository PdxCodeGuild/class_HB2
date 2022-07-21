from urllib import response
import requests

# response = requests.get('https://google.com')
# print(response)
# print(type(response))
# print(response.text)
# print(response.status_code)

# response = requests.get('https://api.chucknorris.io/jokes/random')

# print(response)
# print(response.text)

# joke = response.text
# joke = response.json() #python friendly dictionary
# # print(joke)
# print(joke['value'])


# response = requests.get('https://api.chucknorris.io/jokes/categories')
# print(response.json())

# categories = response.json()

# # for category in categories:
# #     print(category)
    
# for i in range(len(categories)):
#     print(i, categories[i])
    
# choice = int(input('Select a category: '))

# query = {
#     'category': categories[(choice)]['value']
# }

# # response = requests.get(f'https://api.chucknorris.io/jokes/random?category={categories[choice]}')
# response = requests.get('https://api.chucknorris.io/jokes/random', 'params=query')

# print(response.text)


import requests
url = 'https://ghibliapi.herokuapp.com/films'
response = requests.get(url)
# print(response.text)
data = response.json()
# print(data[0]['title'])
for film in data:
    print(film['title'])
    print(film['release_date'])
    print(film['description'])

    
    print('-'*10)

