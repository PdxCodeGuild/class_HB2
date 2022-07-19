'''
Justin Young
Optional Lab, "Lab 17: Quotes API"
https://github.com/PdxCodeGuild/class_orchid/blob/main/1%20Python/labs/17%20Quotes%20API.md
Version2
'''

import requests
import time


p_count = 1
u_term = input('enter a keyword to search for quotes: ')
url = f'https://favqs.com/api/quotes?page={p_count}&filter={u_term}'
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)
page = response.json()
cur_p = page['page']
q = page['quotes']
n_quotes = 0

if page['last_page'] == False:
    print(f'25 quotes associated with {u_term} - page {cur_p}')
    for a in q:
        print(a['body'])
    n_i = input("enter 'next page' or 'done': ")
    while True:
        if n_i == 'done':
            break
        elif n_i == 'next page':
            p_count += 1
            if page['last_page'] == False:
                print(f'25 quotes associated with {u_term} - page {cur_p}')
                for b in q:
                    print(b['body'])
                n_i = input("enter 'next page' or 'done': ")
                
        
elif page['last_page'] == True:
    for a in q:
        n_quotes += 1
        print(f'{n_quotes} associated with {u_term} - page {cur_p}')
        print(a['body'])

'''
cant figure out how to turn the page
'''
    

# num_jokes = 0
# for a in q:
#     num_jokes += 1
#     print(a['body'])


n_quotes = 0
