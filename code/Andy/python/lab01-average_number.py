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
nums = []



Done = True
while Done == True: 
        user = input('Please enter or a number or enter "done" : ')

        if user != Done:
                nums.append(int(user))
        
        else:
                Done = False

        
        
        
        
        # if user != Done:
        #         nums.append(int(user))
        
        # else:
        #         Done = False 

sum = 0 
for num in nums:
        sum += num

print(f' you entered {nums}')
print(f'the average is {sum/len(nums)}')
                
