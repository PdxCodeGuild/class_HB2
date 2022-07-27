from hashlib import new


contacts=[]
keys=[]
ncontacts=[]
dic={}
p=1
new_entry = []


while True:
    print('''\nWelcome to our contact database, please select from the following options: 
To create new user enter "create":
To retrive an existing record enter "search":
To update an existing record enter "update":
To delete a record, enter "delete":
When finished, enter"done":''')
    a = input("Enter: ")
    if a.lower() == 'done':
        False
        break
            
    elif a.lower() == 'create':
        print('\nYou selected to enter a new user follow the commands')
        n = input('enter a name: ')
        new_entry.append(n)
        ph = input('enter a phone number: ')
        new_entry.append(ph)
        st = input(f'enter {n}\'s state: ')
        new_entry.append(st)
        sa = input(f'enter {n}\'s spirit animal: ')
        new_entry.append(sa)
        j = ','.join(new_entry)
        with open('contacts.csv', 'a') as file:
                file.write(f'\n{j}')
    elif a.lower() == 'search':
        print('What user are you looking for?')
        n = input('enter name: ')
        with open('contacts.csv', 'r') as file:
            lines = file.read().split('\n')
            for l in lines:
                if n.lower() in l.lower():
                    print(f'User {n} found: \n---------------------------------------------\n{l}')
                    print('---------------------------------------------')
    elif a.lower() == 'update':
        print('What contact do you want to update? ')
        n = input('Enter name: ')        
        fin = open('contacts.csv', 'rt')
        data = fin.read()
        if n.lower() in data.lower():
            print(f'User {n.title()} found')
            for lines in data.split('\n'):
                if n.lower() in lines.lower():
                    lines = lines.split(',')
                    # lines = ','.join(lines)
                    print(lines)
                    chg = input(f'What needs to change, name, phone, state or spirit animal? ')
                    if chg.lower() == 'name':
                        chg = input('Whats the new name? ')
                        data = data.replace(lines[0],chg)
                        fin.close()
                        fin = open('contacts.csv', 'wt')
                        fin.write(data)
                        fin.close()
                    elif chg.lower() == 'phone':
                        chg = input('Whats the new phone? ')
                        lines[1] = chg
                    elif chg.lower() == 'state':
                        chg = input('Whats the new state? ')
                        lines[2] = chg
                    elif chg.lower() == 'spirit animal':
                        chg = input('Whats the new spirit animal? ')
                        lines[3] = chg
                    else:
                        print('not a valid option')
                    lines = (',').join(lines)
                    


        # data = data.replace()
        #     for l in lines:
        #         if n.lower() in l.lower():  
        #             print(f'Contact {l} found.')
        #             spl = l.split(',')
        #             upd = input('What needs updating, name, phone, state, spirit animal? ')
        #             if upd.lower() == 'name'.lower():
        #                 spl[0]
                            


#             print(spl)
            # n = input('what name are we looking for: ')
            # if n.lower() in l[0].lower():
            #         spl = l.split(',')
            #         spl_a = spl.copy()
            #         print(f'{l} \nis the info on file, what needs to change:\nname,phone,state,spirit animal? ')
            #         a = input('Enter what to change: ')
            #         if a.lower() == 'name':
            #             nchg = input('What do you want to change the name to? ')
            #             print(spl_a)
                        

                    # if a.lower() == 'name':
        
# n = input('enter a name: ')
# new_entry.append(n)
# ph = input('enter a phone number: ')
# new_entry.append(ph)
# st = input(f'enter {n}\'s state: ')
# new_entry.append(st)
# sa = input(f'enter {n}\'s spirit animal: ')
# new_entry.append(sa)
# j = ','.join(new_entry)
# with open('contacts.csv', 'a') as file:
#         file.write(f'\n{j}') 
# with open('contacts.csv', 'a') as file:
#     new_entry = str(new_entry)
#     contacts.csv.write(new_entry)

# contacts=[]
# keys=[]
# ncontacts=[]
# dic={}
# p=1
# new_entry = []

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    for l in lines:
        contacts.append(l.split(',')) #makes lists of contacts seperated by , inside of the contacts list
    for c in contacts[0]: #header value for key:
        keys.append(c) #puts the header value into a list by itself called keys
    # contacts.append(new_entry)    
    while p < len(contacts):
        a = dic.copy()
        b = contacts[p].copy()
        for k in keys: # k is contacts[0](headers.csv) iterated over
            for c in b:
                x=b.index(c)
                b.pop(x)
                a[k] = c                
                break
        p+=1
        ncontacts.append(a)    
        
print(contacts)
print(ncontacts) 

