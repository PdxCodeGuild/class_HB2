# VERSION 1 #


import json
import requests

# response = requests.get("https://favqs.com/api/qotd")

#
# print(response)
# print(type(response))
# print(response.text)
# print(response.status_code)

# quote = response.text
# json_response = response.json()

# quote_author = json_response['quote']['author']

# quote_body = json_response['quote']['body']

# print(f'The author is {quote_author}\nTheir quote: {quote_body}')




#       VERSION 2       #



import pprint





page_number = 1

search_term = 'everything'


response = requests.get(f"https://favqs.com/api/quotes?page={page_number}&filter={search_term}",
                        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'},)


json_response = response.json()
# pprint.pprint(json_response)
is_last_page = json_response['last_page']


# is_last_page == 
# pprint.pprint(json_response['quotes'])
# pprint.pprint(json_response['quotes'][0])

quotes_list = []

for i in range(len(json_response['quotes'])):
    
    author_json = json_response['quotes'][i]['author']
    quote_json = json_response['quotes'][i]['body']
    
    quote_dictionary = {
        'author': author_json,
        'quote': quote_json
        }
    quotes_list.append(quote_dictionary)
pprint.pprint(quotes_list)
# print(len(json_response['quotes']))
