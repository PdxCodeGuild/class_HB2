# Kelin Ray

# Lab 06: Make Change

# Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 

import math

### Helped by T/A Grant

coins = {
    'penny': 1,
    'nickel': 5,
    'dime': 10,
    'quarter': 25
}

print("Welcome to the Change Maker 5000 (tm)") # Welcome message

total_amount = float(input("Enter a dollar amount: ")) # User enters a dollar amount

total = total_amount * 100 # dollars input converter to pennies


quarters_n = total // coins['quarter'] # gets number of quarters

leftover_1 = total % coins['quarter'] 


dimes_n = total // coins['dime'] # gets number of quarters

leftover_2 = leftover_1 % coins['dime'] 


nickels_n = leftover_2 // coins['nickel'] # gets number of quarters

leftover_3 = leftover_2 % coins['nickel'] 


pennies_n = leftover_3 // coins['penny']

quarters = int(quarters_n)
dimes = int(dimes_n)
nickels = int(nickels_n)
pennies = int(pennies_n)


print(leftover_1, leftover_2, leftover_3, quarters, dimes, nickels, pennies)





#  = int(i) # User input becomes an integer



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
