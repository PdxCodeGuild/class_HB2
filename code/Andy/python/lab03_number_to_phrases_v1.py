#version 1

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
    13: 'thirty',
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
# # print(low_numbers[3])
enter = input('Please enter a number between 0 - 99 : ')

number = int(enter)

def convert_number(number):
    # return number]
    if number < 20:
        return low_numbers[number]
    elif number <  100:
        tens_digit = number//10
        ones_digit = number%10
        last_one = int(str(number)[-1:]) #calling the the last number that is being inputed
        if last_one == 0: # its saying that its only calling the last number if it is 0 
            return f'{ten[tens_digit]}' # once all those requirments are met it'll return the tens but what its doing is that it goes into the tens and then calling out the 10s digit it looks at the tens position of what was inputed and reads of the single digit 
    
        
    return f"{ten[tens_digit]} - {low_numbers[ones_digit]}"


print(convert_number(number))




