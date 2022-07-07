'''Lab 4: Blackjack Advice

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. 
At this point, assume aces are worth 1. Use the following rules to determine the advice:

    Less than 17, advise to "Hit"
    Greater than or equal to 17, but less than 21, advise to "Stay"
    Exactly 21, advise "Blackjack!"
    Over 21, advise "Already Busted"

Print out the current total point value and the advice.

What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit

What's your first card? K
What's your second card? 5
What's your third card? 5
20 Stay

What's your first card? Q
What's your second card? J
What's your third card? A
21 Blackjack!'''

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
    "K": 10
}



while True:
    card_one = input("What's your first card?\nYour options are (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\nType 'done to exit")
    if card_one == 'done':
        print("goodbye")
        break

    try:
        value_of_card_one = cards[card_one]
        print(value_of_card_one)
    except:
        print("That input did not follow the choices that were presented\nEnsure that you put the options that are presented")

    if value_of_card_one != cards[card_one]:
        

    card_two = input("What's your second card?\nYour options are (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\nType 'done to exit")
    if card_two == 'done':
        print('goodbye')
        break

    value_of_card_two = cards[card_two]
    print(value_of_card_two)

    card_three = input("What's your third card?\nYour options are (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\nType 'done to exit")
    if card_three == 'done':
        print('Goodbye')
        break
    
    value_of_card_three = cards[card_three]
    print(value_of_card_three)

    value_of_first_three_cards = value_of_card_one + value_of_card_two + value_of_card_three



    if value_of_first_three_cards < 17:
        print(f"Your total is: {value_of_first_three_cards}. I'd advise that you hit")
    elif value_of_first_three_cards >= 17:
        print(f"Your total is: {value_of_first_three_cards}. I'd adives that you stay")
    elif value_of_first_three_cards == 21:
        print(f"Your total is: {value_of_first_three_cards}!!! Nice, that's blackjack")
    else:
        print(f"Your total is: {value_of_first_three_cards}... Sorry, you busted")

# def players_cards():
#     card_one = input("What's your first card?\n")
#     card_two = input("What's your second card?\n")
#     card_three = input("What's your third card?\n")
#     cards_value = card_one + card_two + card_three
#     return cards_value

#print(players_cards()) input = hellotherematt didn't break, there's just no space between the three.
#Could I fix that with a ", ".join(cards_value)???

# def first_three_cards():
#     card_one = input("What's your first card? ")
#     card_one_value = cards[card_one]
#     print(card_one_value)
#     card_two = input("What's your second card? ")
#     card_two_value = cards[card_two]
#     print(card_two_value)
#     card_three = input("What's your third card? ")
#     card_three_value = cards[card_three]
#     print(card_three_value)
#     first_three_cards_value = card_one_value + card_two_value + card_three_value
#     return first_three_cards_value
# #print(first_three_cards()) works exactly as needed: gives three cards and sums them up to print the result
# while True:
#     print("Type 'done' to exit at anytime")
#     cards_given = first_three_cards()
#     if cards_given == 'done':
#         result = "Okay, thank you for your time"
#         print(result)
#         break
# def first_three_cards():
#     card_one = input("What's your first card?\nYour options are (A, 2, 3, 4, 5, 6, 7, 8, 9, 10. J, Q, K)\n ")
#     card_one_value = card_one or cards[card_one]
#     print(card_one_value)
#     card_two = input("What's your second card?\nYour options are (A, 2, 3, 4, 5, 6, 7, 8, 9, 10. J, Q, K)\n ")
#     card_two_value = cards[card_two]
#     print(card_two_value)
#     card_three = input("What's your third card?\nYour options are (A, 2, 3, 4, 5, 6, 7, 8, 9, 10. J, Q, K)\n ")
#     card_three_value = cards[card_three]
#     print(card_three_value)
#     first_three_cards = card_one_value + card_two_value + card_three_value
#     first_three_cards_value = str(first_three_cards)
#     return first_three_cards_value

# while True:
#     print("Type 'done' to exit at anytime")
#     cards_given = first_three_cards()
#     if cards_given == 'done':
#         result = "Okay, thank you for your time"
#         print(result)
#         break






    


    

    
