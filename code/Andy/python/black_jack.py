jack = {
'A': 1,
 '2' : 2,
 '3': 3,
 '4': 4,
 '5': 5,
 '6': 6,
 '7': 7,
 '8': 8,
 '9': 9,
 '10': 10,
 'J':10,
 'Q':10,
 'K': 10
  }         #putting all cards in a dict to be able to pull from when i get further down

gambler = input('pick your first card from this selection A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K: ').upper()
gambler2 = input('pick your second card from this selection A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K: ').upper() #.upper at the end of the input only works if YOU PUT THE PARENTHESIS!
gambler3 = input('pick your third card from this selection A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K: ').upper()

# if gambler == 'a' or 'j' or 'q' or 'k':
#     gambler == gambler.upper  #one way of having it become an uppercase above is the waaay easier way of doing that. that works for sure 
first = jack[gambler]

second = jack[gambler2]
third = jack[gambler3] #first second and third are vaiables that call dictionary of jack and use the input of the gambler to get the the value of their selection 

sum = first + second + third #the addition of all their values into one variable 



if sum < 17:    #if below 17
    print(f'your value is {sum}. Adise to Hit!')

elif sum in range (17 ,20):
    print(f'your value is {sum}. Advise to STAY!')   #if between 17 and 20

elif sum == 21:     #if equal to 21
    print('BLACKJACK!')

elif sum > 21:
    print('BUST!')    #if statments if greater than 21



# print(gambler.upper()) #.upper doesnt work on the outside of the inputs but works in the print statment. and need open and closing parenthesis for it to work 





