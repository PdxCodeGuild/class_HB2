def quarters(amount):
    quarters = amount // 0.25
    quarters_remainder = round(amount - quarters * 0.25, 2)

    return quarters, quarters_remainder

def dimes(amount): 
    dimes = amount // 0.10
    dimes_remainder = round(amount - dimes * 0.10, 2)
    
    return dimes, dimes_remainder

def nickels(amount): 
    nickels = amount // 0.05
    nickels_remainder = round(amount - dimes * 0.05, 2)
    
    return nickels, nickels_remainder

def pennies(amount): 
    pennies = amount / 0.01
    
    return pennies

def main():
    answer = "Yes"

    while answer != "no":
        amount = float(input("Enter a dollar amount: "))
        
        print(dimes(amount))
        
        answer = input("Would you like to make more change? ")
        
main()