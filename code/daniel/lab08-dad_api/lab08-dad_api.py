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

#====================================

# print(response.text) # {"ip":"76.105.187.182"} - raw json response
# data = response.json() # turn raw json into a python dictionary
# print(data) # {'ip': '76.105.187.182'} - python dictionary
# print(data['ip']) # 76.105.187.182


#=======================================================
# Version1
#=======================================================

# import requests
# import time

# response = requests.get("https://icanhazdadjoke.com", headers={'Accept': 'application/json'})


# # print(response.text)
# joke = response.json()
# # print(joke)

# dad_joke = input("Do you wank to hear a dad joke? y or n?: ")

# while True:
#     if dad_joke == "y" or dad_joke == "yes":
#         print(joke['joke']) 
#         break
#     elif dad_joke == "n" or dad_joke == "no":
#         print("goodbye")
#         break
#     else:
#         print("Not a valid answer")
#         break



#=======================================================
# Version2
#=======================================================

import requests
import time


search_joke = input("Enter a search term to find a related dad joke: ")
# print(search_joke)

response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_joke}", headers={'Accept': 'application/json'})
# print(response)



joke = response.json()
jokes = joke["results"]

for joke in jokes:
    print(joke["joke"])
    more_jokes = input("Do you want to hear another dad joke? yes/no: ")
    if more_jokes == "yes" or more_jokes == "y":
        print(joke["joke"])
    elif more_jokes == "no" or more_jokes == "n":
        break
    else:
        print("Not a valid answer")