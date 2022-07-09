

def time_conv(x):
    time={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',
    17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fiftey'}
    a=int(x)//100
    b=int(x)%100
    hour=time[a]
    if b <=20:
        min=time[b]
    elif b >20:
        ten_min=b//10*10
        one_min=b%10
        min=time[ten_min]+time[one_min]

    return f'{hour}-{min}'

while True:
    user_time=input('Enter a time in hours and minutes, ex 1245 or done to stop: ')
    print(time_conv(user_time))
    if user_time == 'done':
        break