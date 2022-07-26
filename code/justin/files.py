from hashlib import new


contacts=[]
keys=[]
ncontacts=[]
dic={}
p=1
new_entry = []
n = input('enter a name: ')
new_entry.append(n)
ph = input('enter a phone number: ')
new_entry.append(ph)
st = input(f'enter {n}\'s state: ')
new_entry.append(st)
sa = input(f'enter {n}\'s spirit animal: ')
new_entry.append(sa)
with open('contacts.csv', 'a') as file:
    for x in new_entry:
        file.write(f'\nx')


# with open('contacts.csv', 'a') as file:
#     new_entry = str(new_entry)
#     contacts.csv.write(new_entry)

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    for l in lines:
        contacts.append(l.split(','))
    for c in contacts[0]:
        keys.append(c)
    contacts.append(new_entry)    
    while p < len(contacts):
        a = dic.copy()
        for k in keys: # k is contacts[0](headers.csv) iterated over
            for c in contacts[p]: # c is each contacts information iterated over
                x = contacts[p].index(c)
                contacts[p].pop(x)
                a[k] = c                
                break
        p+=1
        ncontacts.append(a)    
        
print(contacts)
print(ncontacts) 

