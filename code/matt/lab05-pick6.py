#Matt Nichols
#Lab05

#Version 1

#Importing random for future random.randint(1, 99)
import random

#The payoff of each ticket they've purchased
payoff = {
    0: -2,
    1: 2,
    2: 5,
    3: 98,
    4: 49998,
    5: 999998,
    6: 24999998
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
    for index in range(0,6):
        if player_ticket[index] == winning_ticket[index]:
            matches += 1
    return matches 

#Winning ticket so it prints once and we can compare the players tickets to it
winning_ticket = random_ticket()

#List for future computing and getting the total earnings
ticket_list = []

#Attempts starting at 0 so we can give are while loop a break point
attempts = 0

while attempts < 100000:
    attempts += 1

    #Runs through player_ticket 100,000 times so we can start to compare the earnings (losses)
    player_ticket = random_ticket()

    value_of_ticket = get_value(player_ticket, winning_ticket)

    #Implementing the matches from our get_value functions into keys of our dictionary(payoff) to pull numbers
    earnings_of_each_ticket = payoff[value_of_ticket]

    #Pulling the list we created earlier and appending the earnings to it
    ticket_list.append(earnings_of_each_ticket)

#breaking from the loop and giving one earnings (losses) statement    
total_earnings = (sum(ticket_list))
print(f'Your total is: {total_earnings}')

    



    
#print(players_numbers()) = [32, 40, 63, 83, 45, 71, 54]

# def get_index_and_nums():
#     for i, nums in enumerate(winning_numbers()):
#         print(i, nums)
#     for i, nums in enumerate(players_numbers()):
#         print(i, nums)
#     return get_index_and_nums()

        

# print(get_index_and_nums())


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
    