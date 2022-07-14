person = {'first_name': 'Bruce', 'last_name':  'Wayne', 'age': 25
          }
# print(person['first_name'])
# print(person['fav_color'])
person['fav_color'] = 'blue'
person['fav_color'] = 'red'
person.update({'first_name': 'Robin', 'age': 33, 'weight': 200})
#
# print(person['DOB'])
# print(person.get('DOB', 'Not found'))

#keys(), values(), items()
#finding all keys from dict
attributes = person.keys()
# print(attributes, 'print key attr')

#find all values
values = person.values()
# print(values, 'printing values')

#key/value pairs
pairs = person.items()
# print(pairs, 'key/value')

#print the keys
# for x in person:
#     print(x)

#print keys and values 
# for key, value in person.items():
#     print(key, value)
    
    
    #append data to contacts list
    # contacts.append(name)
    # contacts.append(phone_number)
    # contacts.append(fav_color)
    
    
# contacts = []
# while True:
#     name = input('Enter a name of contact: ')
#     phone_number =input(f"Enter {name}'s phone number: ")
#     fav_color = input(f"Enter {name}'s favorite color: ")
    
#     contacts.append({
#         'name': name, 'phone_number': phone_number, 'fav_color': fav_color
#     })
    
#     additional_data = input('Enter another contact? y/n')
#     if additional_data =='n':
#         break
# print(contacts)


contacts = [
    {'name': 'Susan', 'phone_number': 5555555555, 'fav_color': 'green'},
    {'name': 'Bob', 'phone_number': 555555885, 'fav_color': 'blue'},
    {'name': 'Tom', 'phone_number': 4555555555, 'fav_color': 'yellow'}
    
]


# print(contacts, 'entire list of dicts')
# for contact in contacts:
#     print(contact['name'], 'values from key')
    
# for contact in contacts:
#     if contact['name'] == 'Susan':
#         print(contact['name'], 'conditional value')

while True:
    #show menu to user
    choice = input('Choose: add, search, update, delete ')
    #if user keys 'add', prompt for new contact info
    if choice == 'add':
        name = input('Enter a name of contact: ')
        phone_number =input(f"Enter {name}'s phone number: ")
        fav_color = input(f"Enter {name}'s favorite color: ")
        
        #append contact info to the contacts list
        contacts.append({
        'name': name, 'phone_number': phone_number, 'fav_color': fav_color
        })
    
    elif choice == 'search':
        search_name = input('Enter contact name ').lower()
        #loop over all contacts
        for contact in contacts:
            #if search  name matches name in contact, print info
            if contact['name'].lower() == search_name:
                print(contact['name'])
                print(contact['phone_number'])
                print(contact['fav_color'])
                
    elif choice == 'update':
        search_name = input('Enter contact name: ').lower()
        #loop over contacts dictionary
        for contact in contacts:
            if contact['name'].lower() == search_name:
                #check if name is correct
                correct = input(f"Is {contact['name']} correct? y/n")
                # if not correct, ask for data
                if correct == 'n':
                    name = input(f"Enter new/revised name for contact")
                    contact['name'] = name
                #check if phone number is correct
                correct = input(f"Is {contact['phone_number']} correct? y/n")
                # if not correct, ask for data
                if correct == 'n':
                    phone_number = input(f"Enter new/revised phone_number for contact")
                    contact['phone_number'] = phone_number
                #check if fav_color  is correct
                correct = input(f"Is {contact['fav_color']} correct? y/n")
                # if not correct, ask for data
                if correct == 'n':
                    color = input(f"Enter new/revised color for contact")
                    contact['fav_color'] = color
                
                #show updated contact info
                print(contact['name'])
                print(contact['phone_number'])
                print(contact['fav_color'])
                          
    elif choice == 'delete':
        for i, contact in enumerate(contacts):  #[i = 0{susan}, i = 1 {bob}]
            print(f" {i} - {contact['name']}")
        index = input('Enter the number of the contact u want 2 delete: ')
        remove_contact = contacts.pop(int(index))
        
        
    additional_data = input('Enter another contact? y/n ')
    if additional_data =='n':
        break
    
print(contacts)
