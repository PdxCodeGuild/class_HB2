import random 

def pick6():
    index = 0
    winning = []
    ticket = []
    
    while index < 6:
        winning.append(random.choice(range(1, 100)))
        ticket.append(random.choice(range(1, 100)))
        index += 1
    
    return winning, ticket

def num_matches(winning, ticket):
    index = 0
    matches = 0
    
    while index < 6:
        if winning[index] == ticket[index]:
            matches += 1
        
        index += 1
    
    return matches

def main():
    index = 0
    balance = 0
    earnings = 0
    expenses = 0
    
    while index < 100000:
        winning, ticket = pick6()
        matches = num_matches(winning, ticket)
        
        if matches == 0:
            earnings += 0
        elif matches == 1:
            earnings += 4
        elif matches == 2:
            earnings += 7
        elif matches == 3:
            earnings += 100
        elif matches == 4:
            earnings += 50000
        elif matches == 5:
            earnings += 1000000
        elif matches == 6:
            earnings += 25000000
        
        expenses -= 2
        index += 1
        
    balance = earnings + expenses
    ROI = (earnings + expenses) / expenses
    
    return print(f'Final Balance: {balance}'), print(f'ROI: {ROI}')

main()