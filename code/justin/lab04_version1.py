'''
Justin Young
Lab 04
Version1
'''

 
c1=input('Enter your first card: ')
c2=input('Enter your second card: ')
c3=input('Enter your third card: ')
user_cards=c1,c2,c3

def bljk(cards):
    a=[]
    total=0
    dic={'A':1,'J':10,'Q':10,'K':10}
    for c in cards:
        a.append(c)
    for b in a:        
        try:
            int(b)
            total+=int(b)
        except:
            b=dic[b.upper()]
            total+=b
    if total<17:
        return f"{total} 'Hit!'"    
    elif total ==21:
        return f"{total} 'BLACKJACK!'"
    elif total >=17:
        return f"{total} 'Stay'"
    

print(bljk(user_cards))

