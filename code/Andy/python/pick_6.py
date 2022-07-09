import random

# winning_lotto_number = [] # Placing variable with empty List of to hold numbers 

# for i in range(1 , 7): #creating a forloop to be repeated 6 times
#     numbers = random.randint (1,99) #generating random numbers between 1 and 99 

#     winning_lotto_number.append(numbers) # getting all the numbers that were generated from the top and putting them in to the list of lottonumbers



# users_attempt = [] #same thing as before just putting a place holder for the numbers that will be inputed 

# for i in range(1,7): #for loop getting ready to as the user 6 times to input a number rather than typing the same thing 6 times
#     numbers = random.randint (1,99)

#     users_attempt.append(numbers)

def number_picker():
    numbers = []
    for i in range(1,7):
        numbers.append(random.randint (1,99))
    return numbers


def compare(winning_ticket, current_ticket):
    counter = 0 #keeping track of how many matches  
    for i in range(6): #checking the index of the two arguments range is returning an array which starts at the index of 0 and then goes up to 5
        if winning_ticket[i] == current_ticket[i]:# running the 6 times 
            counter +=1 # counting how many match 
    return counter 
    
print(compare(number_picker(), number_picker()))





   


# print(users_attempt)
# print (winning_lotto_number)
                        #test

