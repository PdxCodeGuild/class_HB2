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


coins = [
    ("half-dollar", 50),
    ("quarter", 25),
    ("dime", 10),
    ("nickel", 5),
    ("penny", 1),
]

while True:

    dollar_amount = ""  # dollar_amount needs to be defined before used further on, dollar_amount equals empty string
    print("Welcome to the Change Maker 5000")
    while (
        type(dollar_amount) != float
    ):  # while the type of dollar_amount does NOT equal a float
        dollar_amount = input(
            "Enter a dollar amount: $"
        )  # dollar_amount equals user-input of dollar_amount as a "string" all inputs are strings
        try:
            dollar_amount = float(
                dollar_amount
            )  # try to convert dollar_amount to a float
            # print(type(dollar_amount))
        except:
            print(
                f"Please enter a valid float: example is '1.57'"
            )  # goes into this line when the user enters an invalid input
    dollar_amount = dollar_amount * 100
    half_dollars = dollar_amount // 50
    # dollar_amount = dollar_amount-(half_dollars * 50)
    dollar_amount = dollar_amount % 50
    # print(dollar_amount)
    # print(half_dollars)

    quarters = dollar_amount // 25
    dollar_amount = dollar_amount - (quarters * 25)
    # print(quarters)
    #
    dimes = dollar_amount // 10
    dollar_amount = dollar_amount - (dimes * 10)
    # print(dimes)

    nickels = dollar_amount // 5
    dollar_amount = dollar_amount - (nickels * 5)
    # print(nickels)

    # print('total before', dollar_amount)

    pennies = dollar_amount / float(1)
    # print('number of pennies', pennies)
    penny_amount = pennies * float(1)
    dollar_amount = dollar_amount - penny_amount
    # print(dollar_amount)
    # print(pennies)

    # print(f"{int(half_dollars)}:Half Dollars {int(quarters)}:Quarters {int(dimes)}:Dimes {int(nickels)}:Nickles {int(pennies)}:Pennies")
    statement = ""
    if half_dollars > 0:
        statement = statement + " " + str(int(half_dollars)) + " " + "Half Dollars"

    if quarters > 0:
        statement = statement + " " + str(int(quarters)) + " " + "Quarters"

    if dimes > 0:
        statement = statement + " " + str(int(dimes)) + " " + "Dimes"

    if nickels > 0:
        statement = statement + " " + str(int(nickels)) + " " + "Nickels"

    if pennies > 0:
        statement = statement + " " + str(int(pennies)) + " " + "Pennies"

    print(statement)

    done = input("Would you like to make more change? yes or no: ").lower()

    if done == "no":
        print("Goodbye")
        quit()
