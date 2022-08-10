#Matt Nichols
#Lab05

#Version 1

#Importing random for future random.randint(1, 99)
from os import truncate
import random
import math

#The payoff of each ticket they've purchased
ticket_price = 2
payoff = {
    '0': 0,
    '1': 4,
    '2': 7,
    '3': 100,
    '4': 50000,
    '5': 1000000,
    '6': 25000000
}

#Function for 6 numbers(1, 99) to fall into a list for future computing/comparing
def random_ticket():
    nums = []
    while len(nums) < 6:
        nums.append(random.randint(1, 99))

    return nums

#Function for comparing the matches between two lists - player_ticket and winning_ticket
def get_value(player_ticket, winning_ticket):
    matches = 0
    for index in range(0, 6):
        if player_ticket[index] == winning_ticket[index]:
            matches += 1
    return matches 

#Winning ticket so it prints once and we can compare the players tickets to it
winning_ticket = random_ticket()

#List for future computing and getting the total earnings
ticket_list = []
deductions = []
earnings = []
#Attempts starting at 0 so we can give are while loop a break point
attempts = 0

while attempts < 100000:
    attempts += 1

    #Runs through player_ticket 100,000 times so we can start to compare the earnings (losses)
    player_ticket = random_ticket()

    value_of_ticket = get_value(player_ticket, winning_ticket)

    #Implementing the matches from our get_value functions into keys of our dictionary(payoff) to pull numbers
    earnings_of_each_ticket = payoff[value_of_ticket] - ticket_price

    #Pulling the list we created earlier and appending the earnings to it
    ticket_list.append(earnings_of_each_ticket)

    ###Deductions for version 2
    deductions.append(ticket_price)

    ###Earnings for version 2
    earnings.append(payoff[value_of_ticket])

    
#breaking from the loop and giving one earnings (losses) statement    
total_earnings = (sum(ticket_list))
print(f'Your total is: {total_earnings}')

#giving roi
expenses = (sum(deductions))
earnings = (sum(earnings))


print(f"Your total earnings are: {earnings}")
print(f'Your total deductions are: {expenses}')
roi = (earnings - expenses) / expenses
roi = round(roi, 3)
print(f"Your ROI is: {roi}")


