'''
Justin Young
Lab 09
Version2
'''

import requests
import pprint
import time

inc = 1
u_term = input('enter a keyword to search for quotes: ')
p_num = 1
url = requests.get('https://favqs.com/api/quotes', params={'filter':{u_term}, 'page':{p_num}}, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
quotes = url.json()['quotes']
while True:
    print('-----------------------------------------------------------------------')
    print(f'There are {len(quotes)} quotes associated with {u_term} - page {p_num}')
    print('-----------------------------------------------------------------------')
    for q in quotes:
        print(q['body'])
    print('-----------------------------------------------------------------------')
    if url.json()['last_page'] == True:
        print('Thats all the quotes!!')
        break
    if url.json()['last_page'] == False:
        a = input("enter 'next page' or 'done': ")
        if a == 'done':
            break
        if a == 'next page':
            p_num += 1
            url = requests.get('https://favqs.com/api/quotes', params={'filter':{u_term}, 'page':{p_num}}, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            quotes = url.json()['quotes']
            
