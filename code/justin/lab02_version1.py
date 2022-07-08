'''
Justin Young
Lab 02
Version1
'''

measurements = {'ft' : 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000}
user_entry = input('Enter how many feet you wish to convert: ')

while True:
    try:
        float(user_entry)
        user_entry = float(user_entry)
        answer = user_entry * measurements['ft']
        break
    except ValueError:
        user_entry = input(f'Value entered is not an acceptable number try again: ')
        False

print(f'The number of meters for {user_entry} ft is {answer}')
