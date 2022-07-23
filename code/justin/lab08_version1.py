'''
Justin Young
Lab 08
Version1
'''

import requests
import time

response = requests.get("https://icanhazdadjoke.com", headers={'Accept': 'application/json'})
call = response.json()
x = input('wanna hear a joke? y/n: ')
if x == 'y':
    print(call['joke'])


