# https://favqs.com/api/qotd


#================================
#Version1
#================================

import requests



response = requests.get(f"https://favqs.com/api/qotd", headers={'Accept': 'application/json'})
# print(response)


random_joke = response.json()
# print(random_joke)


joke_dict = []
joke_dict.append(random_joke['quote'])
print("joke_dict", joke_dict)
print("author", joke_dict[2])


#================================
#Version2
#================================


# get_quote = input("Enter a search term to get a random quote: ")
# print(get_quote)



# # print(response.text)
# print("=====================")
# data = response.json()
# print("=====================")
# print(data)
# print("=====================")






