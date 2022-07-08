# Lab 3: Number to Phrase
# Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Hint: you can use modulus to extract the ones and tens digit.

# x = 67
# tens_digit = x//10
# ones_digit = x%10
# Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.


one = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
    }

teen = {
    '10':'ten',
    '11':'eleven',
    '12':'twelve',
    '13':'thirteen',
    '14':'fourteen',
    '15':'fifteen',
    '16':'sixteen',
    '17':'seventeen',
    '18':'eighteen',
    '19':'nineteen',
    }

ten = {
    '2':'twenty',
    '3':'thirty',
    '4':'forty',
    '5':'fifty',
    '6':'sixy',
    '7':'seventy',
    '8':'eighty',
    '9':'ninety',
    }

num = input("Enter a number between 0 and 99: ")
ones = int(num)%10
teens = int(num)
tens = int(num)//10
user_num = int(num)

if user_num == 0:
    print('zero')

elif user_num < 10:
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_ones)

elif user_num in range (10, 20):
    teens_phrase = str(teens)
    num_phrase_teens = teen[teens_phrase]
    print(num_phrase_teens)

elif user_num in range (20, 100):
    tens_phrase = str(tens)
    num_phrase_tens = ten[tens_phrase]
    ones_phrase = str(ones)
    num_phrase_ones = one[ones_phrase]
    print(num_phrase_tens,num_phrase_ones)

# Version 2
# Handle numbers from 100-999.

# Version 3 (optional)
# Convert a number to roman numerals.

# Version 4 (optional)
# Convert a time given in hours and minutes to a phrase.

