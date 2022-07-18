# Lab 06: Make Change

# Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 
# Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, 
# which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# Welcome to the Change Maker 5000 (tm)
# Enter a dollar amount: 1.36
# 5 quarters, 1 dime, and 1 penny
# Would you like make more change? yes
# Enter a dollar amount: 0.67
# 2 quarters, 1 dime, 1 nickel, 2 pennies
# Would you like make more change? no
# Have a good day!

# Version 2 (optional)

# Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

# coins = [
#     ('half-dollar', 50),
#     ('quarter', 25),
#     ('dime', 10),
#     ('nickel', 5),
#     ('penny', 1)
# ]

#============================================================================================================================================================




print("Welcome to the Change Maker 5000 (tm)")
dollar_amount = float(input("Enter a dollar amount: "))
remaining_change = dollar_amount

make_half_dollar = remaining_change // 0.50
make_quarter = remaining_change // 0.25
make_dime = remaining_change // 0.10
make_nickel = remaining_change // 0.05
make_penny = remaining_change // 0.01


change_amount = {
'half_dollar': 0,
'quarter': 0,
'dime': 0,
'nickel': 0,
'penny': 0
}


while remaining_change > 0.00:
    # print(change_amount)
    # print(remaining_change)
    if remaining_change >= 0.50:
        remaining_change = remaining_change - 0.50
        change_amount['half_dollar'] += 1
    elif remaining_change >= 0.25:
        remaining_change = remaining_change - 0.25
        change_amount['quarter'] += 1
    elif remaining_change >= 0.10:
        remaining_change = remaining_change - 0.10
        change_amount['dime'] += 1
    elif remaining_change >= 0.05:
        remaining_change = remaining_change - 0.05
        change_amount['nickel'] += 1
    elif remaining_change >= 0.01:
        remaining_change = remaining_change - 0.01
        change_amount['penny'] += 1
        # print(remaining_change)

    remaining_change = round(remaining_change, 2)
print(change_amount)
#===========================================================================




