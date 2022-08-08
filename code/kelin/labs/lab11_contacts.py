# Kelin Ray

# Lab 11: Contact List


# Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. 

# Headers might consist of `name`, `favorite fruit`, `favorite color`. Open the CSV, convert the lines of text into a **list of dictionaries**, one dictionary for each user. 

with open('contacts.csv', 'r') as file:
    csv_list = file.read().split('\n') # Reads csv file by line

header = csv_list[0].split(',') # Seperates each line by a comma

contacts_list = [] # Creates contacts list

for line in csv_list: 
    contacts_dict = {} # Creates contacts dictionary
    elements = line.split(',') # Seperates each element by a comma
    for i in range(len(header)):
        contacts_dict.update({header[i]: elements[i]}) # Converts the lines of text into a list of dictionaries
    
    contacts_list.append(contacts_dict) # Adds contacts list to the list of dictionaries

contacts_list.pop(0) # Deletes the header from the dictionaries

for lines in contacts_list:
    print(lines) # Output:

# {'Name': 'Dad', ' Phone': ' 703-8287', ' City': ' Kelso', ' Color': ' Gold', ' Fruit': ' Apple'}
# {'Name': 'Mom', ' Phone': ' 431-1010', ' City': ' Kalama', ' Color': ' Pink', ' Fruit': ' Banana'}
# {'Name': 'Grandma', ' Phone': ' 577-6416', ' City': ' Longview', ' Color': ' Blue', ' Fruit': ' Peach'}

# ## Version 2

# Implement a CRUD REPL


with open('contacts2.csv', 'a') as file:
    name = input('Enter a name: ')
    phone_number = input(f"Enter {name}'s phone number: ") # Add a new contact to your contact list with the attributes that the user entered.
    city = input(f"Enter {name}'s city: ")
    color = input(f"Enter {name}'s favorite color: ")
    fruit = input(f'Enter a fruit: ')
    file.write(f'\n{name},{phone_number},{city},{color},{fruit}') # Writes inputs to the csv file


with open('contacts2.csv') as file:
    phone_book = file.read()
    phone_book = phone_book.split('\n')
    name = input('Lookup name: ') # User enters name to look up contact

    found_entry = False

    for entry in phone_book:

        if name.lower() in entry.lower():
            print(entry) # Prints information for contact
            found_entry - True
    if not found_entry:
        print('Contact not found')

        name = input('Enter new contact name: ') # Adds a new contact to your contact list with the attributes that the user entered.
        phone_number = input(f'Enter the number for: {name}')
        phone_book.append(name + " " + phone_number)

        phone_book.sort()
        with open('contacts2.csv', 'w') as file2:  # "phonebook": update
            file2.write('\n'.join(phone_book))

        
        name = input("Enter a name to update: ")


        with open('contacts2.csv', 'rt') as file:
            data = file.read()
            update_type = input('What would you like to update?: ') # Asks the user for the contact's name, then for which attribute of the user they'd like to update and the value.
                    
            if update_type == 'name':
                name_change = input('Enter a new name: ')
                data = data.replace(contacts[index]['Name'], name_change)
            elif update_type == 'phone':
                phone_change = input('Enter a new number: ')
                data = data.replace(contacts[index]['Phone'], phone_change)
            elif update_type == 'city':
                email_change = input('Enter the new city: ')
                data = data.replace(contacts[index]['Email'], email_change)
            else:
                print('Not a valid selection.')
                file.close()
                file = open('contacts2.csv', 'wt')
                file.write(data)
                file.close()

# - **D**elete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

# ## Version 3

# When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup `contacts.csv` because you likely won't write it correctly the first time.
#  {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# ]
# ```

# *Note: There is a `csv` library in Python that will do much of this for you. It is what you would use normally in a project, but for this lab you need to write all the logic yourself.*