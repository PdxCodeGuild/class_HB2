# Version 1
def version1():
    nums = [5, 0, 8, 3, 4, 1, 6]
    total_amount = 0

    for num in nums:
        total_amount += num

    average_amount = total_amount / len(nums)
    
    return print(average_amount)

# Version 2
def version2():
    total_amount = 0
    user_input = ''
    user_choices = []
    output = ''
    
    while True:
        user_input = input("Enter an integer or 'done' to exit: ")
        if user_input == "done":
            break
        else:
            user_choices.append(user_input)
        
    if len(user_choices) == 0:
        output = print("You did not enter any values")
        
    else:
        for choice in user_choices:
            total_amount += int(choice)
        output = print(f'Average: {total_amount / len(user_choices)}')
    
    return output
    
def main():
    #version1()
    version2()
    
    return 0

main()