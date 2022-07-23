# cents = int(float(input('Enter a dollar amount: ')) * 100)
#11 // 5--->2
# ◦ This example shows integer division. Any remainder is discarded.
# 11 % 5 --->1
# ◦ The computer divides 11 by 5 and returns the remainder (which is 1), not the quotient (which is 2). 
# ◦ The % is performing the "modulo operation"
# quarters = cents // 25 
# # change = cents % 25
# dimes = cents // 10
# # nickles = cents // 5
# print(f'{quarters} quarters and {dimes} dimes and ')




dollars = float(input('Enter a dollar amount: '))
print("dollars: ", dollars)
cents = dollars * 100 
# print('cents: ', cents)

quarters = int(cents // 25)  #you can highlight only to the end of the word and do a parenthesis and it'll do it on the whole thing 
print('quarters: ', quarters)
remainder = cents % 25 #getting what the varible is saying
# print('remainder:', remainder )

dimes = int(remainder // 10) #were getting the scapes from the last remainder and dividing it by 10
print('dimes:', dimes)
remainder = remainder % 10 #here we're getting the new leftovers for the next one 
# print('remainder: ', remainder)

nickles = int(remainder // 5)
print('nickles: ', nickles) 
remainder = remainder % 5 
# print("remainder: ", remainder)

pennys = int(remainder) 
print('pennys:', pennys)


