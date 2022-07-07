# Lab 3: Number to Phrase
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.

# x = 67
# tens_digit = x//10
# ones_digit = x%10
# Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

# Version 2
# Handle numbers from 100-999.

# Version 3 (optional)
# Convert a number to roman numerals.

# Version 4 (optional)
# Convert a time given in hours and minutes to a phrase.
#===================================================================================

import numbers


# tens_digit = x//10
# ones_digit = x%10
onesNumberList = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine", 
}
tensNumberList = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "ninteen",
    2: "twenty",
    3: "thirty",
    4: "fory",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninty",
}

pickANumber = input("Pick a number between 0 and 99: ")
tens_digit = int(pickANumber)//10
ones_digit = int(pickANumber)%10
actual_digit = (f"{tens_digit}{ones_digit}")
# print(f"{tens_digit}{ones_digit}")
# print(actual_digit)

# if int(pickANumber) > 99:
#         print(f"Number is too high")
# elif int(pickANumber) < 0:
#         print(f"Number is too low")
for num in pickANumber:
    if actual_digit[0] == 0:
        print(f"{onesNumberList[1]}")
    
    # else:
    #     print(f"")













