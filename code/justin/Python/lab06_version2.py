from asyncio.windows_events import CONNECT_PIPE_INIT_DELAY
from doctest import COMPARISON_FLAGS
'''
Justin Young
Lab 06
Version 2
'''

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)]
coin_t = ''
r = ', '
for coin in coins:
    if coin != coins[-1]:
        coin_t += coin[0]
        coin_t += r
    else:
        coin_t += coin[0]

  
x = input('Enter amount for change: ')
x = float(x)
total = []
while x > 0.00:
    print(f'\nYour remaining amount is {x} and you current change is {total}')
    y = input(f'Enter denom type, \nChoose from: {coin_t}: ')
    if y.lower() in coin_t:
        for coin in coins:
            if y.lower() == coin[0]:
                if coin[0] == 'dime':
                    num_coin = x / round((coin[1] / 100), 2)
                    am_coin = input(f'You can have up to {num_coin} {y}, enter how many you want: ')
                    new_tupe = y + ', ' + am_coin
                    total.append(new_tupe)
                    x = round(x - float(am_coin)*(coin[1] / 100), 2)          
                    continue
                elif coin[0] == 'penny':
                    num_coin = x / round((coin[1] / 100), 2)
                    am_coin = input(f'You can have up to {num_coin} {y}, enter how many you want: ')
                    new_tupe = y + ', ' + am_coin
                    total.append(new_tupe)
                    x = round(x - float(am_coin)*(coin[1] / 100), 2)          
                    continue       
                else:
                    num_coin = x // round((coin[1] / 100), 2)
                    am_coin = input(f'You can have up to {num_coin} {y}, enter how many you want: ')
                    new_tupe = y + ', ' + am_coin
                    total.append(new_tupe)
                    x = round(x - float(am_coin)*(coin[1] / 100), 2)          
                    break
print(f'Your change is {total}')
                