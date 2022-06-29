'''
Justin Young
Lab 00
Version 1
'''

nums = [5, 0, 8, 3, 4, 1, 6]
added = 0
counted = 0

for num in nums:
    added += num
for x in range(len(nums)):
    counted += 1

avg = added / counted
print(avg)