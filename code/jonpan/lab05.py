import random

def matches_count(winning_ticket, purchase_ticket):
    matches = 0
    for x in range(6):
        if winning_ticket[x] == purchase_ticket[x]:
            matches += 1       
    return matches

def pick_number(x=6):
    return random.sample(range(1, 99), x)

balance = 0
loops = 100000
ticket_cost = (loops * -2)
winning_ticket = pick_number()

for x in range(loops):
    purchase_ticket = pick_number()
    match_counter = matches_count(winning_ticket, purchase_ticket)
    
    if match_counter == 1:
        balance += 4
    elif match_counter == 2:
        balance += 7
    elif match_counter == 3:
        balance += 100
    elif match_counter == 4:
        balance += 50000
    elif match_counter == 5:
        balance += 1000000
    elif match_counter == 6:
        balance += 25000000

payoff = balance + ticket_cost
ROI = (payoff - ticket_cost) / payoff 
# ROI_pct = "{. 0%}".format(ROI)
# print(ROI_pct)

print(f"\nPayoff: {payoff} ")
print(f"\nExpenses: {ticket_cost} ")
print(f"\nROI: {ROI:.0%} ")