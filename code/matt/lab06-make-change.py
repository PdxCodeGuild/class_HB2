#Matt Nichols
#Lab06 Make change

#Version 1
import math
total = 0
quarters = .25
dimes = .10
nickels = .05
pennies = .01 

total_of_qaurters = []
total_of_dimes = []
total_of_nickels = []
total_of_pennies = []

def users_amount():
    user_input = float(input("Enter a dollar amount to convert it to cents, for example 1.36, 3.50, 5.00 etc...\nEnter your amount: "))
    return user_input

def continue_or_exit():
    user_input = input("Would you like to convert another amount?\nType 'yes' to continue OR 'no' to exit the program: ")
    return user_input

# def amount_to_quaters(nums):
#     convert_quarters = nums / 1
#     if convert_quarters >= quarters:
#         amount_in_quarters = nums // quarters
#         amount_in_quarters = math.trunc(amount_in_quarters)
#         print(amount_in_quarters)
#     return amount_in_quarters

# amount_to_quaters(users_amount())

# def amount_to_dimes(nums):
#     convert_dimes = nums / 1
#     if convert_dimes < quarters and convert_dimes >= dimes:
#         amount_in_dimes = nums // dimes
#         amount_in_dimes = math.trunc(amount_in_dimes)
#         print(amount_in_dimes)
#     return amount_in_dimes

response = users_amount()
convert = response / quarters
convert = convert - (response // quarters)
convert = convert * quarters
convert = round(convert, 3)


print(convert)





    



    
    



# print("Welcome to the Change Maker 5000 ")

# while True:
#     amount = users_amount()
#     convert_to_cents = amount / 1
#     if convert_to_cents >= 0.25:
#        amount_in_quarters =  amount // quarters
#        print(amount_in_quarters)
#        remainder = ((amount / quarters) - amount_in_quarters) * quarters
#        #remainder = amount_in_quarters * quarters
#        print(remainder)
       

    



