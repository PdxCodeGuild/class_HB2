# ab 00: Average Numbers

# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

# The code below shows how to loop through an array, and prints the elements one at a time.

# nums = [5, 0, 8, 3, 4, 1, 6]
# runningSum = 0

# # loop over the elements
# for num in nums:
#     runningSum += num
#     # print(runningSum)

# avgNum = runningSum / len(nums)
# print(avgNum)



    
# # Version 2

# # Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.
# from cProfile import run


runningSum = 0
inputCount = 0
numList = []


lab1 = True
while lab1 == True:
    enterNum = input("Enter a number or type 'done' when finished: ")
    if enterNum != "done":
        try:
            enterNum = float(enterNum)
            numList.append(float(enterNum))
        except:
            print("Type a number")
    else:
        lab1 = False
for num in numList:
    runningSum += num
avgNum = runningSum / len(numList)
   
print(f"runningSum = {runningSum}, avgNum = {avgNum}")
print(numList)


