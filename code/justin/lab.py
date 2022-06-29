'''
Justin Young
Lab 00
Version 1
'''

nums = [5, 0, 8, 3, 4, 1, 6]

x = len(nums)

'''this pops the first number in the list x2 then attempts to turn them into integers to add together, then takes the sum and places it at the end of the list'''
while len(nums) > 1:  
    p1 = int(nums.pop(0))
    p2 = int(nums.pop(0))
    sum = p1 + p2
    nums.append(sum)

'''this pops the final number, or sum of the list and attempts to turn in into an integer'''
nums = int(nums.pop(0))
print(nums, type(nums))
print(x, type(x))


'''this takes the sum of the list and divides it by the original list length for the average of the numbers'''
avg = nums / x
print(avg)


'''
Version 2
'''


user_list = []
user_num = input('Enter a single number or "done" when finished.')

if user_num.isnumeric() is True:
    print(user_num)