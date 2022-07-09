# def get_greeting(name):
#     return f'Good evening {name}'
# message = get_greeting('Vick')
# file = open('get_greeting.txt', 'a')
# file.write(message)
# file.close()


# def increment(num1=1, num2=1):
#     return num1 + num2
# print(increment(5, 13))


#results in Typeerror
# def multiply(*nums):
#     total = 1
#     for n in nums:
#         total *= n
#     return total


# print(multiply(2, 4, 6, 8))

# def repeat(quote, num):
#     print(quote * num)
    
# print(repeat(f'\nLive your best life', 5))

# def get_temp(temp):
#     if temp > 90:
#         return 'Hot'
#     elif temp > 75 and temp <= 90:
#         return 'Warm'
#     elif 60 <temp <= 75:
#         return 'Comfortable'
#     elif 45 <temp <= 60:
#         return 'Chilly'
#     else:
#         return 'Pack your parka'
    
# print(get_temp(40))


from cmath import e


number_words = {
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
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred"
    
}

try:
    number = int(input("Give a numerical number to convert to written English: "))
except:
    print("Must enter a number.")
    quit()




tens_digit = number//10
ones_digit = number%10
ten_column = int(str(tens_digit) + "0")

#       VERSION 2          #
hundreds_digit = number//100
hundreds_column = int(str(hundreds_digit) + "00")
tens_column2 = int(str(tens_digit%10) + "0")
tens_digit2 = tens_column2 + ones_digit

if number == 0:
    print("zero")
    
elif hundreds_digit > 0:
    if ones_digit == 0 and tens_column2 == 0:
        print(number_words[hundreds_digit] + "-hundred")
    elif ones_digit == 0:
        print(number_words[hundreds_digit] + "-hundred-" + number_words[tens_column2])
    elif tens_column2 < 10:
        print(number_words[hundreds_digit] + "-hundred-" + number_words[ones_digit])
    elif tens_column2 <20:
        print(number_words[hundreds_digit] + "-hundred-" + number_words[tens_digit2])
    
    else:
        print(number_words[hundreds_digit] + "-hundred-" + number_words[tens_column2] + "-" + number_words[ones_digit])
elif ones_digit == 0:
    print(number_words[ten_column])
elif number < 20:
    print(number_words[number])
else:
    print(number_words[ten_column] + "-" + number_words[ones_digit])
