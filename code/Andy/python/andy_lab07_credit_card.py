

def credit_card_validator(card):
    temp_list = []
    for i in card:
        i = int(i)
        temp_list.append(i)
        # print(temp_list)
    print(temp_list)     


    check_digit = temp_list[:-1]#list comprehension cutting out last number 
    print(check_digit)
    check_digit = check_digit[:: -1]
    print(check_digit) #reversing numbers 

    check_digit[::2]= [i *2 for i in check_digit[::2]] #multiplying the second digit
    print(check_digit)
    for i, item in enumerate(check_digit): #enumerate takes a tuple and helps you loop through them using check_digit since thats where my numbers left off on 
        if item > 9:        #item is just what i put honestly dont fully understand the enumerate look into more
            check_digit[i] = item - 9 #in the enumerate "i" is the index of the numbers and item is the whats in that space 
    print(check_digit)
    check_digit = sum(check_digit)
    print(check_digit)
    check_digit =  check_digit % 10
    print(check_digit)
    if check_digit == temp_list.pop(-1):
         # also removes the number you want to take out but shows it aswell 
        return f'{True}Valid!'
    else:
        return f'{False} Not Valid!'
user = input('Enter credit card number: ')
print(credit_card_validator(user))


#