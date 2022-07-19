'''
Justin Young
Optional Lab, "Lab 17: Quotes API"
https://github.com/PdxCodeGuild/class_orchid/blob/main/1%20Python/labs/17%20Quotes%20API.md
Version1
'''

import requests
import time

response = requests.get('https://favqs.com/api/qotd')
# print(response.text)
# print(response)
page = response.json()
r_qt = page['quote']
quote = r_qt['body']
author = r_qt['author']
print(f'\n"{quote}" \nBy:{author}\n')
