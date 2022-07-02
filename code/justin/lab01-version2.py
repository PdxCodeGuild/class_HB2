'''
Justin Young
Lab 00
Version 2
'''

user_num = input('Enter a number or "done" to finish: ')
user_list = []
added = 0
counted = 0

while user_num.lower() != 'done':
    try:
        user_list.append(int(user_num))
        print('Your numbers so far are', user_list)
        user_num = input('Enter a number or "done" to finish: ')
    except ValueError:
        user_num = input(f'{user_num} is not an acceptable number try again or enter "done": ')

else:
    for num in user_list:
        added += num
    for x in range(len(user_list)):
        counted +=1
    print('The average of your numbers is', added/counted)
        