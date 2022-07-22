def quarters(amount): 
    """
    Quarters takes an amount argument and calculates the number of quarters in that amount. 
    It then returns the number of quarters and any remainder as a float.
    """
    quarters = amount // 25
    quarters_remainder = amount - quarters * 25
    print(quarters_remainder)
    return quarters, quarters_remainder

def dimes(amount): 
    """
    Dimes takes an amount argument and calculates the number of dimes in that amount. 
    It then returns the number of dimes and any remainder as a float.
    """
    dimes = amount // 10
    dimes_remainder = amount % 10
    
    return dimes, dimes_remainder

def nickels(amount): 
    """
    Nickels takes an amount argument and calculates the number of nickels in that amount. 
    It then returns the number of nickels and any remainder as a float.
    """
    nickels = amount // 5
    nickels_remainder = amount % 5
    
    return nickels, nickels_remainder

def pennies(amount): 
    """
    Pennies takes an amount argument and calculates the number of pennies in that amount. 
    It then returns the number of pennies and any remainder as a float.
    """
    pennies = amount / 1
    
    return pennies

def main():
    answer = "Yes"

    while answer != "no":
        amount = float(input("Enter a dollar amount: "))
        print(amount)
        amount = int(round(amount * 100))
        print(amount)

        quarter, quarter_remainder = quarters(amount)
        dime, dime_remainder = dimes(quarter_remainder)
        nickel, nickel_remainder = nickels(dime_remainder)
        penny = int(pennies(nickel_remainder))

        print(f'{quarter} quarters, {dime} dimes, {nickel} nickels, and {penny} pennies')
        
        answer = input("Would you like to make more change? ")
        
    return answer

main()