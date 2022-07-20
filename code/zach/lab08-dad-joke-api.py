import requests

def get_joke(search_parameter):
    response = requests.get(f"https://icanhazdadjoke.com/search?term={search_parameter}", headers={
        'Accept': 'application/json'
    })
    data = response.json()["results"]
    jokes = []
    for item in data:
        jokes.append(item['joke'])
    return jokes

def main(): 
    
    user_input = input("Enter a search term to return dad jokes or type 'done' to exit: ")
    jokes = get_joke(user_input)
    index = 0
    answer = 'yes'
    
    print(len(jokes))
    
    if user_input == 'done':
        exit
    else:
        while index < len(jokes) and answer == 'yes':
            print(jokes[index])
            index += 1
            answer = input(f"Would you like to see another dad joke about '{user_input}'? Enter yes/no: ")
        #else:
        #    print("We have run out of jokes on this topic.")

    print("You're welcome. Byeeeee")

main()