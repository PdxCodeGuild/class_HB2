

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



#===========================================
pickANumber = input("Pick a number between 0 and 999: ")
intNum = int(pickANumber)

tens_digit = intNum % 100 // 10
tens_digit_mod = tens_digit % 10
ones_digit = intNum % 10

# three_digit_number = 875

# two_digit_number = 92

three_floor_100 = intNum // 100

three_mod_100 = intNum % 100

working_2_digit_num = three_mod_100

two_digit_floor_ten = working_2_digit_num // 10

two_digit_mod_ten = working_2_digit_num % 10


print("three_floor_100: ", three_floor_100)
print("three_mod_100: ", three_mod_100)
print("two_digit_floor_ten: ", two_digit_floor_ten)
print("two_digit_mod_ten: ", two_digit_mod_ten)
#===========================================



if intNum in number_list:
        print(str(number_list[intNum]))
elif intNum not in number_list and intNum < 100: 
        print(str(number_list[two_digit_floor_ten * 10] + "-" + number_list[two_digit_mod_ten]))
elif 100 < intNum < 1000 and three_mod_100 < 20:
        print(str(number_list[three_floor_100 * 100] + "-" + number_list[three_mod_100]))
elif 100 < intNum < 1000 and three_mod_100 > 20 and two_digit_mod_ten != 0:
        print(str(number_list[three_floor_100 * 100] + " " + (number_list[two_digit_floor_ten * 10] + "-" + number_list[two_digit_mod_ten])))
elif 100 < intNum < 1000 and three_mod_100 >= 20 and two_digit_mod_ten == 0:
        print(str(number_list[three_floor_100 * 100] + "-" + number_list[three_mod_100]))

