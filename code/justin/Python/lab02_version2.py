'''
Justin Young
Lab 02
Version2
'''

measurements = {'ft' : 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000}
user_distance = input(f'What is the known distance: ')
while True:
    try:
        float(user_distance)
        user_distance = float(user_distance)
        break
    except:
        user_distance = input(f'Not a valid number try again: ')
        False
print(f'{user_distance} entered')
user_measurement = input(f'What is the known unit of measurement: ')
while True:
    if user_measurement in measurements.keys():
        answer = user_distance * measurements[user_measurement]
        print(f'{user_distance} {user_measurement} is equal to {answer} meters.')
        break
    else:
        user_measurement = input(f'{user_measurement} is not a valid entry select from "ft", "mi", "m", "km", and try again: ')
        False

