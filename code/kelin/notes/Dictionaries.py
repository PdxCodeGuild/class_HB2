from tkinter import N
from pkg_resources import add_activation_listener


person = {'first_name': 'Bruce', 'last_name': 'Wayne', 'age': 25}

print(person['first_name'])

# Bruce

person['fav_color'] = 'blue'
print(person)

# {'first_name': 'Bruce', 'last_name': 'Wayne', 'age': 25, 'fav_color': 'blue'}

person['fav_color'] = 'red'

print(person)

# {'first_name': 'Bruce', 'last_name': 'Wayne', 'age': 25, 'fav_color': 'red'}

person.update({'first_name': 'Robin', 'age': 33, 'weight': 200})

# {'first_name': 'Robin', 'last_name': 'Wayne', 'age': 33, 'fav_color': 'red', 'weight': 200}

# print(person['DOB'])

print(person.get('DOB', 'Not found'))

#  Not found
#  keys(), values(), items()
#  finding all keys
attributes = person.keys()
print(attributes, 'print key attr')

# dict_keys(['first_name', 'last_name', 'age', 'fav_color', 'weight']) print key attr

values = person.values()
print(values, 'printing values')

# dict_values(['Robin', 'Wayne', 33, 'red', 200]) printing values

pairs = person.items()
print(pairs, 'key/value')

# dict_items([('first_name', 'Robin'), ('last_name', 'Wayne'), ('age', 33), ('fav_color', 'red'), ('weight', 200)]) key/value

for x in person:
    print(x)

# first_name
# last_name
# age
# fav_color
# weight

for key, value in person.items():
    print(key, value)

# first_name Robin
# last_name Wayne
# age 33
# fav_color red
# weight 200

contact = []
while True:

    name = input('Enter a name of contact: ')
    phone_number = input(f"Enter {name}'s phone number: ")
    fav_color = input(f"Enter {name}'s favorite color: ")

# contact.append(name)
# contact.append(phone_number)
# contact.append(fav_color)

# print(contact)

# Enter a name of contact: yo
# Enter yo's phone number: 55
# Enter yo's favorite color: blue
# ['yo', '55', 'blue']

    contact.append ({
        'name': name, 'phone_number': phone_number, 'fav_color': fav_color})

    additional_data = input('Enter another contact y/n')
    if additional_data =='n':
        break
print(contact)

# Enter a name of contact: kelin
# Enter kelin's phone number: 3
# Enter kelin's favorite color: blue
# Enter another contact y/ny
# Enter a name of contact: kelin
# Enter kelin's phone number: 324
# Enter kelin's favorite color: red
# Enter another contact y/nn
# [{'name': 'kelin', 'phone_number': '3', 'fav_color': 'blue'}, {'name': 'kelin', 'phone_number': '324', 'fav_color': 'red'}]

# Enter a name of contact: Kelin 
# Enter Kelin's phone number: 3607038670
# Enter Kelin's favorite color: Blue
# [{'name': 'Kelin', 'phone_number': '3607038670', 'fav_color': 'Blue'}]

# contacts = [{'name': 'Kelin', 'phone_number': '55', 'fav_color': 'Blue'}, {'name': 'Arthur', 'phone_number': '66', 'fav_color': 'Yellow'}, {'name': 'Gracie', 'phone_number': '44', 'fav_color': 'Green'}]

# print(contacts, 'entire list of dicts')

# for contacts in contact:

# print(contact['name'])

# for contacts in contact:
#     if contacts['name'] == 'Kelin':
#         print(contacts['name'], 'conditional value')


while True:
    # Show menu to user
    choice = input('Choose: add, search, updated ')
    # if user keys 'add', prmpt for new contact info
    if choice == 'add':
        name = input('Enter a name of contact: ')
        phone_number = input(f"Enter {name}'s phone number: ")
        fav_color = input(f"Enter {name}'s favorite color: ")
        contact.append({
            'name': name, 'phone_number': phone_number, 'fav_color': fav_color
        })
    elif choice == 'search':
        search_name = input ('Enter contact name').lower()
        # loop over all contacts
        for contact in contacts:
            # if search anme matches print info
            if contact['name'].lower() == search_name:
                print(contact['name'])
                print(contact['phone_number'])
                print(contact['fav_color'])
    elif choice == 'update':
        search_name = input('Enter contact name: ').lower()
        # loop over contacts
        for contact in contacts:
            if contact ['name'].lower() == search_name:
                correct = input(f"is {contact['name']} correct y/n")
                if correct == 'n':
                    name = input(f"Enter new/revised name")
                    contact['name'] = name

                    #  copy for phone number/fav color
                    
        additional_data = input('Enter another contact y/n')
        if additional_data == 'n':
            break

        print(contact)