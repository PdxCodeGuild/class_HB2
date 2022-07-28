# Pick6

# Have the computer play pick6 many times and determine net balance.

# import random

# def pick6game():
#     numbers = [] #something to put the nums in 
#     for i in range(1,7): #Should run the loop 6 times 
#         numbers.append(random.randint (1,99))
#     return numbers


# def compare(winning_ticket, current_ticket):
#     counter = 0 #keeping track of how many matches  
#     for i in range(6): #checking the index of the two arguments range is returning an array which starts at the index of 0 and then goes up to 5
#         if winning_ticket[i] == current_ticket[i]:# running the 6 times 
#             counter +=1 # counting how many match 
#     return counter 
    

# # print(compare(number_picker(), number_picker())) 
#                                                 #test
# winner = number_picker() # winning ticket on the outside so it stays constant
# balance = 0 # Holder

# for i in range(100000):
#     comparing_tickets = compare(number_picker(), winner) #i'm getting my compare function putting my number_picker funtion with in it which is the one thats gonna be getting changed the 100,000 time and comparing it to the winner which is the one that will be staying the same all those times 
#     balance -= 2  # since the balnce on top is the holder im making it -2 since that is how much it is to pay for a ticket 
#     if comparing_tickets == 1: # if one of the compared matches has one match in the same spot we get $2 since we were already losing 2
#         balance += 4
#     elif comparing_tickets == 2:
#         balance += 7 
#     elif comparing_tickets == 3:
#         balance += 100
#     elif comparing_tickets == 4:
#         balance += 50,000
#     elif comparing_tickets == 5:
#         balance += 1,000,000
#     elif comparing_tickets == 6:
#         balance += 25,000,000

# return_of_in = balance / 200000 # getting the balance and then dividing it bt the 200,000 because thats the two dollars to buy the ticket and multiplying it by the many times we're gonna but the ticket 
# print(f'The winning lotto numbers are {winner}') 
# print(f'\n and your balance is {balance}')
# print(f'Your ROI is {return_of_in}')


   


# print(users_attempt)
# print (winning_lotto_number)


# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are `[5, 10]` and your ticket numbers are `[10, 5]` you have **0** matches. If the winning numbers are `[5, 10, 2]` and your ticket numbers are `[10, 5, 2]`, you have **1** match. Calculate your net winnings (the sum of all expenses and earnings).

# - a ticket costs $2
# - if 1 number matches, you win $4
# - if 2 numbers match, you win $7
# - if 3 numbers match, you win $100
# - if 4 numbers match, you win $50,000
# - if 5 numbers match, you win $1,000,000
# - if 6 numbers match, you win $25,000,000

# Write the following functions and use them in the code:

# - `pick6()`: Generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Return the list
# - `num_matches(winning, ticket)`: Return the number of matches between the winning numbers and the ticket.

# ## Steps

# 1. Generate a list of 6 random numbers representing the winning tickets
# 2. Start your balance at 0
# 3. Loop 100,000 times, for each loop:
# 4. Generate a list of 6 random numbers representing the ticket
# 5. Subtract 2 from your balance (you bought a ticket)
# 6. Find how many numbers match
# 7. Add to your balance the winnings from your matches
# 8. After the loop, print the final balance

# ## Version 2

# The ROI (return on investment) is defined as `(earnings - expenses)/expenses`. Calculate your ROI, print it out along with your earnings and expenses.

