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


def pick6():
    winning = []
    ticket = []

    for r in range(6):
        x = random.randint(1,99)
        y = random.randint(1,99)
        winning.append(x)
        ticket.append(y)
    print(winning)
    print(ticket)
    return winning, ticket
pick6()


def num_matches(winning, ticket):
    index = 0
    matching_nums = 0

    while index < 6:
        if winning[index] == ticket[index]:
            matching_nums += 1
        index += 1
    print(matching_nums)
    return matching_nums
# num_matches()


#=====================


balance = 0
simulations = 0



while simulations < 100000:
    simulations += 1
# print(simulations)
    winning, ticket = pick6()
    matching_nums = num_matches(winning, ticket)

    if matching_nums == 0:
        balance -= 2
    if matching_nums == 1:
        balance += 2
    if matching_nums == 2:
        balance += 5
    if matching_nums == 3:
        balance += 98
    if matching_nums == 4:
        balance += 48998
    if matching_nums == 5:
        balance += 999998
    if matching_nums == 6:
        balance += 24999998
    
    print(balance)
    # print(simulations)
    
#================================================================
#Version2
#================================================================
    expenses = simulations * 2
    # print(expenses)
    # ROI = (earnings - expenses) / expenses
    ROI = (balance - expenses) / expenses

    print(f"earnings:{balance}")
    print(f"expenses:{expenses}")
    print(f"ROI:{round(ROI, 2)}")






