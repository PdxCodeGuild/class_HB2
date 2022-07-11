
#            Lab 01: Average Numbers          #

entering_numbers = True

list = []

while entering_numbers:
    
    answer = input("Enter a number or 'done' to quit: ")
    
    if answer == 'done':
        entering_numbers = False
        
    else:
        list.append(int(answer))

        
print(f"\nYou entered nums {list} \n\nThe average of the numbers is {sum(list) / len(list)}")
    
