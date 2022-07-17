'''
Justin Young
Lab 08
Version2
'''

import requests
import time


u_input = input('enter a search term:  ')
response = requests.get(f"https://icanhazdadjoke.com/search?term=${u_input}", headers={
    'Accept': 'application/json'
})

js = response.json()
total = js['total_jokes']
for j in js['results']:
    print(f'\nThere are {total} more jokes with the word {u_input}, get ready for the next one!!')
    total -= 1
    time.sleep(3)
    print(j['joke'])
    if total == 0:
        print(f'Thats all the jokes with {u_input}, thanks!')
        break
    a = input(f'\nLOL! Funny right? another joke? y/n: ')
    if a.lower() == 'n':
        break

