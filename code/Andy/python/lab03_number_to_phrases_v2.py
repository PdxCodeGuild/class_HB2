#version 2 
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
enter = input('Please enter a number between 0 - 999 : ')

number = int(enter)

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
        hundreds_word = hundreds[hundreds_digit]
        last_two = int(str(number)[-2:]) #python get last two digits in number stack exchange
        last_one = int(str(number)[-1:])

            

        if last_two <=19: #catching all the numbers below 20
            return f'{hundreds_word + " " +low_numbers[last_two] }'  
    
        tens_digit = number // 10 
        new_tens = tens_digit % 10
        ones_digit = number % 10
        tens_word = ten[new_tens]
        ones_word = low_numbers[ones_digit]
        if last_one == 0:
            return f'{hundreds_word + " " + tens_word}' #placing this here to be able to get the numbers with 0 at the end, from having it say number then adding zero also placement beacause it needs to run all of that to be able to distinguish when it needs to use it 
            
        return f'{hundreds_word + " " + tens_word + " " + ones_word}'   

         
        # return hundreds_digit, tens_digit
    # return f"{hundreds[hundreds_digit]} - {ten[tens_digit]} - {low_numbers[ones_digit]}"

print(convert_number(number))

# print(convert_number(111))
# print(convert_number(813))
# print(convert_number(140))