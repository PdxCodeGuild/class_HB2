# Lab 08: Dad Joke API

# Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.
# Part 1

# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the Accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

# response = requests.get("https://icanhazdadjoke.com", headers={
#     'Accept': 'application/json'
# })

# Part 2

# Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time.

# response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
#     'Accept': 'application/json'
# })
# ======================================================================================================

import time
import requests

response = requests.get("https://icanhazdadjoke.com", headers={'Accept': 'application/json'})
joke = response.json()

# print(response.url)
# print(response.status_code)
# print(response.encoding)
# print(response.headers)
# print(response.text)
# print(response.json())

print(joke)

data = response.json()
# print(data[0]['title'])
for film in data:
    print(film['title'])
    print(film['release_date'])
    print(film['description'])
    print('-'*10)

#========================================

# Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time.


# response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={'Accept': 'application/json', params=query)})

