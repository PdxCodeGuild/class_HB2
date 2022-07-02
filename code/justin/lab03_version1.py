'''
Justin Young
Lab 03
Version1
'''

def n2p(number):
    ones = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
    tens = {1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
    if number >= 20:
        a = number%10    
        b = number//10    
        if a == 0:
            return tens[b]
        else:
            return f'{tens[b]}-{ones[a]}'
    elif number >= 10 <= 19:
        a = number%10
        b = number//10 
        if a == 0:
            return tens[b]
        elif a == 1:
            return 'eleven'
        elif a ==2:
            return 'twelve'
        elif a ==3:
            return 'thirteen'
        elif a ==4:
            return 'fourteen'
        elif a ==5:
            return 'fifteen'
        elif a ==6:
            return 'sixteen'
        elif a ==7:
            return 'seventeen'
        elif a ==8:
            return 'eighteen'
        elif a ==9:
            return 'nineteen'
    elif number >= 0 <= 9:
        a = number%10
        return ones[a]
         
user_num = input('Enter a number between 0-99: ')
try:
    user_num = int(user_num)
except:
    print(f'Invalid entry, enter a number between 0-99: ') 
else:
    user_num = int(user_num)   
print(n2p(user_num))
