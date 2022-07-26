
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
    the_name, the_favorite_fruit, the_favorite_color = lines[l].split(",")
    # print(name, favorite_fruit, favorite_color)
    
    contact_dict = {
        headers[0]: the_name,
        headers[1]: the_favorite_fruit,
        headers[2]: the_favorite_color

    }
    print(contact_dict)

    contacts_list.append(contact_dict)
pprint.pprint(contacts_list)

    # contacts['name'] = name
    # contacts['favorite_fruit'] = favorite_fruit
    # contacts['favorite_color'] = favorite_color

# print(contacts)

#==========================================================
# Version2
#==========================================================

# def record():
#     get_info = []
#     get_name = input("Add a name to the contact list: ")
#     get_fruit = input(f"What is {get_name}'s favorite fruit?: ")
#     get_color = input(f"What is {get_name}'s favorite color?: ")
#     get_info.append(get_name)
#     get_info.append(get_fruit)
#     get_info.append(get_color)
#     # print(get_info)
    
# record()

# with open('contact_list.csv', 'r') as file:
#     lines = file.write(get_info)


#==========================================================
# Version3
#==========================================================