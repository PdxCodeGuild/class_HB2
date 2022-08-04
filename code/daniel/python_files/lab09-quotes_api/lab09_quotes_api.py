# https://favqs.com/api/qotd

import requests
#================================
#Version1
#================================


# response = requests.get(f"https://favqs.com/api/qotd", headers={'Accept': 'application/json'})
# # print(response.json())

# random_quote = response.json()['quote']['body']
# print(random_quote)

# random_quote_author = response.json()['quote']['author']
# print(' ~',random_quote_author)


#================================
#Version2
#================================
url_format = "https://favqs.com/api/quotes?page={0}&filter={1}"


# print(response.json())

page = 1
get_keyword = input("Enter a search term to get a related quote: ")


while True:
    url_string = url_format.format(page, get_keyword)
    response = requests.get(url_string, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    print(response)
    keyword_quote = response.json()['quotes']
    print(len(keyword_quote))
    for quote in keyword_quote:
        print(quote['body'])
        print("======")
    next_response = input("Enter 'next page' or 'done': ")
    if next_response == 'next page':
            page += 1
    elif next_response == 'done':
            break




# ======================================================================


