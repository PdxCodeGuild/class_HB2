import requests 

def version1():
    response = requests.get('https://favqs.com/api/qotd', headers={'Accept': 'application/json'})

    quote = response.json()['quote']['body']
    author = response.json()['quote']['author']
    
    return print(f'"{quote}" - {author}')

def version2():
    page = 1
    index = 0
    search_term = input('Enter a keyword to search for quotes: ')
    
    while True:
        response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={search_term}', headers={
            'Accept': 'application/json', 
            'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        last_page = response.json()['last_page']
        quotes = response.json()['quotes']
        num_quotes = len(quotes)
        
        if last_page == False:
            print(f'{num_quotes} quotes associated with {search_term} - page {page}')

            for quote in quotes: 
                print(f"'{response.json()['quotes'][index]['body']}' - {response.json()['quotes'][index]['author']}")
                index += 1
                        
            answer = input("Enter 'next page' or 'done': ")
            
            if answer == 'done':
                return
            elif answer == 'next page':
                page += 1
                index = 0
        
        
def main(): 
    #version1()
    version2()
    
main()