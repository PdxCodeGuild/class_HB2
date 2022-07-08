#Matt Nichols
#Lab04

#Version 1

#Choices to pull from
cards = {
    "a": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5, 
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "j": 10,
    "q": 10,
    "k": 10
}

#While loop so the user can continue to put numbers unless they feel like exiting
while True:
    #Try and except block starting from the beginning to the end, so if they make an input error no matter where, it goes back to the top
    try:
        #Sequence of asking for the players hand starting with card one. ALSO, giving them a outing if they decide to exit
        card_one = input("What's your first card?\nYour options are (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\nType 'done' to exit\n").lower()
        if card_one == 'done':
            print("goodbye")
            break

        value_of_card_one = cards[card_one]
        print(value_of_card_one)

        #card 2   
        card_two = input("What's your second card?\nYour options are (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\nType 'done' to exit\n").lower()
        if card_two == 'done':
            print('goodbye')
            break

        value_of_card_two = cards[card_two]
        print(value_of_card_two)

        #card 3
        card_three = input("What's your third card?\nYour options are (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\nType 'done' to exit\n").lower()
        if card_three == 'done':
            print('Goodbye')
            break
        
        value_of_card_three = cards[card_three]
        print(value_of_card_three)
        
        #Taking their cards and getting the total
        value_of_first_three_cards = value_of_card_one + value_of_card_two + value_of_card_three
    
        #If statement for what recommendation I should apply
        if value_of_first_three_cards < 17:
            print(f"Your total is: {value_of_first_three_cards}. I'd advise that you hit")
        elif value_of_first_three_cards >= 17 and value_of_first_three_cards < 21:
            print(f"Your total is: {value_of_first_three_cards}. I'd advise that you stay")
        elif value_of_first_three_cards == 21:
            print(f"Your total is: {value_of_first_three_cards}!!! Nice, that's blackjack")
        elif value_of_first_three_cards > 21:
            print(f"Your total is: {value_of_first_three_cards}... Sorry, you busted")
    
    except:
        print("That input did not go along with the choices that were presented\nEnsure that you put the options that are shown\n...............................................................")
