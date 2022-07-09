#Matt Nichols
#HB2 Lab03

#Version 1

#Dictionaries for future key[input] to output
ones_place = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}
complex_place = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}
tens_place = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninty'
}

#Function for when you need to pull from two keys with one input
def twenty_to_ninty_nine(nums):
    tens = nums // 10
    ones = nums % 10
    if ones == 0:
        return tens_place[tens]
    return '{0}-{1}'.format(tens_place[tens], ones_place[ones])

#Function for putting the everything together
def zero_to_ninty_nine(nums):
    if nums < 10:
        return ones_place[nums]
    elif nums < 20:
        return complex_place[nums]
    return twenty_to_ninty_nine(nums)

#Version2

#Function for finding/pulling more keys with one input
def hundreds(nums):
    hundreds = nums // 100
    tens = nums % 100
    ones = nums % 10
    if tens == 0:
        return f'{ones_place[hundreds]}-hundred'
    if tens < 10:
        return f'{ones_place[hundreds]}-hundred-{ones_place[ones]}'
    if tens < 20:
        return f'{ones_place[hundreds]}-hundred-{complex_place[tens]}'
    return f'{ones_place[hundreds]}-hundred-{twenty_to_ninty_nine(tens)}'

#Putting it all together
def numbers_zero_to_hundreds(nums):
    if nums < 10:
        return ones_place[nums]
    if nums < 20:
        return complex_place[nums]
    if nums < 100:
        return twenty_to_ninty_nine(nums)
    return hundreds(nums)


while True:
    user_input = input("Enter a number between 0-999 OR type 'done' to exit\n")
    #Ending program
    if user_input == 'done':
        result = "Goodbye"
        print(result)
        break
    #For users invalid input
    try:
        number_to_string = numbers_zero_to_hundreds(int(user_input))
        print(number_to_string)
    except:
        print(f"You entered - {user_input}.\nMake sure you have no spaces, numbers don't exceed 999, and no negatives ")

 