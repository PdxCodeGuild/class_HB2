'''
Justin Young
Lab 03
Version1
'''

def n2p(number):
    ones = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
    teens = {1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
    tens = {1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
    if number >= 20:
        a = number%10    
        b = number//10    
        if a ==0:
            return tens[b]
        else:
            return f'{tens[b]}{ones[a]}'
    elif number ==10:
        return tens[1]
    elif number >= 11 <= 19:
        a = number%10 
        if a >=1 <=9:
            return teens[a]
    elif number >= 0 <= 9:
        a = number%10
        return ones[a]
         
while True:
    try:
        user_num = input('Enter a number between 0-99: ')
        user_num = int(user_num)
        if user_num >= 100:
            print(f'number too high, 0-99 only pls')
            continue
        break
    except:
        user_num =input(f'Not a valid entry')
        continue
        
print(n2p(user_num))
