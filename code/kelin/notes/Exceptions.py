# try:
#     num = int(input('Enter a number: '))
#     divide_num = 100/num
# except (ValueError, ZeroDivisionError):
#     print('Please enter a number other than 0')
# Enter a number: 0
# Please enter a number other than 0
    # print(ex, 'printing the ex error')
    # print(type(ex))
# except ZeroDivisionError:
#     print('Number cannot = zero')

# Enter a number: 0
# Number cannot = zero

# else:
#     print('We are printing the else clause')

# Enter a number: f
# Please enter a number

# Enter a number: 3
# We are printing the else clause

# Enter a number: d
# Please enter a number
# invalid literal for int() with base 10: 'd'

# Enter a number: f
# Please enter a number
# invalid literal for int() with base 10: 'f' printing the ex error
# <class 'ValueError'>

# Enter a number: 0
# Traceback (most recent call last):
#   File "C:\Users\13607\Documents\Coding\Bootcamp\GitHub\class_hb2\code\kelin\practice\exceptions.py", line 3, in <module>
#     divide_num = 100/num
# ZeroDivisionError: division by zero

# import numbers

# message = input('Enter a number ')
# try:
#     number = float(message)
# except ValueError:
#     print('Please enter a number')
# else:
#     print('Your number converted successfully')
# finally:
#     print('Finally is printing')

# Enter a number 5
# Your number converted successfully
# Finally is printing

names = ['Peter', 'Parker', 'Storm']
while True:
    message = input('Enter a number ')

    try:
        number = int(message)
        names[number]
        break
    except(ValueError, IndexError) as error:
        if type(error) == IndexError:
            print('We have an index error')
        else:
            print('Please enter a valid number')
        # print(error, 'Printing except error')
print('No error has occured')

# Enter a number j
# Please enter a valid number

# Enter a number 1
# No error has occured

# Enter a number 3
# list index out of range Printing except error
# Enter a number 2
# list index out of range Printing except error
# Enter a number 1

