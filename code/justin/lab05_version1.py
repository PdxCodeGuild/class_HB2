'''
Justin Young
Lab 05
Version1&2
'''


def ticket():
    import random
    ticket=[]
    while len(ticket)<6:
        ticket.append(random.randint(1,99))
    return ticket

def matching(a,b):
    running_num=0
    if a[0]==b[0]:
        running_num+=1
    if a[1]==b[1]:
        running_num+=1
    if a[2]==b[2]:
        running_num+=1
    if a[3]==b[3]:
        running_num+=1
    if a[4]==b[4]:
        running_num+=1
    if a[5]==b[5]:
        running_num+=1
    return running_num        

def lottery():
    winner = ticket()
    times=0
    a = 0
    total_win = 0
    while times<1000:
        a = matching(winner,ticket())
        if a == 1:
            total_win+=4
        elif a ==2:
            total_win+=7
        elif a ==3:
            total_win+=100
        elif a ==4:
            total_win+=50000
        elif a ==5:
            total_win+=1000000
        elif a ==6:
            total_win+=25000000            
        times+=1      
    return f'${times*2} invested ${total_win} earned \nROI {(total_win-(times*2))/(times*2)}'  
print(lottery())
