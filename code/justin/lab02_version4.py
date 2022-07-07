'''
Justin Young
Lab 02
Version4
'''

measurements = {'ft' : 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000, 'yd': 0.9144, 'in': 0.0254}
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
user_starting_measurement = input(f'What is the starting unit of measurement select from "ft", "mi", "m", "km", "yd", or "in": ')
while True:
    if user_starting_measurement in measurements.keys():
        first_answer = user_distance * measurements[user_starting_measurement]
        break
    else:
        user_starting_measurement = input(f'{user_starting_measurement} is not a valid entry select from "ft", "mi", "m", "km", "yd", or "in" and try again: ')
        False
user_ending_measurement = input(f'What unit are we converting to: ')
while True:
    if user_ending_measurement in measurements.keys():
        second_answer = first_answer / measurements[user_ending_measurement]
        print(f'{user_distance} {user_starting_measurement} converts to {second_answer} {user_ending_measurement}')
        break
    else:
        user_ending_measurement = input(f'{user_ending_measurement} is not a valid entry select from "ft", "mi", "m", "km", "yd", or "in" and try again: ')
        False
   
