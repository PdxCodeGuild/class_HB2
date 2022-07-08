'''Lab 5: Pick6

Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. 
Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

    a ticket costs $2
    if 1 number matches, you win $4
    if 2 numbers match, you win $7
    if 3 numbers match, you win $100
    if 4 numbers match, you win $50,000
    if 5 numbers match, you win $1,000,000
    if 6 numbers match, you win $25,000,000

One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. 
Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.
Steps

    Generate a list of 6 random numbers representing the winning tickets
    Start your balance at 0
    Loop 100,000 times, for each loop:
    Generate a list of 6 random numbers representing the ticket
    Subtract 2 from your balance (you bought a ticket)
    Find how many numbers match
    Add to your balance the winnings from your matches
    After the loop, print the final balance'''
import random
#print(random.randint(1,99)) - gives random number 1-99 as expected
def winning_numbers():
    nums = []
    while len(nums) < 7:
        nums.append(random.randint(1, 99))
    return nums
#print(winning_numbers()) = [54, 56, 20, 55, 81, 48, 23]

def players_numbers():
    nums = []
    while len(nums) < 7:
        nums.append(random.randint(1, 99))
    return nums
#print(players_numbers()) = [32, 40, 63, 83, 45, 71, 54]

def get_index_and_nums():
    for i, nums in enumerate(winning_numbers()):
        print(i, nums)
    for i, nums in enumerate(players_numbers()):
        print(i, nums)
    return get_index_and_nums()

        

print(get_index_and_nums())


#for i, value in enumerate(winning_numbers()):
#     print(i, value) =
#     0 13
#     1 69
#     2 87
#     3 8
#     4 47
#     5 70
#     6 73


#for index in winning_numbers():
    # print(index)
    # 23
    # 4
    # 84
    # 21
    # 14
    # 80
    # 85
#for index in range(len(winning_numbers())):
    # print(winning_numbers()[index]) =
    # 15
    # 79
    # 99
    # 89
    # 60
    # 44
    # 32
    #print(winning_numbers())
    # [65, 56, 27, 79, 93, 83, 76]
    # [54, 77, 34, 38, 90, 75, 15]
    # [94, 26, 5, 94, 63, 35, 30]
    # [63, 23, 57, 51, 28, 31, 71]
    # [73, 97, 49, 81, 34, 72, 57]
    # [91, 88, 32, 60, 56, 84, 60]
    # [30, 91, 20, 25, 72, 91, 24]
    #print(index) = 
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    