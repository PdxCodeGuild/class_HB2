#Matt Nichols
#HB2 Lab01

#Version 1

#Default list that was given
nums = [5, 0, 8, 3, 4, 1, 6]
total = 0

#For loop for running through the list and getting a 'running sum'
for num in range(len(nums)):
    running_sum = nums[num]
    total = total + running_sum
    print(total)

#Finding the mean   
mean = total / len(nums)
print(f'{mean} is the mean')

#Version 2

#Def function for summing numbers in a list
def sum(nums):
    total = 0
    for num in range(len(nums)):
        nums_in_list = nums[num]
        total = total + nums_in_list
    return total

#Def function for user input
def user_input():
    user = input("Enter a number (Make sure there are no spaces)\nType 'done' to exit\n")
    return user

#Empty list for sum function
empty_list = []

#While loop to take and add the user input to find their running sum
while True:

#For when the user wants to exit the program 
    response = user_input()
    if response == 'done':
        result = "Okay, thank you for your time "
        print(result)
        break

#To add numbers to the empty list and calculate their sum OR to tell them the input was invalid
    try:
        empty_list.append(float(response))
        added = sum(empty_list)
        print(added)
    except:
        print("Sorry, that wasn't readable. Please make sure you type what is prescribed below. ")
    
#If statement catching zero input from user, as well as giving them their total/mean if they do give give valuable input    
if len(empty_list) == 0:
    print("Mean = N/A")
else:
    print(f'Your total is {added}. {added} divided by {len(empty_list)} is equal to {added / len(empty_list)} ')