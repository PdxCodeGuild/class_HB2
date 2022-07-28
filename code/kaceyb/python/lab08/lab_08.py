#           PART 1            #

import requests


# response = requests.get("https://icanhazdadjoke.com", headers={
#     'Accept': 'application/json'})

# # print(response)
# # print(type(response))
# # print(response.text)
# # print(response.status_code)


# # joke = response.text
# joke = response.json()
# # print(joke)

# answer = input('Wanna hear a joke, Yes or No?: ').lower()

# if answer == 'yes':
#     print(joke['joke'])
# else:
#     print('Fine, Gbyeeee')

#             PART 2            #

search_term = input("Enter a search term: ")


response = requests.get(
    f"https://icanhazdadjoke.com/search?term={search_term}",
    headers={"Accept": "application/json"},
)

# print(response)

# joke = response.text

joke = response.json()
jokes = joke["results"]

try:

    for joke in jokes:
        print(joke["joke"])
        another_joke = input("Want another joke? yes/no: ").lower()
        if another_joke == "no":
            break

except exception as e:
    print(f"error {e}")
