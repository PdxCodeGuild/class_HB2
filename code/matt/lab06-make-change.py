#Matt Nichols
#Lab06 Make change

#Version 1

#NOTE*** I put a lot of '----------------------------------' in my prints because I liked the way they looked. WILL NOT DO NEXT TIME
import math

#Function for calculating the remainder and giving the value back for quarters thru pennies
def show_coins(cents):
    quarters = coins(cents, 25)
    dime = coins(quarters[0], 10)
    nickel = coins(dime[0], 5)
    penny = coins(nickel[0], 1)
    print(f'----------------------------------\nYour total in change is:\nQuarters: {quarters[1]}\nDimes: {dime[1]}\nNickels: {nickel[1]}\nPennies: {penny[1]}\n----------------------------------')

#Function for continue or exit after number has been converted
def do_keep_going():
    while True:
        user_input = input("Would you like to convert another amount?\nType 'yes' to continue OR 'no' to exit: ")
        if user_input == 'yes':
            return user_input
        if user_input == 'no':
            return user_input
        print(f"----------------------------------\nThe input '{user_input}' is invalid.\nMake sure there are NO spaces and NO capitals in your spelling\n----------------------------------")


#Function for taking the users input and finding the amount of coins and give the remainder
def coins(gross, amount_to_quarters):
    coins = gross % amount_to_quarters
    remainder = gross // amount_to_quarters
    return [coins, remainder]

print("Welcome to the Change Maker 5000")
while True:
    #Exceptions for when the user types a letter instead of a integer
    try:
        #Input from user AND converting the amount to a whole number so that we can convert to cents easier
        dollars = float(input("----------------------------------\nEnter the amount you'd like to convert: "))
        cents = dollars * 100
        #give a whole number as the result
        cents = math.trunc(cents)
        #If user types a negative number or no value at all    
        if cents <= 0:
            print("----------------------------------\nPlease enter a number that's greater than 0\n----------------------------------")
        elif cents > 0:
            show_coins(cents)
    except:
        print(f"----------------------------------\nPlease make sure you ONLY input integers\nFor example (1.10, 3.50, 5 etc...)\n----------------------------------")
    
    keep_going = do_keep_going()
    if keep_going == 'no':
        break

print("----------------------------------\nThank you for your time.")
