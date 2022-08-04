
#==========================================================

# contact_info = {'David': '5551234', 'Alice': '6662345'}
# with open('phonebook.txt', 'w') as phone_book_file:
#     for name, number in phonebook.items():
#         line = f'{name} {number}\n'
#         phone_book_file.write(line)


#==========================================================

# with open('phonebook.txt') as phone_book_file:
#     phone_book_data = phone_book_file.read().split('\n')

# phone_book = {}
# for line in phone_book_data:
#     name, number = line.split()
#     phone_book[name] = number

#==========================================================
# Version1
#==========================================================

import pprint

with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
    # print('lines: ', lines)

contacts_list = []

headers = lines[0].split(",")
# print("headers: ", headers)

for l in range(1, len(lines)):
    if ',' not in lines[l]:
        continue
    the_name, the_favorite_fruit, the_favorite_color = lines[l].split(",")

    # print(name, favorite_fruit, favorite_color)
    
    contact_dict = {
        headers[0]: the_name,
        headers[1]: the_favorite_fruit,
        headers[2]: the_favorite_color

    }
    # print(contact_dict)

    contacts_list.append(contact_dict)
pprint.pprint(contacts_list)

    # contacts['name'] = name
    # contacts['favorite_fruit'] = favorite_fruit
    # contacts['favorite_color'] = favorite_color

# print(contacts)

#==========================================================
# Version2
#==========================================================

def record():
    get_name = input("Add a name to the contact list: ")
    get_fruit = input(f"What is {get_name}'s favorite fruit?: ")
    get_color = input(f"What is {get_name}'s favorite color?: ")
    contacts_list.append({
        headers[0]: get_name,
        headers[1]: get_fruit,
        headers[2]: get_color
    })
    # write()

def write():
    with open('contact_list.csv', 'w') as file:
        file.write(f'{headers[0]}, {headers[1]}, {headers[2]}\n')
        for contact in contacts_list:
            file.write(f'{contact[headers[0]]}, {contact[headers[1]]}, {contact[headers[2]]}\n')

   
# record()
# print(contacts_list)



def retrieve():
    lookup_name = input("Enter a username: ")
    for contact in contacts_list:
        if lookup_name == contact[headers[0]]:
            print(contact)
            break
# retrieve()


def delete():
    delete_user = input("What contact do you want to delete?: ")
    contacts_list_copy = contacts_list.copy()
    for i in range(len(contacts_list_copy)):
        if delete_user == contacts_list_copy[i][headers[0]]:
            del contacts_list[i]
            break
    # write()
# delete()
 


def update():
    pick_contact = input("Pick a contact to update: ")
    for index in range(len(contacts_list)):
        if pick_contact == contacts_list[index]['name']:
            update_info = input("What would you like to update? name, color, or fruit?")
            if update_info == 'name':
                contacts_list[index]['name'] = input("Enter a name: ")
    return contacts_list
                # write()
while True:
    print("""
    -Type 1 to create
    -Type 2 to retrieve
    -Type 3 to update
    -Type 4 to delete
    """)
    user = input()

    if user == "1":
        pass
        # create()
    if user == "2":
        # retrieve()
        pass
    if user == "3":
        print(contacts_list)
        print(retrieve(update_info))
    # for contact in contacts_list:
    # if pick_contact == contact['name']:
    #     update_info = input("What would you like to update? name, color, or fruit?")
    #     if update_info == 'name':
    #         new_name = input("Type a new name to replace the old contact name: ")
    #         contacts_list = contacts_list.replace(contact['name'], new_name)

# update()
#==========================================================
#==========================================================


            

# with open('contact_list.csv', 'r') as file:
#     lines = file.write(get_info)


#==========================================================
# Version3
#==========================================================


