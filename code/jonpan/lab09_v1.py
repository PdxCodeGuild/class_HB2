#Lab09: Quotes API

import requests
import pprint

response = requests.get("https://favqs.com/api/qotd", headers={'Accept': 'application/json'})
data = response.json()

pprint.pprint(data)
# print(type(data))

# print(f"\nAuthor: {data['quote']['author']}") 
# print(f"\nQuote: {data['quote']['body']}") 

quotes = {
    'Author': data['quote']['author'],
    'Quote': data['quote']['body']
}

print(f"\nAuthor: {quotes['Author']}")
print(f"\nQuote: {quotes['Quote']}") 