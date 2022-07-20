# VERSION 1

# nums = [5, 0, 8, 3, 4, 1, 6]

# # for num in nums:
# #    print(num)

# for i in range(len(nums)):
#     print(nums[i])

# print(sum(nums)/len(nums))

# VERSION 2

nums = []
x = 0

while x != 'done':
    x = input("\nEnter a number, or 'done':  ") 
    if x != 'done':
        nums.append(x)

int_nums = [int(i) for i in nums]

print(sum(int_nums)/len(int_nums))