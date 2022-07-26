# Kelin Ray
# Lab 4: Blackjack Advice

# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. 
# At this point, assume aces are worth 1. Use the following rules to determine the advice:
"""Add user input 3 cards, 1 deck, and Give advice based on those cards"""
<<<<<<< HEAD
=======

>>>>>>> 95cb38435aca229552e3df8d2ce45fef033755ae

print(f"Welcome to Blackjack Advice.")

first_card = input("Enter first card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")
second_card = input("Enter second card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")
third_card = input("Enter third card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ") 

# Deleted the random cards and now take 3 inputs for cards from the user to give advice.

print(f"Your cards are:",first_card,second_card,third_card)

if first_card == 'A':
    first_card = int('1')
elif first_card == 'J':
    first_card = int('10')
elif first_card == 'Q':
    first_card = int('10')
elif first_card == 'K':
    first_card = int('10')

if second_card == 'A':
    second_card = int('1')
elif second_card == 'J':
    second_card = int('10')
elif second_card == 'Q':
    second_card = int('10')
elif second_card == 'K':
    second_card = int('10')

if third_card == 'A':
    third_card = int('1')
elif third_card == 'J':
    third_card = int('10')
elif third_card == 'Q':
    third_card = int('10')
elif third_card == 'K':
    third_card = int('10')

first_card = (int(first_card))
second_card = (int(second_card))
third_card = (int(third_card))

card_totals = (first_card + second_card + third_card)

if card_totals < 17:
    print("You should hit.")
elif card_totals in range (17, 21):
    print("You should stay.")
elif card_totals > 21:
    print("Sorry you busted.")
elif card_totals > 20:
    print("Congratulations, Blackjack!")

# Version 2 (optional)

# Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. 
# Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. 
# For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.

