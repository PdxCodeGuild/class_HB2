from urllib.robotparser import RequestRate
import requests
keyword = input('Enter in a keyword: ')
page_counter = 1 
response= requests.get(f'https://favqs.com/api/quotes?page=<page>&filter=<keyword>.') #to help with they params set page = to page and filter = to the page it starts on 
#response = requests.get(f'https://favqs.com/api/quotes',params= {'pages':{page_counter} , 'filter':{keyword}} , headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}')

print(response)



 