phrases = {
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
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def numbers_to_text(num):
    output = ''
    
    if 0 < num < 20:
        output = phrases[num]
        
    elif 20 < num < 100:
        tens_digit = num // 10
        ones_digit = num % 10
        
        if ones_digit != 0:
            output = phrases[tens_digit * 10] + '-' + phrases[ones_digit]
        else:
            output = phrases[tens_digit * 10]
            
    elif 100 <= num < 1000:
        hundreds_digit = num // 100
        tens_digit = ((num - (hundreds_digit * 100)) // 10)
        ones_digit = ((num - (hundreds_digit * 100)) % 10)
        
        if tens_digit != 0 and ones_digit != 0:
            output = phrases[hundreds_digit] + '-hundred ' + phrases[tens_digit * 10] + '-' + phrases[ones_digit]
        elif tens_digit != 0:
            output = phrases[hundreds_digit] + '-hundred ' + phrases[tens_digit * 10]
        elif ones_digit != 0: 
            output = phrases[hundreds_digit] + '-hundred ' + phrases[ones_digit]
        else: 
            output = phrases[hundreds_digit] + '-hundred '
    
    return print(output)
    
def main():
    numbers_to_text(0)
    numbers_to_text(1)
    numbers_to_text(10)
    numbers_to_text(19)
    numbers_to_text(99)
    numbers_to_text(100)
    numbers_to_text(101)
    numbers_to_text(110)
    numbers_to_text(199)
    
main()