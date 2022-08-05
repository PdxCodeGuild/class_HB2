# # Version 1
# nums = [5, 0, 8, 3, 4, 1, 6]

# total = 0

# for num in nums:
#         total = total + num

# average = total/(len(nums))
# print(average)


# for i in range(len(nums)):
#      print(nums[i])

# Version 2



nums = [] #place holder
sum = 0 # place to help when adding the num together and help get the average 

while True: #while statement to get all the numbers being put by the user
        user= input(' Please enter a number or done when finished: ')
        if user == 'done':
                break
        nums.append(int(user)) #strings dont add together for numbers, .append adding all the numbers in a list and the int making them into an integer.
        # print(nums)

for num in nums: #for statement helping me get the nums value of all the inputs and calling out single ones
        sum += num #where it calls the sigle ones and adds them together
        average = sum/ len(nums) #the len is getting the length of numbers so getting how many there is and the sum is getting the value of all the ones being put together and dividing them to get the average

print (f" Your total average is {round(average)} ")  #round removes the decimal and has to be within the curly bracket to have the function work
