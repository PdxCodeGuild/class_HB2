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


response = requests.get(f"https://favqs.com/api/quotes?page=<page>&filter=<keyword>", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
print(response.json())

page = 1


while True:
    get_keyword = input("Enter a search term to get a related quote: ")
    # print(get_keyword)
    keyword_quote = response.json['quotes']['index']




# ======================================================================






