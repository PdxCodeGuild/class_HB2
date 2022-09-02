'''
Justin Young
Lab 03
Version2
'''

def n2p(number):
    ones = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:''}
    teens = {1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
    tens = {1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety',0:''}
    if number >= 100:
        a = number % 10
        b = number % 100 // 10
        c = number // 100
        if a == 0:
            if b == 0:
                return f'{ones[c]}hundred'
            elif b > 0:
                return f'{ones[c]}hundred-{tens[b]}'
        elif a > 0:
            if b == 0:
                return f'{ones[c]}hundred-{ones[a]}'
            elif b == 1:
                return f'{ones[c]}hundred-{teens[a]}'
            elif b > 1:
                return f'{ones[c]}hundred-{tens[b]}{ones[a]}'

    elif number >= 20 <= 99:
        a = number % 10    
        b = number // 10  
        if a == 0:
            return tens[b]
        else:
            return f'{tens[b]}-{ones[a]}'
    elif number >= 10 <= 19:
        a = number % 10
        b = number // 10 
        if a == 0:
            return tens[b]
        elif a >= 1 <= 9:
            return teens[a]
    elif number > 0 <= 9:
        a = number % 10
        return ones[a]
    elif number == 0:
        return 'zero'
         
while True:
    try:
        user_num = input('Enter a number between 0-999: ')
        user_num = int(user_num)
        if user_num >= 1000:
            print(f'number too high, 0-999 only pls')
            continue
        break
    except:
        user_num =input(f'Not a valid entry')
        
        
print(n2p(user_num))