'''
Muki's Lab09 Quotes API
below will be the copied text of the lab in the multi line comment


'''

import requests
import time
# url i is gonna use https://favqs.com/api/qotd

question = input("Would you like a quote? \ny/n\n\t> ")
if question.lower() == "y":
    response = requests.get('https://favqs.com/api/qotd')
    # print(response)
    q = response.text
    # print(q)
    q = response.json()
    print(' ')
    quote = q['quote']
    print(f'\n\n\n\n\n\n"{quote["body"]}" \n\n\t\t')
    time.sleep(0.5)
    print(f'-- {quote["author"]}\n\n\n\n\n\n\n\n')
    time.sleep(.5)
elif question != "y":
    time.sleep(1)
    # print("Well, I didn't have one anyway. Goodbye\n\n")
    print("Well, I didn't have one anyway.\n\n")
# time.sleep(1)    
#added a delay and onto version 2

keyword = input('Enter a keyword to search for a quotes:\n\t>')
page = (1,26)
pk = (page, keyword)
response = requests.get('https://favqs.com/api/quotes?page=<page>&filter=<keyword>', params= pk)
# print(response)
q = response.text
# print(q)
q = response.json()
print(q)
print(' ')
quote = q['quote']
print(f'\n\n\n\n\n\n"{quote["body"]}" \n\n\t\t')
time.sleep(1)
print(f'-- {quote["author"]}\n\n\n\n\n\n\n\n')
time.sleep(2)





