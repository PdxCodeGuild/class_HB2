
import requests
def get_counter(pages, filter):#matches what it represents

    response = requests.get(f'https://favqs.com/api/quotes' , params = {'pages': {pages},'filter':{filter}}, headers= {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})#make sure parenthesis and curly brackets are closed
        
    return response
def get_filter():
    # filter = web['quotes'][0]['body']
    for i in range(len(web)):
        print(web[i]["body"])
page_counter = 1 

keyword = input('Enter in a keyword: ')
# print(response)
# print(web)
# web = response.json() #to get all that info and transfer it 
print(get_counter(page_counter, keyword))


# print(get_filter())

#get keywoed
#get user inputs
#print out quotes 
#get response

