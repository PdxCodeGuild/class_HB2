# Kelin Ray

# Lab 7: Credit Card Validation


# Let's write a function `credit_card_validator` which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

# 1. Convert the input string into a list of ints

import math

cardnum = int(input('Enter a credit card number: '))
numlist = [int(index) for index in str(cardnum)] # Input string converted to list of integers

# 2. Slice off the last digit.  That is the **check digit**.

numlist.pop() # Getting check digit
print(numlist)

# 3. Reverse the digits.

newnumlist = numlist[:] # Getting copy of sliced list
newnumlist.reverse() # Reversing the numbers
print(newnumlist)

# 4. Double every other element in the reversed list (starting with the first number in the list).

reversednums = newnumlist[:] # Copy of reversed list

doubleelements = reversednums[:]
doubleelements[::2] = [index * 2 for index in reversednums[::2]] # Doubled elements in reversed list
print(doubleelements)

# 5. Subtract nine from numbers over nine.

subtract = doubleelements[:]
def subtract9(value):
    if value > 9:
        return value - 9
    return value
subtract = [subtract9(index) for index in subtract] # 9 subtracted if over
print(subtract)

# 6. Sum all values.

subtract9list = subtract[:]
sumnums = sum(subtract) # Gets sum of values from subtracted list
print(sumnums)

# 7. Take the second digit of that sum.

validnumber = sumnums
sumnums = [int(index) for index in str(sumnums)] # Gets validating number

validated = numlist.pop() # Pulling the check digit
validated = int(validated)

if validated == validnumber[-1]:
        print("Valid credit card")
else:
        print("Invalid card")

# 8. If that matches the check digit, the whole card number is valid.

# Here is a valid credit card number to test with: 4556737586899855

# For example, the worked out steps would be:

# 1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
# 2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
# 3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
# 4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
# 5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
# 6. 85
# 7. 5
# 8. `True` Valid!
