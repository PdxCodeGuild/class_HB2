#Matt Nichols
#Lab09

#Version 1

import requests
import pprint

r = requests.get("https://favqs.com/api/qotd")

#Getting the authors name
author = r.json()['quote']['author']
print(f'Author: {author}')

#Getting the quote itself
quote = r.json()['quote']['body']
print(f'Quote: {quote}')

#For aesthectics
lines_for_looks = ("----------------------------------")
print(lines_for_looks)

#Version 1 completed
#Version 2 below

#For aesthectics
lines_for_looks = ("----------------------------------")

#Function for allowing the user to go to the next page IF desired
def do_keep_going():
    while True:
        user_input = input("Would you like to continue to the next page of quotes?\nEnter 'yes' to continue OR 'no' to exit: ")
        if user_input == "no":
            return user_input
        if user_input == "yes":
            return user_input
        print(f"{lines_for_looks}\nSorry, {user_input} was NOT readable. Ensure you type 'yes' OR 'no' ")

#Function for allowing the user to view how many quotes are on the next page
def do_view():
    while True:
        user_input = input("Would you like to view the quotes?\nEnter 'yes' to continue OR 'no' to exit: ")
        if user_input == "no":
            return user_input
        if user_input == "yes":
            return user_input
        print(f"{lines_for_looks}\nSorry, {user_input} was NOT readable. Ensure you type 'yes' OR 'no' ")

#Greeting
print("Hello and Welcome, User! ")

#'''Keyword''' for my params allowing the user to enter what tags they want to read
keyword = input("Enter a keyword to search for quotes: ")

#'''page''' for them to start on page one and to continue IF wanted
page = 1

#requesting a response from the following down below
r = requests.get(f'https://favqs.com/api/quotes',
params={'page': page, 'filter': keyword}, 
headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

#The variable '''quotes''' is allowing us to fall into a deeper level with the url and pull what we desire from the following dictionary 'qoutes'
quotes = r.json()['quotes']

#The variable '''last_page''' allows us to use a boolean value for our while loop and continue on to the next page if optional
last_page = r.json()['last_page']

while True:
    
    #Tells the user how many quotes are on the next page
    print(lines_for_looks)
    print(f'There are {len(quotes)} quotes that appear on Page{page} with this keyword')
    print(lines_for_looks)
    
    view = do_view()
    if view == 'no':
        break
    
    #prints the auther and quote
    for q in quotes:
        print(f"Author: {q['author']}")
        print(f"Quote: {q['body']}")
        print(lines_for_looks)
    
    #Pulling the '''last_page''' variable in
    #IF it's the last page it will break 
    if last_page == True:
        print("That's all the quotes from this keyword")
        break
    #If it's NOT the last page it will give them the option to continue OR exit
    if last_page == False:
        keep_going = do_keep_going()
        if keep_going == 'no':
            break
        elif keep_going == 'yes':
            #Pulling in one of the values of are query
            page = page + 1
            #We have to print this out again or it will continue to print out the same results
            #This is due to the variable '''r''' being a contant and out of the while loop
            r = requests.get(f'https://favqs.com/api/quotes',
            params={'page': page, 'filter': keyword}, 
            headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            quotes

print("Thanks for your time")

#Version 2 completed












# print(r)
# pprint.pprint(r.text)
# print("------")
# pprint.pprint(r.json())