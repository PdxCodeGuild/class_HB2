import requests


def get_response(page, filter):#matches what it represents

    response = requests.get(
        f'https://favqs.com/api/quotes' , 
        params = {'filter': filter, 'page': page}, 
        headers= {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})#make sure parenthesis and curly brackets are closed

    return response


page = 1 
keyword = input('Enter in a keyword: ')
response = get_response(page, keyword) #calling get response fuction with arguments page counter and keyword and setting it equal to web
quotes_dict = response.json()#['quotes'] #<--- thats a type list 
# print('response dir: ', dir(response))

while True: #having it repeat until not 
    for i in range(len(quotes_dict["quotes"])): # looping through the list of the object
        # get author from first quote of list 
        first_quote_dict = quotes_dict['quotes'][i] # accessing item at the key of sequence 
        first_author = first_quote_dict['author']
        # get the quote from the first quote of list 
        first_quote = first_quote_dict['body']
        print(f'\n{first_quote} \n\t\t{first_author}\n')
        # json_response = response.json() # makes it 
        # pprint.pprint('json response: ', json_response) 

    print(quotes_dict['last_page'])

    if quotes_dict['last_page'] != True:
        page_option = input('would you like to go to the next page? type y for next page or n for Done: ') #command d
        
        if page_option == "y":
            page += 1 
            print('next page number', page)
            response = get_response(page, keyword) #code stuff not able to read 
            print('response info: ', response)
            quotes_dict = response.json()# makes it able for us to read. calling json method  on the response object
            # print('printing type for variable', type(quotes_dict))
            # continue #it goes back up 

        else:
            break

    else:
        print("You're on the last page")
        break
           
                 


