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

selection_1 = input("\nSelect the first of three cards: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K. ")
selection_2 = input("\nSelect the second card: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K. ")
selection_3 = input("\nSelect the third and last card: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K. ")

selection_1_int = cards[selection_1]
selection_2_int = cards[selection_2]
selection_3_int = cards[selection_3]
sum = selection_1_int + selection_2_int + selection_3_int

if sum < 17:
    print(f"\n{sum}  Hit") 

elif sum in range (17, 20):
    print(f"\n{sum}  Stay") 

elif sum == 21:
    print(f"\n{sum}  Blackjack") 

elif sum > 21:
    print(f"\n{sum}  Already Busted") 
