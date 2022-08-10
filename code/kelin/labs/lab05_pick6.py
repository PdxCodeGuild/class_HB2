# Kelin Ray

# Lab 5 Pick6

# Have the computer play pick6 many times and determine net balance.

import random

# Write the following functions and use them in the code:

# - `pick6()`: Generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Return the list

def pick6(): # First function generates a list of 6 random numbers
    nums = [] # Winning numbers
    for i in range(0,6):
        x = random.randint(1, 99)
        nums.append(x)
    return(nums)

winning = pick6() # Winning numbers
ticket = pick6() # Player numbers

# - `num_matches(winning, ticket)`: Return the number of matches between the winning numbers and the ticket.

def num_matches(winning, ticket): # Second function returns the number of matches
    matches = 0
    for index in range(0, 6): # Looking for 6 matches
        if winning[index] == ticket[index]:
            matches += 1
    return matches

balance = 0
ticketprice = 2
# times_played = 100000
earnings = []
plays = 0
winningmatches = { # Winning amounts
    '0': 0,
    '1': 4,
    '2': 7,
    '3': 100,
    '4': 50000,
    '5': 1000000,
    '6': 25000000
}
while plays < 100000:
    plays += 1 # Creates loop for 100,0000 plays

    winningmatches = num_matches(ticket, winning) # Gets the number of winning matches and number values

    # winningticket = winningmatches[num_matches] - ticketprice # Subtracts ticket price from winnings

    earnings.append(winningmatches) # Adding earnings
  
total_winnings = (sum(earnings))
print(f'You had {winningmatches} matches')
print(f'You have won {total_winnings}')

# ## Steps

# 1. Generate a list of 6 random numbers representing the winning tickets
# 2. Start your balance at 0
# 3. Loop 100,000 times, for each loop:
# 4. Generate a list of 6 random numbers representing the ticket
# 5. Subtract 2 from your balance (you bought a ticket)
# 6. Find how many numbers match
# 7. Add to your balance the winnings from your matches
# 8. After the loop, print the final balance

# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are `[5, 10]` and your ticket numbers are `[10, 5]` you have **0** matches. If the winning numbers are `[5, 10, 2]` and your ticket numbers are `[10, 5, 2]`, you have **1** match. Calculate your net winnings (the sum of all expenses and earnings).

# - a ticket costs $2
# - if 1 number matches, you win $4
# - if 2 numbers match, you win $7
# - if 3 numbers match, you win $100
# - if 4 numbers match, you win $50,000
# - if 5 numbers match, you win $1,000,000
# - if 6 numbers match, you win $25,000,000

# ## Version 2

# The ROI (return on investment) is defined as `(earnings - expenses)/expenses`. Calculate your ROI, print it out along with your earnings and expenses.

