def credit_card_input():
    """Takes credit card number as user input and returns as a string."""
    #user_input = input("Enter a valid 16 digit credit card number: ")
    user_input = "4556737586899854"
    return user_input

def credit_card_input_validation(user_input):
    """"Takes the output from credit_card_input() and first checks if the input was 16 characters. Then converts number as string to a list of ints."""
    
    if len(user_input) != 16:
        print(f'{user_input} is not a valid card number. Please validate your card number and try again.')
        main()
    else:
        card_as_list = []

        for char in user_input:
            card_as_list.append(int(char))
    
    return card_as_list

def reverse_list(card_as_list):
    """Takes the output from credit_card_input_validation() and reverses the list of ints."""
    reversed_list = []
    index = -1
    
    for num in card_as_list:
        reversed_list.append(card_as_list[index])
        index -= 1
    
    return reversed_list

def double_every_other_number(reversed_list):
    """Takes a list of ints and doubles every other number."""
    index = 0
    doubled_list = reversed_list

    while index < len(doubled_list):
        doubled_list[index] *= 2
        index += 2

    return doubled_list

def subtract_nine(doubled_list):
    """If number is greater than nine, subtract nine."""
    nine_diff_list = doubled_list
    index = 0

    while index < len(nine_diff_list):
        if nine_diff_list[index] > 9:
            nine_diff_list[index] -= 9
            index += 1
        else: 
            index +=1

    return nine_diff_list

def validate_check_digits(check_digit1, check_digit2):
    """If the two inputs equal, returns True else returns False."""
    if check_digit1 == check_digit2:
        return "Card Valid"
    else:
        return "Card Invalid"

#def print_result(check_digit1, check_digit2):
#    if evaluate_check_digit(check_digit1, check_digit2):
#        print("Test1")
#    else: 
#        print("Test2")

def main():
    
    user_input = credit_card_input()
    print(user_input)
    
    card_as_list = credit_card_input_validation(user_input)
    print(card_as_list)
    
    check_digit1 = card_as_list.pop()
    print(check_digit1)
    
    reversed_list = reverse_list(card_as_list)
    print(reversed_list)
    
    doubled_list = double_every_other_number(reversed_list)
    print(doubled_list)
    
    nine_diff_list = subtract_nine(doubled_list)
    print(nine_diff_list)
    
    check_digit2 = int(str(sum(nine_diff_list))[-1])
    print(check_digit2)
    
    test_var = validate_check_digits(check_digit1, check_digit2)
    print(test_var)
    
main()