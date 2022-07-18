import requests
import time

search_term= input('enter a term to search for: ')
response = requests.get(f"https://icanhazdadjoke.com/search?term=${search_term}", headers={
    'Accept': 'application/json'
})

# print(response)
son = response.json()
total = son["total_jokes"] #the amount of jokes they have for that term. why is the that it has to be total_jokes and not something else for this to work 
# print(total)

for s in son['results']:
    total -= 1 #subtracting one to get to the end 
    time.sleep(2) #how long its going to take for the joke to populate 
    print(s["joke"])#still dont get why it has to be but as joke and nothing else
    print(f'there is {total} left')
    if total == 0: 
        print('Thats all the jokes for this term')
        break
    more = input("another joke?: y or n?:  ")
    if more == "n": 
        break




# print(response.text)
# print(data['joke'])
# import requests
# import time


u_input = input('enter a search term:  ')
response = requests.get(f"https://icanhazdadjoke.com/search?term=${u_input}", headers={
     'Accept': 'application/json'
 })

