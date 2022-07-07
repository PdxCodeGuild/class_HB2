# def get_greeting(name):
#     return f"Good evening {name}"
# message = get_greeting('kathy')
# file = open('get_greeting.txt', 'w')
# file.write(message)
# file.close

# def increments(number, by):
#     return number + by

# result = increments(3, 1)
# print(result)

# def increments(number, by=1):
#     return number + by
# print(increments(2))

# def increments(number, by=1):
#     return number + by
# print(increments(2, 13)) #overwrites the by=1

# def increments(num1 =1, num2 =1 ):
#     return num2 + num1
# print(increments(num2= 5, num1 = 13)) 

#tuple
# def multiply(*nums):
#     print(nums)
# print(multiply(2, 4, 6, 8)) 

# def multiply(*nums):
#     for n in nums:
#     print(n)

# print(multiply(2, 4, 6, 8)) 


# x = 67
# test_digit = x / 10


# # print(test_digit)
# print(tens_digit)
# print(ones_digit)

# low_numbers = { 
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: 'nine',
#     10: 'ten',
#     11: 'eleven',
#     12: 'tweleve',
#     13: 'thirty',
#     14: 'fourteen',
#     15: 'fifteen',
#     16: 'sixteen',
#     17: 'seventeen',
#     18: 'eighteen',
#     19: 'nineteen'

# }

# ten = {
#     2: "twenty",
#     3: "thirty",
#     4: "forty",
#     5: "fifty",
#     6: "sixty",
#     7: "seventy",
#     8: "eighty",
#     9: "nintey"
#     }
# # print(low_numbers[3])

# def convert_number(number):
#     # return number]
#     if number < 20:
#         return low_numbers[number]
#     elif number <  100:
        
    
#         tens_digit = number//10
#         ones_digit = number%10
#     return f"{ten[tens_digit]} - {low_numbers[ones_digit]}"


# print(convert_number(67))
from hashlib import new


low_numbers = { 
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'tweleve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'

}

ten = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "nintey"
    }

hundreds = {
    1: "one hundred",
    2: "two hundred",
    3: "three hundred",
    4:'four hundred',
    5:'five hundred',
    6:'six hundred',
    7:'seven hundred',
    8:'eight hundred',
    9:'nine hundred'
    
}
# print(low_numbers[3])

def convert_number(number):
    # return number]
    if number < 20:
        return low_numbers[number]
   
    elif number <  100:
        
        tens_digit = number // 10
        # print('10s digit: ', tens_digit)
        ones_digit = number % 10 #takes whatever number and divides that by 10 and then gives the remainder
        # print('1s digit: ', ones_digit)
    # return f"{ten[tens_digit]} - {low_numbers[ones_digit]}" 
        tens_word = ten[tens_digit]
        ones_word = low_numbers[ones_digit]
        return f'{tens_word + " " + ones_word}'


    elif number < 999:
        
        hundreds_digit = number // 100 #floor divide regular division with no remainder
        tens_digit = number // 10 
        new_tens = tens_digit % 10
        ones_digit = number % 10
        hundreds_word = hundreds[hundreds_digit]
        tens_word = ten[new_tens]
        ones_word = low_numbers[ones_digit]
        return f'{hundreds_word + " " + tens_word + " " + ones_word}'    
        # return hundreds_digit, tens_digit
    # return f"{hundreds[hundreds_digit]} - {ten[tens_digit]} - {low_numbers[ones_digit]}"

print(convert_number(532))

print(convert_number(111))
print(convert_number(813))
print(convert_number(140))


