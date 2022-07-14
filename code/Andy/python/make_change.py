cents = int(float(input('Enter a dollar amount: ')) * 100)
#11 // 5--->2
# ◦ This example shows integer division. Any remainder is discarded.
# 11 % 5 --->1
# ◦ The computer divides 11 by 5 and returns the remainder (which is 1), not the quotient (which is 2). 
# ◦ The % is performing the "modulo operation"
quarters = cents // 25 
change = cents % 25
dimes = cents // 10
# nickles = cents // 5
print(f'{quarters} quarters and {dimes} dimes and ')


