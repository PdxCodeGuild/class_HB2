# Lab 7: Credit Card Validation

# Let's write a function credit_card_validator which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

#     Convert the input string into a list of ints
#     Slice off the last digit. That is the check digit.
#     Reverse the digits.
#     Double every other element in the reversed list (starting with the first number in the list).
#     Subtract nine from numbers over nine.
#     Sum all values.
#     Take the second digit of that sum.
#     If that matches the check digit, the whole card number is valid.

# Here is a valid credit card number to test with: 4556737586899855

# For example, the worked out steps would be:

#     4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
#     4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
#     5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
#     10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
#     1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
#     85
#     5
#     True Valid!
# ========================================================================================


enter_ccn = (input("Enter your 16-digit credit card number: "))
# print(len(enter_ccn))


try:
    len(enter_ccn) == 16
    enter_ccn = list(enter_ccn)
    print(enter_ccn)
    # print("check")
except (ValueError):
    print("Invalid number length, try again")
    print(enter_ccn)
except (ValueError):
    print('Please enter a number')
# ====================================================
# Convert the input string into a list of ints
# ====================================================
# print(enter_ccn)
# print(type(enter_ccn))

# ====================================================
# Slice off the last digit. That is the check digit.
# ====================================================
check_digit = enter_ccn.pop()
print(check_digit)

# ====================================================
# Reverse the digits.
# ====================================================
enter_ccn.reverse()
print(enter_ccn)

# =============================================================================================
# Double every other element in the reversed list (starting with the first number in the list).
# =============================================================================================

index = 0
ccn_odd_doubled = []
for odd in enter_ccn:    
        if int(enter_ccn[index]) % 2 != 0:
            ccn_odd_doubled.append(int(enter_ccn[index]) * 2)
            index += 1
        else:
            ccn_odd_doubled.append(int(enter_ccn[index]))
            index += 1
print(ccn_odd_doubled)


# ====================================================
# Subtract nine from numbers over nine.
# ====================================================
index = 0
for num in ccn_odd_doubled:
    if ccn_odd_doubled[index] >= 9:
        ccn_odd_doubled.pop(index)
        index += 1
print(ccn_odd_doubled)
# ====================================================
# Sum all values.
# ====================================================
index = 0
sum_ccn = 0
for num in ccn_odd_doubled:
    sum_ccn += ccn_odd_doubled[index]
    index += 1
print(sum_ccn)

# ====================================================
# Take the second digit of that sum.
# ====================================================
index = 1
second_digit = list(map(int, str(sum_ccn)))
# print(str(second_digit))
print(second_digit[index])


# ====================================================
# If that matches the check digit, the whole card number is valid.
# ====================================================

if check_digit == second_digit[index]:
    print("True Valid!")
else:
    print("False, check digit not valid")