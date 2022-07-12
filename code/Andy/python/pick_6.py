import random

# winning_lotto_number = [] # Placing variable with empty List of to hold numbers 

# for i in range(1 , 7): #creating a forloop to be repeated 6 times
#     numbers = random.randint (1,99) #generating random numbers between 1 and 99 

#     winning_lotto_number.append(numbers) # getting all the numbers that were generated from the top and putting them in to the list of lottonumbers



# users_attempt = [] #same thing as before just putting a place holder for the numbers that will be inputed 

# for i in range(1,7): #for loop getting ready to as the user 6 times to input a number rather than typing the same thing 6 times
#     numbers = random.randint (1,99)

#     users_attempt.append(numbers) if you have to make one of these twice, indicates that you should just use a function

def number_picker():
    numbers = [] #something to put the nums in 
    for i in range(1,7): #Should run the loop 6 times 
        numbers.append(random.randint (1,99))
    return numbers


def compare(winning_ticket, current_ticket):
    counter = 0 #keeping track of how many matches  
    for i in range(6): #checking the index of the two arguments range is returning an array which starts at the index of 0 and then goes up to 5
        if winning_ticket[i] == current_ticket[i]:# running the 6 times 
            counter +=1 # counting how many match 
    return counter 
    

# print(compare(number_picker(), number_picker())) 
                                                #test
winner = number_picker() # winning ticket on the outside so it stays constant
balance = 0 # Holder

for i in range(100000):
    comparing_tickets = compare(number_picker(), winner) #i'm getting my compare function putting my number_picker funtion with in it which is the one thats gonna be getting changed the 100,000 time and comparing it to the winner which is the one that will be staying the same all those times 
    balance -= 2  # since the balnce on top is the holder im making it -2 since that is how much it is to pay for a ticket 
    if comparing_tickets == 1: # if one of the compared matches has one match in the same spot we get $2 since we were already losing 2
        balance += 4
    elif comparing_tickets == 2:
        balance += 7 
    elif comparing_tickets == 3:
        balance += 100
    elif comparing_tickets == 4:
        balance += 50,000
    elif comparing_tickets == 5:
        balance += 1,000,000
    elif comparing_tickets == 6:
        balance += 25,000,000

return_of_in = balance / 200000 # getting the balance and then dividing it bt the 200,000 because thats the two dollars to buy the ticket and multiplying it by the many times we're gonna but the ticket 
print(f'The winning lotto numbers are {winner}') 
print(f'\n and your balance is {balance}')
print(f'Your ROI is {return_of_in}')


   


# print(users_attempt)
# print (winning_lotto_number)
                        #test
