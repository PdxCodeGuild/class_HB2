# Kelin Ray

# Lab 08: Dad Joke API

# Use the [Dad Joke API](https://icanhazdadjoke.com/api) to get a dad joke and display it to the user. You may want to also use [time.sleep](https://www.geeksforgeeks.org/sleep-in-python/) to add suspense.


# ## Part 1

# Use the [requests](../docs/15%20Requests.md) library to send an HTTP request to `https://icanhazdadjoke.com/` with the `Accept` header as `application/json`. 

import requests
import time

response = requests.get('https://icanhazdadjoke.com/', headers={
    'Accept': 'application/json'})

# If the response is in [JSON](../0%20General/09%20-%20JSON,%20CSV,%20&%20XML.md), you can turn it into a python dictionary using the `json.loads()` function or the `json()` method on the response object.
# You can then extract the relevant data.

joke = response.json() # Getting a joke from the dictionary

print(f"{joke['joke']}") # Prints the joke

# This will return a dad joke in JSON format. You can then use the `.json()` method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.


# ## Part 2

# Add the ability to "search" for jokes using [another endpoint](https://icanhazdadjoke.com/api#search-for-dad-jokes).

search = input("Search for a dad joke: ") # User search input

time.sleep(2) # Add suspense with delay

response = requests.get(f"https://icanhazdadjoke.com/search?term=${search}", headers={
'Accept': 'application/json'}) # Returns a joke from the search

#  Create a REPL that allows one to enter a search term and go through jokes one at a time.

index = 0 # For the loop

#Function for allowing the user to view another joke
def morejokes():
    while True:
        user_input = input("Press enter for another joke or type 'done': ")
        if user_input == 'done':
            return user_input
        if user_input == '': # Input picks another joke from search results
            return user_input
        print("Press enter or type 'done'")


jokelist = response.json()['results'] # List of jokes from search

while index < len(jokelist):
    time.sleep(2) # Add suspense with delay
    print({jokelist[index]['joke']}) # Prints another joke
    index = index + 1 # For looping
    
    done = morejokes() # Ends loop
    if done == 'done':
        break