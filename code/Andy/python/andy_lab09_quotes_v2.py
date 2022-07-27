import pprint
import requests



def get_response(page, filter):#matches what it represents

    response = requests.get(f'https://favqs.com/api/quotes' , params = {'page': page,'filter': filter}, headers= {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})#make sure parenthesis and curly brackets are closed
        
    return response


# def get_filter():
#     # filter = web['quotes'][0]['body']
#     for i in range(len(web)):
#         print(web[i]["body"])


page_counter = 1 

# keyword = input('Enter in a keyword: ')
keyword = 'nature' #just to test


# # print(web)
# # 
response = get_response(page_counter, keyword) #calling get response fuction with arguments page counter and keyword and setting it equal to web
# print('response : ', response)
# print('response text: ', response.text)
# json_response = response.json()['last_page'] 

quotes = response.json()['quotes'] #<--- thats a type list 
print('response json: ', quotes)#just a variable not a method




for i in range(len(quotes)):

    #get author from first quote of list 
    first_quote_dict = quotes[i]
    first_author = first_quote_dict['author']
    print('************************first author: ' , first_author)
    #get the quote from the first quote of list 
    first_quote = first_quote_dict['body']
    print('first quotes *************$$$$', first_quote)
    # json_response = response.json() # makes it 
    # pprint.pprint('json response: ', json_response)




#get keywoed
#get user inputs
#print out quotes 
#get response

