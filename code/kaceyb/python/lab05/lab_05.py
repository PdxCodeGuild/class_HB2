#     RANDOM TEST of '\n' concatinated to the file.write     #

# def get_greeting(name):
#     return f'Good evening {name}'
# message = get_greeting('Eric')
# file = open('get_greeting.txt', 'a')

# file.write(message + '\n')
# file.close()

# try: 
#     num = int(input('Enter a number: '))
#     divide_num = 100/num
# except (ValueError, ZeroDivisionError):
#     print('Please enter a number other than zero')
#     # print(ex, 'printing the ex error')
#     # print(type(ex))
# # except ZeroDivisionError:
# #     print('Numbers cannot = 0')
# else:
#     print('We are printing the else clause')

# message = input('Enter a number: ')

# try:
#     numbers = float(message)
# except ValueError:
#     print('Please enter a number')
# else:
#     print('Your number converted successfully')
# finally:
#     print('Finally is printing')

# names = ['Peter', 'Parker']

# while True:
#     message = input('Enter a number:')
#     try:
#         number = int(message)
#         names[number] #names[4] creates an out of index range error
#         break
#     except(ValueError, IndexError) as error:
#         if type(error) == IndexError:
#             print('We have an index error')
#         else:
#             print('Pleaes enter a valid number')
#         # print(error, 'Printing except error')
        
# print('No error has occured')



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


#                VERSION 1              #
import random


def num_matches(winning, ticket):
    matches = 0
    for number in range(6):
        # print(winning[number], ticket[number])
        
        
        if winning[number] == ticket[number]:
            # print("YOU WIN!")
            matches += 1       
    return matches
# Generate a list of 6 random numbers representing the winning tickets
def pick6():
    ticket_numbers = [] 
    for x in range(6):
        # print(x)
        ticket_numbers.append(random.randint(1, 99))
        # print(ticket_numbers)
    return ticket_numbers


winning_ticket = pick6()
earnings = 0
runs = 100000
expenses = runs*2

for x in range(runs):

    match_counter = 0

    match_counter += num_matches(winning_ticket, pick6())
    
    
    if match_counter == 1:
        earnings += 4
    elif match_counter == 2:
        earnings += 7
    elif match_counter == 3:
        earnings += 100
    elif match_counter == 4:
        earnings += 50000
    elif match_counter == 5:
        earnings += 1000000
    elif match_counter == 6:
        earnings += 25000000
    
payout = earnings - expenses

print(payout)



#        VERSION 2        #
    

roi = (earnings - expenses)/expenses

print(roi)

























