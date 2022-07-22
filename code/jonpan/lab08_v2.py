#Lab08 V2: Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time.

import requests
import time
import pprint
import random

search_term = input("Enter a word to search jokes for:  ")

response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
    'Accept': 'application/json'
})
data = response.json()

# pprint.pprint(data)

# x = random.choice(range(len(data)))
# joke = data['results'][x]['joke']
# print(joke)

while True:
    x = random.choice(range(len(data)))
    joke = data['results'][x]['joke']
    print(joke)
    more = input("do you want another joke? yes or no. ")
    if more == "no":
        print("see you later")
        break
       

# for i in range(len(data)):
#     print(random.choice(data['results'][i]['joke']))
