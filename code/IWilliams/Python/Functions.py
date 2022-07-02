# def greet():
#     print('Good evening')
#     print('Welcome to Functions')
    
# greet()
    

# def greet(first_name, last_name):
#     print(f'Hello {first_name}, {last_name}')
    
# greet('Wayne', 'Bruce')
# greet('Grey', 'Jean')
# greet('Jean', 'Grey')


# 2 function types --> Values and Task
#Task
# def greet(name):
#     print(f'{name}, from print function')
#     return name #value from function
    
# print(greet('Joe'))


#Value
# def get_greeting(name):
#     return f'Good evening {name}'
# message = get_greeting('Paul')
# file = open('get_greeting.txt', 'w')
# file.write(message)
# file.close()


# #flush this out..
# def get_greeting2():
#     results = get_greeting()
#     return results

# print(get_greeting2('Larry'))


# def increment(number, by):
#     return number + by

# result = increment(3, 1)
# print(result)


# def increment(number, by=1):
#     return number + by
# print(increment(2))


# def increment(number, by=1):
#     return number + by
# print(increment(2, 13))

# def increment(num1=1, num2=1):
#     return num2 +num1
# print(increment(num2=5, num1=13))


#this will result in Typeerror
# def multiply(a, b):
#     return a*b

# print(multiply(2, 4, 6, 8))

#xargs
# def multiply(*nums): #[2, 4, 6, 8]
#     total = 1
#     for n in nums:
#      #print(n)
#         #total = total * n
#         total *=n
#     return total

# print(multiply(2, 4, 6, 8))

#xxargs --> key/word
# def user_demographics(**user):
#     print(user['name'], user['confirmed'])
    
# user_demographics(id=100, name='Parker', age=35, confirmed ='N')

# def patient():
#     MRN = '7VLYZ'

#print(MRN) #not accessible to local scope 

# MRN = 'Z10111'
# def patient(name):
#     MRN = '85RZLL'
    
# def doctor(name):
#     MRN = '67382C'

# patient('Smith')
# print(MRN)

# def repeat(quote, num):
#     print(quote * num)

# print(repeat('Live your best life ', 5)'

# def get_temp(temp):
#     if temp > 90:
#         return 'Hot'
#     elif temp >75 and temp <=90:
#         return 'Warm'
#     elif 60 <temp <=75:
#         return 'Comfortable'
#     elif  45 <temp <=60:
#         return 'Chilly'
#     else:
#         return 'Pack your parka'


# print(get_temp(40))


