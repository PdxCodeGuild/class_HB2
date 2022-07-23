#Matt Nichols
#Lab08

#Version1

import requests 
import pprint

lines_for_looks = "-----------------------------------------"
#For future using to seperate the jokes

response = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'})

joke = response.json()
#pulling from the dictionary

print(f"{joke['joke']}\n{lines_for_looks}")
#print the actual joke itself

###VERSION2

#For while loop
index = 0

#Function for allowing the user to view another joke
def do_keep_going():
    while True:
        user_input = input("Would you like to see another joke from this genre? y/n: ")
        if user_input == 'n':
            return user_input
        if user_input == 'y':
            return user_input
        print("Please enter 'y' to continue OR 'n' to exit the program")
    
#print("Thanks for your time")
search_term = input("Enter the genre of joke\n")
#For user to input their own genre of joke

response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
'Accept': 'application/json'})
#New get request with query

results = response.json()['results']
#Pulling from the searchterm and giving a list of jokes

number_of_jokes = response.json()['total_jokes']
#The amount of jokes for the user to see
print(f"There are {number_of_jokes} jokes in this genre")    


while index < len(results):
    print(f"{lines_for_looks}\n{results[index]['joke']}\n{lines_for_looks}")
    index = index + 1
    
    keep_going = do_keep_going()
    if keep_going == 'n':
        break

number_of_jokes_left = number_of_jokes - index    
print(f"There are {number_of_jokes_left} jokes left from this genre. Thanks for your time.")
    