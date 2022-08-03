# Kelin Ray

# Lab 06: Make Change

# Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 

import math

penny = 1 # Values for coins
nickel = 5
dime = 10
quarter = 25

print("Welcome to the Change Maker 5000 (tm)") # Welcome message

i = input("Enter a dollar amount: ") # User enters a dollar amount

i = int(i) # User input becomes an integer

if i >= quarter:
    quarter_n = i // quarter # Gets amount of quarters from dollar amount
    i = i - quarter * quarter_n
    if i >= dime:
        dime_n = i // dime # Gets amount of dimes
        i = i - dime * dime_n
        if i >= nickel:
            nickel_n = i // nickel # Gets amount of nickels
            i = i - nickel * nickel_n
            if i >= penny:
                penny_n = i // penny # Gets amount of pennies
                print (quarter_n,"quarters,",dime_n,"dimes",nickel_n,"nickels",penny_n,"pennies")
        else:
            if i >= penny:
                penny_n = i // penny
                print (quarter_n,"quarters,",dime_n,"dimes",penny_n,"pennies")
    else:
        if i >= nickel:
            nickel_n = i // nickel
            i = i - nickel * nickel_n
            if i >= penny:
                penny_n = i // penny
                print (quarter_n,"quarters,",nickel_n,"nickels",penny_n,"pennies")
        else:
            if i >= penny:
                penny_n = i // penny
                print (quarter_n,"quarters,",penny_n,"pennies")
else:
    if i >= dime:
        dime_n = i // dime
        i = i - dime * dime_n
        if i >= nickel:
            nickel_n = i // nickel
            i = i - nickel * nickel_n
            if i >= penny:
                penny_n = i // penny
                print (dime_n,"dimes",nickel_n,"nickels",penny_n,"pennies")
        else:
            if i >= penny:
                penny_n = i // penny
                print (dime_n,"dimes",penny_n,"pennies")
    else:
        if i >= nickel:
            nickel_n = i // nickel
            i = i - nickel * nickel_n
            if i >= penny:
                penny_n = i // penny
                print (nickel_n,"nickels",penny_n,"pennies")
        else:
            if i >= penny:
                penny_n = i // penny
                print (penny_n,"pennies")


# Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, 

# which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# Version 2 (optional)

# Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

# coins = [
#     ('half-dollar', 50),
#     ('quarter', 25),
#     ('dime', 10),
#     ('nickel', 5),
#     ('penny', 1)
# ]
