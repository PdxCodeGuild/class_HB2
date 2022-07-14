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
    101: "one hundred one",
    102: "one hundred two",
    103: "one hundred three",
    104: "one hundred four",
    105: "one hundred five",
    106: "one hundred six",
    107: "one hundred seven",
    108: "one hundred eight",
    109: "one hundred nine", 
    110: "one hundred ten",
    111: "one hundred eleven",
    112: "one hundred twelve",
    113: "one hundred thirteen",
    114: "one hundred fourteen",
    115: "one hundred fifteen",
    116: "one hundred sixteen",
    117: "one hundred seventeen",
    118: "one hundred eighteen",
    119: "one hundred ninteen",
    120: "one hundred twenty",
    130: "one hundred thirty",
    140: "one hundred forty",
    150: "one hundred fifty",
    160: "one hundred sixty",
    170: "one hundred seventy",
    180: "one hundred eighty",
    190: "one hundred ninty",
    201: "two hundred one",
    202: "two hundred two",
    203: "two hundred three",
    204: "two hundred four",
    205: "two hundred five",
    206: "two hundred six",
    207: "two hundred seven",
    208: "two hundred eight",
    209: "two hundred nine", 
    210: "two hundred ten",
    211: "two hundred eleven",
    212: "two hundred twelve",
    213: "two hundred thirteen",
    214: "two hundred fourteen",
    215: "two hundred fifteen",
    216: "two hundred sixteen",
    217: "two hundred seventeen",
    218: "two hundred eighteen",
    219: "two hundred ninteen",
    220: "two hundred twenty",
    230: "two hundred thirty",
    240: "two hundred forty",
    250: "two hundred fifty",
    260: "two hundred sixty",
    270: "two hundred seventy",
    280: "two hundred eighty",
    290: "two hundred ninty",
    301: "three hundred one",
    302: "three hundred two",
    303: "three hundred three",
    304: "three hundred four",
    305: "three hundred five",
    306: "three hundred six",
    307: "three hundred seven",
    308: "three hundred eight",
    309: "three hundred nine", 
    310: "three hundred ten",
    311: "three hundred eleven",
    312: "three hundred twelve",
    313: "three hundred thirteen",
    314: "three hundred fourteen",
    315: "three hundred fifteen",
    316: "three hundred sixteen",
    317: "three hundred seventeen",
    318: "three hundred eighteen",
    319: "three hundred ninteen",
    320: "three hundred twenty",
    330: "three hundred thirty",
    340: "three hundred forty",
    350: "three hundred fifty",
    360: "three hundred sixty",
    370: "three hundred seventy",
    380: "three hundred eighty",
    390: "three hundred ninty",
    401: "four hundred one",
    402: "four hundred two",
    403: "four hundred three",
    404: "four hundred four",
    405: "four hundred five",
    406: "four hundred six",
    407: "four hundred seven",
    408: "four hundred eight",
    409: "four hundred nine", 
    410: "four hundred ten",
    411: "four hundred eleven",
    412: "four hundred twelve",
    413: "four hundred thirteen",
    414: "four hundred fourteen",
    415: "four hundred fifteen",
    416: "four hundred sixteen",
    417: "four hundred seventeen",
    418: "four hundred eighteen",
    419: "four hundred ninteen",
    420: "four hundred twenty",
    430: "four hundred thirty",
    440: "four hundred forty",
    450: "four hundred fifty",
    460: "four hundred sixty",
    470: "four hundred seventy",
    480: "four hundred eighty",
    490: "four hundred ninty",
    501: "five hundred one",
    502: "five hundred two",
    503: "five hundred three",
    504: "five hundred four",
    505: "five hundred five",
    506: "five hundred six",
    507: "five hundred seven",
    508: "five hundred eight",
    509: "five hundred nine", 
    510: "five hundred ten",
    511: "five hundred eleven",
    512: "five hundred twelve",
    513: "five hundred thirteen",
    514: "five hundred fourteen",
    515: "five hundred fifteen",
    516: "five hundred sixteen",
    517: "five hundred seventeen",
    518: "five hundred eighteen",
    519: "five hundred ninteen",
    520: "five hundred twenty",
    530: "five hundred thirty",
    540: "five hundred forty",
    550: "five hundred fifty",
    560: "five hundred sixty",
    570: "five hundred seventy",
    580: "five hundred eighty",
    590: "five hundred ninty",
    601: "six hundred one",
    602: "six hundred two",
    603: "six hundred three",
    604: "six hundred four",
    605: "six hundred five",
    606: "six hundred six",
    607: "six hundred seven",
    608: "six hundred eight",
    609: "six hundred nine", 
    610: "six hundred ten",
    611: "six hundred eleven",
    612: "six hundred twelve",
    613: "six hundred thirteen",
    614: "six hundred fourteen",
    615: "six hundred fifteen",
    616: "six hundred sixteen",
    617: "six hundred seventeen",
    618: "six hundred eighteen",
    619: "six hundred ninteen",
    620: "six hundred twenty",
    630: "six hundred thirty",
    640: "six hundred forty",
    650: "six hundred fifty",
    660: "six hundred sixty",
    670: "six hundred seventy",
    680: "six hundred eighty",
    690: "six hundred ninty",
    701: "seven hundred one",
    702: "seven hundred two",
    703: "seven hundred three",
    704: "seven hundred four",
    705: "seven hundred five",
    706: "seven hundred six",
    707: "seven hundred seven",
    708: "seven hundred eight",
    709: "seven hundred nine", 
    710: "seven hundred ten",
    711: "seven hundred eleven",
    712: "seven hundred twelve",
    713: "seven hundred thirteen",
    714: "seven hundred fourteen",
    715: "seven hundred fifteen",
    716: "seven hundred sixteen",
    717: "seven hundred seventeen",
    718: "seven hundred eighteen",
    719: "seven hundred ninteen",
    720: "seven hundred twenty",
    730: "seven hundred thirty",
    740: "seven hundred forty",
    750: "seven hundred fifty",
    760: "seven hundred sixty",
    770: "seven hundred seventy",
    780: "seven hundred eighty",
    790: "seven hundred ninty",
    801: "eight hundred one",
    802: "eight hundred two",
    803: "eight hundred three",
    804: "eight hundred four",
    805: "eight hundred five",
    806: "eight hundred six",
    807: "eight hundred seven",
    808: "eight hundred eight",
    809: "eight hundred nine", 
    810: "eight hundred ten",
    811: "eight hundred eleven",
    812: "eight hundred twelve",
    813: "eight hundred thirteen",
    814: "eight hundred fourteen",
    815: "eight hundred fifteen",
    816: "eight hundred sixteen",
    817: "eight hundred seventeen",
    818: "eight hundred eighteen",
    819: "eight hundred ninteen",
    820: "eight hundred twenty",
    830: "eight hundred thirty",
    840: "eight hundred forty",
    850: "eight hundred fifty",
    860: "eight hundred sixty",
    870: "eight hundred seventy",
    880: "eight hundred eighty",
    890: "eight hundred ninty",
    901: "nine hundred one",
    902: "nine hundred two",
    903: "nine hundred three",
    904: "nine hundred four",
    905: "nine hundred five",
    906: "nine hundred six",
    907: "nine hundred seven",
    908: "nine hundred eight",
    909: "nine hundred nine", 
    910: "nine hundred ten",
    911: "nine hundred eleven",
    912: "nine hundred twelve",
    913: "nine hundred thirteen",
    914: "nine hundred fourteen",
    915: "nine hundred fifteen",
    916: "nine hundred sixteen",
    917: "nine hundred seventeen",
    918: "nine hundred eighteen",
    919: "nine hundred ninteen",
    920: "nine hundred twenty",
    930: "nine hundred thirty",
    940: "nine hundred forty",
    950: "nine hundred fifty",
    960: "nine hundred sixty",
    970: "nine hundred seventy",
    980: "nine hundred eighty",
    990: "nine hundred ninty",

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
    tens_digit = intNum // 10
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
    elif intNum not in number_list and intNum < 100: 
        print(str(number_list[tens_digit * 10] + "-" + number_list[ones_digit]))
        break
    else:
        print(str(number_list[hundred_digit * 100] + " " + (number_list[tens_digit_mod * 10] + "-" + number_list[ones_digit])))
        break


