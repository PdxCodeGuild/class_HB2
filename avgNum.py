
nums = [5, 0, 8, 3, 4, 1, 6]
runningSum = 0

# loop over the elements
for num in nums:
    runningSum += num
    # print(runningSum)

avgNum = runningSum / len(nums)
print(avgNum)
