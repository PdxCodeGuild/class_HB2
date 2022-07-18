# Here is a valid credit card number to test with: 4556737586899855

# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# True Valid!

# Let's write a function credit_card_validator which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:


def credit_card_validator(credit_card_number):

    # Convert the input string into a list of ints

    input_list = list(credit_card_number)

    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])

    print(input_list)
    # Slice off the last digit. That is the check digit.

    check_digit = input_list.pop(-1)
    # print(check_digit)
    print(input_list)
    # Reverse the digits.
    input_list.reverse()
    print(input_list)

    # Double every other element in the reversed list (starting with the first number in the list).

    doubled_list = input_list

    for i in range(len(doubled_list)):
        if i % 2 == 0:
            doubled_list[i] = (doubled_list[i]) * 2
        else:
            doubled_list[i] = doubled_list[i]
    print(doubled_list)

    # Subtract nine from numbers over nine.

    subtract_nine = doubled_list

    for i in range(len(subtract_nine)):

        if (subtract_nine[i]) > 9:
            subtract_nine[i] = (subtract_nine[i]) - 9

    print(subtract_nine)

    # Sum all values.
    sum_values = str(sum(subtract_nine))
    print(sum_values)

    # Take the second digit of that sum.
    second_digit = sum_values[1]
    print(second_digit)
    # If that matches the check digit, the whole card number is valid.
    answer = second_digit == check_digit
    # Return a boolean

    return answer


print(credit_card_validator("4556737586899855"))
