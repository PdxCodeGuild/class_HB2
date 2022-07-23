def change():
    print("Welcome to the Change Maker 5000 (tm)")
    dollar_amount = input("\nEnter a dollar amount without the dollar sign (e.g. 1.50):  ")
    x = float(dollar_amount)
    cents = int(x * 100)
    quarters = cents // 25
    change_1 = cents - (quarters * 25)
    dimes = change_1 // 10
    change_2 = cents - (quarters * 25) - (dimes * 10)
    nickels = change_2 // 5
    change_3 = cents - (quarters * 25) - (dimes * 10) - (nickels * 5)
    pennies = change_3
    message = ""
    if quarters > 0:
        message = message + str(quarters) + " quarters"
    if dimes > 0:
        message = message + " " + str(dimes) + " dimes"
    if nickels > 0:
        message = message + " " + str(nickels) + " nickels"
    if pennies > 0:
        message = message + " " + str(pennies) + " pennies"
    print(message)

while True:
    change()
    
    cont = input("Would you like make more change? (yes or no):  ")

    while cont.lower() not in ("yes", "no"):
        cont = input("Would you like make more change? (yes or no):  ")

    if cont == "no":
        print("Have a good day!")
        break

