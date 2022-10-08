import requests
import pprint

def print_results(p_num, search_term):
    response = requests.get(f"https://favqs.com/api/quotes?page=<page>&filter={search_term}", params={'page':{p_num}},
    headers={'Accept': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    data = response.json()

    for i in range(len(data['quotes'])):
        print(f"\nAuthor: {data['quotes'][i]['author']}") 
        print(f"\nQuote: {data['quotes'][i]['body']}") 

search_term = input("enter a keyword to search for quotes:  ")
p_num = 1

# search_term and p_num are defined outside the function so need to be included in the function(here)

while True:
    print_results(p_num, search_term)
    cont = input("enter 'next page' or 'done'  ")
    if cont == 'done':
            print("Goodbye")
            break
    else:
        p_num += 1


# pprint.pprint(data)
# print(f"\nAuthor: {data['quotes'][0]['author']}") 