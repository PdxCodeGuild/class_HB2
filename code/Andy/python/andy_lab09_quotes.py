
import requests
import pprint

response = requests.get(f'https://favqs.com/api/qotd')

# print(response)
# print(response.text)

web = response.json()
# pprint.pprint(web)

get_quotes = web['quote'] #using web since pulling from that website. this goes into their dict and then doing a doing brackets to go in their dict to go into the key and retreive their value
bod = get_quotes['body'] #when pulling from the dict look at the url and go to it to see how they spell, for instance quote and not quotes or just pprint the json and look at how they word their dict there which is fast tbh 
# print(f'{bod}')
auth = get_quotes['author']

pprint.pprint(f'{bod}  by {auth}')