# Lab 5: Pick6

# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. 
# Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
# If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

#     a ticket costs $2
#     if 1 number matches, you win $4
#     if 2 numbers match, you win $7
#     if 3 numbers match, you win $100
#     if 4 numbers match, you win $50,000
#     if 5 numbers match, you win $1,000,000
#     if 6 numbers match, you win $25,000,000

# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. 
# Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.
# Steps

#     Generate a list of 6 random numbers representing the winning tickets
#     Start your balance at 0

#     Loop 100,000 times, for each loop:
#     Generate a list of 6 random numbers representing the ticket
#     Subtract 2 from your balance (you bought a ticket)
#     Find how many numbers match
#     Add to your balance the winnings from your matches
#     After the loop, print the final balance

# Version 2

# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
# ====================================================================================================================================================

import random

ticket = []


def pick6():
    # ticket = []
    for r in range(6):
        y = random.randint(1,99)
        ticket.append(y)
    # print(ticket)
    return ticket

winning_ticket = pick6()    
print(f"winning ticket: {winning_ticket}")


def num_matches(winner, ticket):
    index = 0
    matching_nums = 0
    while index < 6:
        if ticket[index] == winner[index]:
            matching_nums += 1
        index += 1
    print(matching_nums)
    return matching_nums
num_matches(winning_ticket, ticket)


# #=====================

expenses = 0
earnings = 0
simulations = 0

cost_of_ticket = 2

while simulations < 100000:
    new_ticket = pick6()
    # print(simulations)
    total_matches = num_matches(winning_ticket, new_ticket)

    expenses += cost_of_ticket

    if total_matches == 1:
        earnings += 4
    elif total_matches == 2:
        earnings += 7
    elif total_matches == 3:
        earnings += 100
    elif total_matches == 4:
        earnings += 50000
    elif total_matches == 5:
        earnings += 1000000
    elif total_matches == 6:
        earnings += 25000000
    simulations += 1
    print(earnings)
    # print(simulations)
    
# #================================================================
# #Version2
# #================================================================
#     expenses = simulations * 2
#     # print(expenses)
#     # ROI = (earnings - expenses) / expenses
#     ROI = (balance - expenses) / expenses

#     print(f"earnings:{balance}")
#     print(f"expenses:{expenses}")
#     print(f"ROI:{round(ROI, 2)}")






