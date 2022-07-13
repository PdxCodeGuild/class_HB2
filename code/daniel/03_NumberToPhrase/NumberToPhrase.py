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



#====================================
#Version1
#====================================

# onesNumberList = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine", 
# }
# tensNumberList = {
#     10: "ten",
#     11: "eleven",
#     12: "twelve",
#     13: "thirteen",
#     14: "fourteen",
#     15: "fifteen",
#     16: "sixteen",
#     17: "seventeen",
#     18: "eighteen",
#     19: "ninteen",
#     20: "twenty",
#     30: "thirty",
#     40: "fory",
#     50: "fifty",
#     60: "sixty",
#     70: "seventy",
#     80: "eighty",
#     90: "ninty",
# }


# pickANumber = input("Pick a number between 0 and 99: ")
# intNum = int(pickANumber)
# tens_digit = intNum//10
# ones_digit = intNum%10
# # print(tens_digit)
# # print(ones_digit)


# while intNum > 99 or intNum < 0:
#         print(f"Number is out of range")
#         exit()

#     # print(onesNumberList.get(int(6)))
# while True:
#     if intNum in onesNumberList:
#         print(str(onesNumberList[intNum]))
#         break
#     elif intNum in tensNumberList:
#         print(str(tensNumberList[intNum]))
#         break
#     elif intNum not in onesNumberList and intNum not in tensNumberList:
#         # wordNum = tensNumberList[tens_digit * 10] + onesNumberList[ones_digit * 10]
#         print(str(tensNumberList[tens_digit * 10] + "-" + onesNumberList[ones_digit]))
#         break
 
#=======================================
#Version2
#=======================================

number_list = {
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
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninty",
    100: "one hundred",
    200: "two hundred",
    300: "three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred", 
}

pickANumber = input("Pick a number between 0 and 99: ")
intNum = int(pickANumber)
#========
#digits
#========
hundred_digit = intNum // 100
if intNum > 99:
    tens_digit = intNum % 100 // 10
    tens_digit_mod = tens_digit % 10
else:
    tens_digit = intNum // 100
    tens_digit_mod = 0
ones_digit = intNum % 10
#========
print(f"Hundred Digit: {hundred_digit}")
print(f"Tens Digit: {tens_digit}")
print(f"Tens Digit Mod: {tens_digit_mod}")
print(f"Ones Digit: {ones_digit}")


while intNum >= 1000 or intNum < 0:
        print(f"Number is out of range")
        exit()   
while True:
    if intNum in number_list:
        print(str(number_list[intNum]))
        break
    elif intNum not in number_list and intNum < 99: 
        print(str(number_list[tens_digit * 10] + "-" + number_list[ones_digit]))
        break
    elif intNum not in number_list and 100 <= intNum < 1000:
        tens_digit = intNum % 100 // 10
        ones_digit = intNum % 10
        print(str(number_list[hundred_digit * 100] + "-" (number_list[tens_digit])
        
        # break
    else:
        print(str(number_list[hundred_digit * 100] + " " + (number_list[tens_digit_mod * 10] + "-" + number_list[ones_digit])))
        break




 # hundreds = str(number_list[hundred_digit * 100])
        # newIntNum = intNum - (hundred_digit *100)
        # tens_digit = NewIntNum // 10
        # print(str(number_list[hundred_digit * 100] + " err " + (number_list[tens_digit_mod * 10] + "-" + number_list[ones_digit])))