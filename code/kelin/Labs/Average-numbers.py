# kelin-lab00-average-numbers

# Version 1

nums = [5, 0, 8, 3, 4, 1, 6]
x = sum(nums)
i = len(nums)
answer = (x / i)
print(answer)

# Prints Answer 3.857142857142857 Average of 5, 0, 8, 3, 4, 1, and 6

# Version 2

user_nums = []

while True:
    user = input("Enter numbers to average, and type 'done' to calculate: ")
    if user == "done":
        print((sum(user_nums)) / (len(user_nums)))
    else:
        user_nums.append(int(user))
        print(user_nums)

# User enters number and displays them in a list until they type 'done' and the average is given.
