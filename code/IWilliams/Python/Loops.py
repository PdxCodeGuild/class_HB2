'''
While loop:

while condition:
    statement(code)
'''
# print_hello = 1
# while print_hello <=5:  #6<=5 ==False
#     print('Good evening')
#     print_hello +=1
    
# num =1
# even_numbers = []

# while num <=20:
#     if num % 2 ==0:
#         even_numbers.append(num)
#     num +=1
# print('Even numbers are', even_numbers)

# x = True
# while x:
#     print ('Infinite ')
#     x = False

# num = 1
# while num <=7:
#     print(f'This is True: {num} <=7')
#     num +=1
# else:
#     print(f'This is False: {num}>7')
    

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print('Hello number')

# odd_numbers = []
# for i in range(1, 22):
#     if i %2 !=0:
#         odd_numbers.append(i)
# print(f'Odd Numbers: {odd_numbers}')

# num = [0]
# for i in num:
#     print(i)
#     num.append(i+1)


# numbers = [1, 2, 3, 4, 5, 6, 7]
# for num in numbers:
#     print(num)
# else:
#     print('We have printed all the numbers')

# example_date ={
#     'Year': 2025,
#     'Month': 'July',
#     'Day': 30
# }
#print(example_date['Month'] )   

# for key in example_date:
#     print(f'{key}: {example_date[key]}')

# for k, v in example_date.items():
#     #print(f'{key}: {value}')
#     print(f'{k}: {v}')
    
# for num in range(1, 20):
#     if num ==5:
#         break
#     else:
#         print(num)

# for num in range(1, 20):
#     if num ==5:
#         continue
#     else:
#         print(num)

# while True:
#     print('Good evening class HB2')
#     name = input('What is your name?: ')
#     if name == 'exit':
#         break
#     print(name)
# print('Our while loop has completed')


# while True:
#     print('Good evening class HB2')
#     name = input('What is your name?: ')
#     if name == 'exit':
#         break
#     elif name == 'password':
#         continue
#     print(name)
# print('Our while loop has completed')


# user_input = input('Enter a number:')
# try:
#     user_input = int(user_input)
# except:
#     print('Invalid number...goodnight')
#     exit()
# print(f'You entered number {user_input}')

# while True:
#     user_input = input('Enter a number:')
#     try:
#         user_input = int(user_input)
#         break
#     except ValueError:
#         print('Invalid number...goodnight')
# print(f'You entered number {user_input}')

# for x in range(10): 
#     print(x)
#     time.sleep(.5)

#user_input = input('Enter a number') #returns a string
# user_input = int(input('Enter a number')) #convert string to num
# for x in range (user_input):
#     print(x)
#     time.sleep(.5)
    
# for x in range (3, 11):
#     print(x)
#     time.sleep(.5)

# for x in range (0, 21, 2):  #[0, 1, 2, 3.....20]
#     print(x)
#     time.sleep(.5)

class_name = 'HB2'
# for char in class_name:
#     print(char)

# for c in class_name:
#     print(c)
#     if c == 'B':
#         break

# class_name = 'Honeybadger2'
# for char in class_name:
#     if char == 'E': #E
#         continue
#     print(char)
    

import random
numbers = [1, 12, 57, 90, 1111, 888, 333, 55]  
print(random.choices(numbers, k=3))
    
