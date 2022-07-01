#
#Variables, integer, float, boolean, string
student_count = 100 #integer
rating = 99.2 #float
is_on = True #boolean True/False (accepted); TRUE/true 
book_name = 'Python Magic'

#Case Sensitive 
# student_count 
# STUDENT_COUNT  
# Student_Count


#Strings
# '', "" ''' '''
# string1 = 'Single Quote'  
# string2 = "Double Quote"
# string3 = '''
#     Hello, today is 6/28

# '''


course = 'Python Programming'
# print(len(course)) #general purpose 
# print(course[0])
# print(course[-1])

#slicing
# ['beg pos, end pos']
# print(course[0:3])
# print(course[0:]) 
# print(course[:3])
# print(course[:], 'copy of string')
# print(course[-5:-2])
# print(course[0:20:2])

#string methods
# course = '   python programming   '
# print(course.upper(), 'upper case')#converts string to upper case
# print(course.lower(), 'lower case') #converts string to lower case
# print(course.title(), 'proper case') #caps 1st letter of every word
# print(course.strip(), 'strip method') #removes trailing spaces 
# print(course.lstrip(), 'lstrip') #removes trailing left hand space
# print(course.rstrip(), 'rstrip') #removes trailing right spaces
# print(course.find('pro')) # returns the index of chars
# print(course.find('Pro')) #if value not found, return -1
# print(course.replace('m', 'M')) #replace m with M
# print('the'in course) #returns a boolean False
# print('tho' in course) #returns boolean True
# print('yellow' not in course) #

#Numbers
'''
3 types of numbers in Python. integers, floats, complex 
'''
# x = 100 # int
# y = 100.1 #float
# #c = 100+ 2i

# print(100 + 3) #addition
# print(100 - 3) #subtraction 
# print(100 * 3) #multiplication
# print(100/ 3, 'division') #division --> returns float
# print(100 // 3, 'floor division') #floor  --> returns int
# print(5 % 2, 'modulus') # 5/2 = 2; with 1 remaining 
# print(6 %3, 'modulus, no remainder')
# print(100 ** 3, 'exponent') #exponent --> left to the power of right. 100 to power of 3

# y = 100
# y = y+3 
# y +=3

# import math
# # print(math.ceil(2.2))
# # print(math.floor(2.2))

# import random
# print(random.random()) #returns a number between 0 and 1
# print(random.randint(0, 10)) #return number between 0 and 10

# letters = 'abcde'
# print(random.choice(letters))

# greeting = 'Hello'
# user_input = input('Enter your name ')
# print(greeting + user_input)

# greeting = 2
# #user_input = input("Enter  your number ")
# user_input = int(input("Enter  your number "))
# print(greeting + user_input)
# print(type(user_input))


# x = input('Enter a number ')
#convert user input to integer
# x = int(x)

# #x = -2
# if x>0:
#     print('This is a positive number')
#     print("😊")
# elif x==0:
#     print('The number is 0')
# else:
#     print('This is a negative number')

# a = 2
# b = 40
# print(abs(b))
# print(min(a, b), 'min num')
# print(max(a, b), 'max num')
# print(sum((a, b))) #pass as tuple or list


#               0          1               2       3       4           5
#animals = ['platypus', 'honeybadger', 'skunk', 'tiger', 'goldfish', 'duck']

# print(len(animals))

# for a in animals:
#     print(a)
    
# numbers = range(5)
# # print(numbers)

# for n in numbers:
#     print(n)     

# for i in range(len(animals)):
#     print(i)#5 --> len(5)

# for i in range(len(animals)):
#     print(animals[i])# 

#key/value pairs 
grades = {
    'A': '90-100',
    'B': '80-89',
    'C': '70-79',
    'D': '60-69',
    'F' : '0-59'
}

for key in grades:
    print(grades[key])


for key, value in grades.items():
    print(key, value)
