def blackjack_advice():
    card_points = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
    }

    choice1 = input('What is your first card? ')
    choice2 = input('What is your second card? ')
    choice3 = input('What is your third card? ')

    card_sum = int(card_points[choice1]) + int(card_points[choice2]) + int(card_points[choice3])
    
    if card_sum < 17:
        print(f'{card_sum} Hit')
    elif 17 <= card_sum < 21:
        print(f'{card_sum} Stay')
    elif card_sum == 21:
        print('Blackjack!')
    else: 
        print('Already Busted')

blackjack_advice()