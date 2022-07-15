#Matt Nichols
#Lab06 Make change

#Version 1
import math
# total = 0
# quarters = 25
# dimes = 10
# nickels = 5
# pennies = 1 

# total_of_qaurters = []
# total_of_dimes = []
# total_of_nickels = []
# total_of_pennies = []

# def users_amount():
#     user_input = float(input("Enter a dollar amount to convert it to cents, for example 1.36, 3.50, 5.00 etc...\nEnter your amount: "))
#     return user_input

# def continue_or_exit():
#     user_input = input("Would you like to convert another amount?\nType 'yes' to continue OR 'no' to exit the program: ")
#     return user_input

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


    
    

    

# response = users_amount()
# convert = response / quarters
# convert = convert - (response // quarters)
# convert = convert * quarters
# convert = round(convert, 2)


#print(convert)





    



    
    



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
       

    




# def amount_to_quarters(gross, change):
#     gross = gross / 0.01
#     to_pennies = gross / 0.01
#     coins_given = to_pennies // change
    

# def coins(gross, converter):
#     gross = gross / .01
#     coins = converter % gross
#     remainder = converter // gross

    

# print(cents_given(1.20, 25))

# def cents_remainder (gross, change):
#     to_pennies = gross / 0.01
#     cents_remaining = to_pennies % change
#     return cents_remaining
# test = (cents_remainder(1.20, 25))

# print(cents_given(test, dimes))


# gross = float(input("Enter your amount: "))


# amount_in_quarters = cents_given(gross, quarters)
# remaining = cents_remainder(gross, quarters)
# print(remaining)
# print(amount_in_quarters)

# while True:
#     amount = cents_given(gross, quarters)
#     remaining = cents_remainder(gross, quarters)
#     print(amount)
#     amount = cents_given(remaining, dimes)
#     print(amount)
    # amount = cents_given(remaining, dimes)











#def coins_in_dimes(gross, amount_to_dimes):

# def coins_in_nickels(gross, amount_to_nickels):
#     coins = gross % amount_to_nickels
#     remainder = gross // amount_to_nickels
#     return [coins, remainder]

# def coins_in_pennies(gross, amount_to_pennies):
#     coins = gross % amount_to_pennies
#     remainder = gross // amount_to_pennies
#     return [coins, remainder]



# quarters = coins(pennies, quarter)
# print(quarters)
# print(quarters[1])#coins
# print(quarters[0])#remainder
# dimes = coins(quarters[0], dime)
# print(dimes)
# print(dimes[1])
# print(dimes[0])

# while True:
#     print("Welcome to the Change Maker 5000 ")
#     dollars = float(input("Enter amount: "))
#     pennies = dollars * 100
#     pennies = math.trunc(pennies)
#     quarters = coins(pennies, quarter)
#     dimes = coins(quarters[0], dime)
#     nickels = coins(dime[0], nickel)
#     pennys = coins(nickel[0], pennys)
#     print(f"Your change is:\n{quarters[1]} quartersn\ ")














def coins(gross, amount_to_quarters):
    coins = gross % amount_to_quarters
    remainder = gross // amount_to_quarters
    return [coins, remainder]


while True:
    try:
        dollars = float(input("Enter the amount you'd like to convert: "))
        cents = dollars * 100
        cents = math.trunc(cents)
            
        if cents <= 0:
            print("Please enter a number that's greater than 0")
        elif cents > 0:

            quarters = coins(cents, 25)
            dime = coins(quarters[0], 10)
            nickel = coins(dime[0], 5)
            penny = coins(nickel[0], 1)
            print(f'Your total in change is:\nQuarters: {quarters[1]}\nDimes: {dime[1]}\nNickels: {nickel[1]}\nPennies: {penny[1]}')
    except:
        print("Please make sure you ONLY input intergers\nFor example (1.10, 3.50, 5 etc...)")
    continue_exit = input("Would you like to continue?\nEnter 'no' to exit OR 'yes' to convert\n")
    if continue_exit == 'no':
        print("Okay, thanks for your time")
        break
    elif continue_exit != 'no':
       
            
            

    

        
    




        
        
    
    
    
    

#keep going


   



                
            







