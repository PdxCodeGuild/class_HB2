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

for x in range(loops):
    winning_ticket = pick_number()
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

print(payoff)




## OLD CODE
# if winningticket[0] == purchaseticket[0]:
#    a = (a + 1)
# if winningticket[1] == purchaseticket[1]:
#    b = (b + 1)
# if winningticket[2] == purchaseticket[2]:
#    c = (c + 1)
# if winningticket[3] == purchaseticket[3]:
#    d = (d + 1) 
# if winningticket[4] == purchaseticket[4]:
#    e = (e + 1)
# if winningticket[5] == purchaseticket[5]:
#    f = (f + 1)

# sum = (a + b + c + d + e + f)

# if sum == 1:
#   earnings = earnings + 4
# if sum == 2:
#   earnings = earnings + 7
# if sum == 3:
#   earnings = earnings + 100
# if sum == 4:
#   earnings = earnings + 50000
# if sum == 5:
# earnings = earnings + 1000000
# if sum == 6:
# earnings = earnings + 25000000