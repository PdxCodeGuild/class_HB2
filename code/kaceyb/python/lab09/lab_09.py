# VERSION 1 #


import json
import requests

# response = requests.get("https://favqs.com/api/qotd")

#
# print(response)
# print(type(response))
# print(response.text)
# print(response.status_code)

# quote = response.text
# json_response = response.json()

# quote_author = json_response['quote']['author']

# quote_body = json_response['quote']['body']

# print(f'The author is {quote_author}\nTheir quote: {quote_body}')


#       VERSION 2       #



page_number = 1  # Starts page_number at page 1

search_term = input("Enter a keyword to search for quotes: ") # Gives the user an input to search for term


def get_response(search_term):  # Make a function to make code reusable and keep program clean
    """ Pulls JSON from API and converts it into a dictionary

    Args:
        search_term (string): Term that the API uses to search with
        
    Returns:
        boolean: True if last page, False if not
        dictionary: API response(big jumbled mess of dictionary key/value pairs)
    """
    response = requests.get(
        f"https://favqs.com/api/quotes?page={page_number}&filter={search_term}", # F string that builds the API URL
        headers={"Authorization": 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, # API Token which gives access [200]=Success [401]=Unathorized
    ) 

    json_response = response.json() # creates dictionary from JSON

    is_last_page = json_response["last_page"] # "last_page is a field inside JSON_response which returns True or False THEN assigns it to is_last_page"

    return is_last_page, json_response 


is_last_page = False # Assigning False so the loop will run at least once
quotes_list = [] # Assigning an Empty list to the quotes_list(initiating dictionary)
while is_last_page == False: # Beginning while loop
    is_last_page, json_response = get_response(search_term) # Calling function and assigning responses
    for i in range(len(json_response["quotes"])): # For loop to loop through all the quotes

        author_json = json_response["quotes"][i]["author"] # Get author from quotes for the current quote, i
        quote_json = json_response["quotes"][i]["body"] # Get quote body from quotes for the current quote, i

        print(f'"{quote_json}"\nBy {author_json}\n') # Print formatted string to display the quote and author
    user_is_done = input("enter 'next page' or 'done': ").lower().strip() # Ask the user if they want to continue
    page_number += 1 # Incrementing page_number by 1 each loop
    if user_is_done == "done": # Taking user inputs "done" and breaking the loop ending the program
        break
