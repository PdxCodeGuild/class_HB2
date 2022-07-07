'''
Justin Young
Lab 03
Version3
'''

# user_input = input("enter a number: ")

value = {1:'I',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',50:'L',100:'C',500:'D',1000:'M'}
# a = user_input//1000


user_input = input('Enter a number 1-1999, or "done" to exit: ')
while user_input != 'done':
    try:
        int(user_input)
        break
        # if len(user_input) ==4:
        #     print('is 4 num long')
    except:
        user_input = input('Please try again: ')
while len(user_input)<=1:        
    if int(user_input[-1]) <= 3:
        ones=(value[1]*int(user_input[-1]))
        break
    elif int(user_input[-1])==4:
        ones=value[int(user_input)]
        break
    elif int(user_input[-1])==5:
        ones=(value[5])
        break
    elif int(user_input[-1])>=6<=9:
        ones=value[int(user_input)]
        break

print(ones)        
# if int(user_input[-2])<=3:
#     tens=(value[10]*int(user_input[-2]))
# print(tens+ones)    