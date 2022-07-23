# Lab 4: Blackjack Advice

# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. 
# At this point, assume aces are worth 1. Use the following rules to determine the advice:

#     Less than 17, advise to "Hit"
#     Greater than or equal to 17, but less than 21, advise to "Stay"
#     Exactly 21, advise "Blackjack!"
#     Over 21, advise "Already Busted"

# Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!
#=============================================================

import random

face_cards = {
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "A": 1
}
# #======================
# # Input validation fix
# #======================
# while True:
#     try:
#         question_1 = int(input("What's your first card?: "))
#         question_2 = int(input("What's your second card?: "))
#         question_3 = int(input("What's your third card?: "))
#     except ValueError:
#         print("Invalid Value, try agian")
#         continue
#     except TypeError:
#         print("Please enter a number")
#         continue        
#     # else:
#     #     break




card_total = 0

while True:
    if question_1 in face_cards:
        card_total += int(face_cards[question_1])
        print(f"question_1: {question_1}")

        if question_2 in face_cards:
            card_total += int(face_cards[question_2])
            print(f"question_2: {question_2}")

            if question_3 in face_cards:
                card_total += int(face_cards[question_3])
                print(f"question_3: {question_3}")
                break
            else:
                print("Not valid")
                break
        else:
            print("Not valid")
            break
    else:
        print("Not valid")
        break
if card_total < 17:
    print(f"Hit {card_total}")
elif 17 <= card_total < 21:
    print(f"Stay {card_total}")
elif card_total == 21:
    print(f"Backjack! {card_total}")
elif card_total > 21:
    print(f"Already Busted {card_total}")
else:
    print("Not Valid")





# Version 2 (optional)

# Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. 
# Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. 
# For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.
