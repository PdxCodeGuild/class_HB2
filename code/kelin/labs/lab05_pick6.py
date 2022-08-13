# Kelin Ray

# Lab 5 Pick6

# Have the computer play pick6 many times and determine net balance.

import random

# Write the following functions and use them in the code:

# - `pick6()`: Generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Return the list

def pick6(): # First function generates a list of 6 random numbers
    """
    Picks 6 random numbers for player ticket and winning ticket
    """
    nums = [] # Winning numbers
    for i in range(6):
        # print(i) checking i
        x = random.randint(1, 99) 
        nums.append(x)
    return(nums)

# winning = pick6() # Winning numbers
# print(winning) checking winning numbers
# winning_ticket = [7, 24, 36, 48, 13, 59]
# # ticket = pick6() # Player numbers
# player_ticket = [7, 34, 36, 23, 13, 15]

# - `num_matches(winning, ticket)`: Return the number of matches between the winning numbers and the ticket.

def num_matches(winning, ticket): # Second function returns the number of matches 
    """
    Accepts winning and player ticket args and returns the number of matches
    """
    matches = 0
    for index in range(len(winning)): # Looking for 6 matches
        if winning[index] == ticket[index]:
            matches += 1
    return matches

# number_matches = num_matches(winning_ticket, player_ticket)

# print(f'You had {number_matches} matches')

### Worked with T/A Bruce Stull

payout = { # Winning amounts
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

expenses = 0
earnings = 0
ticket_price = 2
maxplays = 100000
plays = 0
winning_ticket = pick6()

while plays < maxplays:
    expenses += ticket_price # Bought a ticket
    player_ticket = pick6()
    winning_matches = num_matches(winning_ticket, player_ticket)
    winning_amount = payout[winning_matches]
    earnings += winning_amount
    plays += 1

print('Balance: ', earnings - expenses) 

# ## Version 2

# The ROI (return on investment) is defined as `(earnings - expenses)/expenses`. Calculate your ROI, print it out along with your earnings and expenses.

roi = (earnings - expenses) / expenses

print('ROI: ', roi)  # Prints return on investment