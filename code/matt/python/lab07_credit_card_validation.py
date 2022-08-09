'''Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list (starting with the first number in the list).
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
Here is a valid credit card number to test with: 4556737586899855

For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
True Valid!'''
import math
def user_nums():

    while True:
        num = int(input("Please enter the 16 digits of your card"))
        if num == int:
            return num
        print("Invalid input. Make sure you only enter numbers (0-9)")

try: 
    num = int(input("Please enter the 16 digits of your card: "))
    
    #num = 4556737586899855


    num_list = [int(index) for index in str(num)]
    #print(num_list)
    #This takes the numbers someone will input and convert it into a list. Below is an example
    #[4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

    num_list.pop()
    #print(num_list)
    #We are now taking the last number from the list and removing it/using it for a boolean value. below is an example
    #[4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5]

    num_list_copy = num_list[:]
    #print(num_list_copy)
    #We are now making a copy of the list with the popped value so that we can start to reverse it. Below is an example
    #[4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5]

    num_list_copy.reverse()
    #print(num_list_copy)
    #We are now reversing the list with the copied list so that we can make another copy of this current list. Below is an example
    #[5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4]

    reversed_list = num_list_copy[:]
    #print(reversed_list)
    #We have now taken the copied list that's in reverse and put it into a new list called reversed_list. Below is an example
    #[5, 8, 9, 9, 8, 6, 8, 5, 7, 3, 7, 6, 5, 5, 4]

    reversed_and_double = reversed_list[:]
    reversed_and_double[::2] = [index * 2 for index in reversed_list[::2]]
    #print(reversed_and_double)
    #We are now pulling every other index (starting at 0 and times it by 2). Below is an example
    #[10, 8, 18, 9, 16, 6, 16, 5, 14, 3, 14, 6, 10, 5, 8]

    subtract_9 = reversed_and_double[:]
    def subtract_9_if_over(value):
        if value > 9:
            return value - 9 
        return value    
    subtract_9 = [subtract_9_if_over(index) for index in subtract_9]
    #print(subtract_9)
    #We are now taking creating a function to plug into list comprehension to subtract 9 from every digit that is greater than 9. Below is an example
    #[1, 8, 9, 9, 7, 6, 7, 5, 5, 3, 5, 6, 1, 5, 8]

    subtract_9_copy = subtract_9[:]
    sum_of_numbers = sum(subtract_9_copy)
    #print(sum_of_numbers)
    #We now have all we need to gather the sum. Below is an example
    #85

    last_digit = sum_of_numbers
    last_digit = [int(index) for index in str(last_digit)]
    #print(last_digit)
    #I'm now creating another list so that we can pull the last value and compare it to the popped value. Below is an example
    #[8, 5]

    popped = num_list.pop()
    #print(popped)
    #Now I'm pulling the popped num from our original list. Below is an example
    #5

    if popped == last_digit[-1]:
        print("VALID")
    else:
        print("NOT VALID")
except:
    print("Make sure that you ONLY put numbers in.")
