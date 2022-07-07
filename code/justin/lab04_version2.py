'''
Justin Young
Lab 04
Version2
'''

 
c1=input('Enter your first card: ')
c2=input('Enter your second card: ')
c3=input('Enter your third card: ')
user_cards=c1,c2,c3

def bljk(cards):
    a=[]
    total_1=0
    total_2=0
    dic={'a':11,'A':1,'J':10,'Q':10,'K':10}
    for c in cards:
        a.append(c)
    for b in a:        
        try:
            int(b)
            total_1+=int(b)
            total_2+=int(b)
        except:
            if b.upper() =='A':
                total_1+=dic[b.upper()]
                total_2+=dic[b.lower()]
            else:
                b=dic[b.upper()]            
                total_1+=b
                total_2+=b
    print(total_1, total_2)
    if total_1==total_2:  
        if total_1<17:
            return f"{total_1} 'Hit!'"    
        elif total_1 ==21:
            return f"{total_1} 'BLACKJACK!'"
        elif total_1 >21:
            return f"{total_1} 'BUSTED!!!!'"
        elif total_1 >=17:
            return f"{total_1} 'Stay'"
    else:
        if total_2<17:
            return f"{total_1} or {total_2} 'Hit!'"    
        elif total_2 ==21:
            return f"{total_1} or {total_2} 'BLACKJACK!'"
        elif total_2 >21:
            return f"{total_1} or {total_2} 'BUSTED!!!!'"
        elif total_2 >=17:
            return f"{total_1} or {total_2} 'Stay'"
    

print(bljk(user_cards))
