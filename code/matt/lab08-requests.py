import requests
import pprint
# response = requests.get("https://icanhazdadjoke.com", headers={
#     'Accept': 'application/json'
# })

#print(response.text)
# joke = response.json()
# print(joke['joke'])

#version 1
# joke = response.json()
# search_term = input("Input a genre for a joke you'd like to see ")

#Think about how to do this.. First we need to figure out how to pull a singular joke. secondly

# response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
#     'Accept': 'application/json'
# })
# print(response.text)
# joke = response.json()
# first_step = (joke['results'])
# second_step = (first_step[0]['joke'])
# print(second_step)
# for key in range (len(first_step)):
#     print(key, first_step[key])

# # joke = response.json()
# # search_term = joke['golf']
# # print(response.json())
# # joke = response.json()

response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})
# print(response)
# print(response.url)
# print(response.encoding)
# print(response.status_code)
# print(response.headers)

# pprint.pprint(response.text)
# pprint.pprint(response.json())
jokes = response.json()
pprint.pprint(jokes)
print("------------------")
print(jokes)
# print(f'there are {len(jokes)}')
# for joke in jokes:
#     print(jokes)

