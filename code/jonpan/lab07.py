#Lab07 Credit Card Validator

def credit_card_validator(credit_card_number):
    
    #Convert the input string into a list of ints

    cc_to_list = list(credit_card_number)

    for i in range(len(cc_to_list)):
        cc_to_list[i] = int(cc_to_list[i])

    print(cc_to_list)

    # Slice off the last digit. That is the check digit.

    check_digit = cc_to_list.pop(-1)
    # print(check_digit)

    # Reverse the digits.

    reversed_list = cc_to_list[::-1]
    print(reversed_list)

    # Double every other element in the reversed list (starting with the first number in the list).

    # for i in range(0, len(reversed_list), 2):
    #     reversed_list[i] = int(reversed_list[i]) * 2
    #     print(reversed_list[i])

    double_list = []

    for i in range(len(reversed_list)):
        if i % 2 == 0:
            double_list.append(reversed_list[i] * 2)
        else:
            double_list.append(reversed_list[i])

    print(double_list)

    # Subtract nine from numbers over nine.

    subtract_list = []

    for i in range(len(double_list)):

        if (double_list[i]) > 9:
            subtract_list.append(double_list[i] - 9)
        else:
            subtract_list.append(double_list[i])

    print(subtract_list)

    # Sum all values.

    sumall = str(sum(subtract_list))

    print(sumall)
    
    # Take the second digit of that sum.

    second_digit = sumall[1]

    print(second_digit)

    # If that matches the check digit, the whole card number is valid.

    if second_digit == str(check_digit):
        print("Valid!")

print(credit_card_validator("4556737586899855"))