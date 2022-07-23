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


# Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10.
player_cards = []

# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).

for player_card in range(1, 4):
    player_cards.append(input(f"What's your card #{player_card}: ").upper())

# At this point, assume aces are worth 1. Use the following rules to determine the advice:

#     Less than 17, advise to "Hit"
#     Greater than or equal to 17, but less than 21, advise to "Stay"
#     Exactly 21, advise "Blackjack!"
#     Over 21, advise "Already Busted"


def summ(nums):
    total = 0
    cards = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

    for num in nums:
        total = total + cards[num]
    return total


cards_total = summ(player_cards)

if cards_total < 17:
    result = "Hit"
elif cards_total >= 17 and cards_total < 21:
    result = "Stay"
elif cards_total == 21:
    result = "Blackjack!"
else:
    result = "Already Busted"

# Print out the current total point value and the advice.

print(f"{cards_total} is a {result}")
