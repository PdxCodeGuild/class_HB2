'''
Justin Young
Lab 06
Version 1
'''
# amount = input('Enter your total dollar amount in a number: ')

def change_make(amount):
    answer = []
    r = ''
    change_a = [.01,.05,.10,.25]
    change_b = ['penn','nickle','dime','quarter']
    while amount != 0.0:
        if change_a[3] <= amount:
            q = amount // change_a[3]
            if q == 1:
                answer.append(f"{int(q)} {change_b[3]}")
            else:
                answer.append(f"{int(q)} {change_b[3]}'s")
            amount = round(amount - q*change_a[3], 2)
        elif change_a[2] <= amount:
            d = amount // change_a[2]
            if d == 1:
                answer.append(f"{int(d)} {change_b[2]}")
            else:
                answer.append(f"{int(d)} {change_b[2]}'s")
            amount = round(amount - d*change_a[2], 2)
        elif change_a[1] <= amount:
            n = amount // change_a[1]
            if n == 1:
                answer.append(f"{int(n)} {change_b[1]}")
            else:
                answer.append(f"{int(n)} {change_b[1]}'s")
            amount = round(amount - n*change_a[1], 2)
        elif change_a[0] <= amount:
            p = amount / change_a[0]
            if p == 1:
                answer.append(f"{int(p)} {change_b[0]}y")
            else:
                answer.append(f"{int(p)} {change_b[0]}ies")
            amount = round(amount - p*change_a[0], 1)
    for x in answer:
        r += x
        r += ' '
    return r    

while True:
    x = input('enter amount or "done" to exit: ')
    if x == 'done':
        break
    else:
        try:
            x = float(x)
        except:
            x = input('enter amount again: ')
        
        print(change_make(x))
     

            
            


