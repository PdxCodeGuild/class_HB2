'''
Justin Young
Lab 09
Version 1
'''

import requests
import time

response = requests.get('https://favqs.com/api/qotd')
page = response.json()['quote']
quote = page['body']
author = page['author']
print(f'\n"{quote}" \nBy:{author}\n')
