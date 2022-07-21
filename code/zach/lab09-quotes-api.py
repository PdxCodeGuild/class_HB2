import requests 

def version1():
    response = requests.get('https://favqs.com/api/qotd', headers={
        'Accept': 'application/json'})

    quote = response.json()['quote']['body']
    author = response.json()['quote']['author']
    
    return print(f'"{quote}" - {author}')

def main(): 
    version1()
    
main()