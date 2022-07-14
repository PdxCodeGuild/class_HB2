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
    
    while index < 100000:
        winning, ticket = pick6()
        matches = num_matches(winning, ticket)
        
        if matches == 0:
            balance -= 2
        elif matches == 1:
            balance += 2
        elif matches == 2:
            balance += 5
        elif matches == 3:
            balance += 98
        elif matches == 4:
            balance += 49998
        elif matches == 5:
            balance += 999998
        elif matches == 6:
            balance += 24999998
        
        index += 1

    return print(f'Final Balance: {balance}')

main()