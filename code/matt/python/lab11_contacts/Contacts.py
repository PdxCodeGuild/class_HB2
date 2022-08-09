#Matt Nichols
#Lab11 contacts

#VERSION 1

lines_for_looks = "--------------------"

def go_contacts():
    contacts_list = []

    with open('C:/Users/mudbo/programmingHB2/class_HB2/code/matt/python/lab11_contacts/contacts.csv', 'r') as file_handle:
        data = file_handle.read().split('\n')

    #Taking the headers and spliting them up into their own elements
    headers = data[0]
    headers = headers.split(',')

    #Grabbing the individuals data and spliting them up into their own elements
    for lines in range(1, len(data)):
        contact = data[lines].split(',')
        
        #Taking the split elements and turning them into lists of dictionaries
        contacts_list.append(dict(zip(headers, contact)))
    return contacts_list

#Test and it prints as expected
print(go_contacts())

#[{'first': 'Matt', 'last': 'Nichols', 'age': '23'},
#{'first': 'Caleb', 'last': 'Nichols', 'age': '16'},
#{'first': 'Trevor', 'last': 'Nichols', 'age': '30'},
#{'first': 'Nic', 'last': 'Nichols', 'age': '32'},
#{'first': 'Randy', 'last': 'Nichols', 'age': '55'},
#{'first': 'William', 'last': 'Nichols', 'age': '12'},
#{'first': 'Joy', 'last': 'Nichols', 'age': '50'}]

#Version 1 complete
print(lines_for_looks)
print(lines_for_looks)
print(lines_for_looks)
print(lines_for_looks)
print(lines_for_looks)
#Version 2 AND 3 below

#Using function from version 1 as suggested
def crud():

    contacts = go_contacts()

    #User input for our CRUD
    CRUD = input("Please make a selection from the following choices down below\nType 'c' to create a new contact\nType 'r' to retrieve an existing contact\nType 'u' to update an existing contact\nType 'd' to delete an existing contact\n").lower()
    lines_for_looks = '--------------------'

    print(lines_for_looks)

    #Creating a new contact
    if CRUD == 'c':

        #With the '''a''' we are making sure to append to the file, not just overwrite it
        with open('C:/Users/mudbo/programmingHB2/class_HB2/code/matt/python/lab11_contacts/contacts.csv', 'a') as file_handle:

            #Inputs for user
            first = input("Enter the first name of new contact: ")
            last = input("Enter the last name of new contact: ")
            age = input("Enter the age of new contact: ")

            #Now we are using the write method, along with creating a new line and making sure they are spaced out properly
            file_handle.write(f'\n{first},{last},{age}')
        

    #Retrieving a current contact (IF said contact exists)
    elif CRUD == 'r':

        #Searching for name
        search = input("Enter the first name of the person you would like to find\n")

        #For loop to run thru the list of contacts and try to pair the given name with it's key 'first'
        for lines in range(len(contacts)):
            if search == contacts[lines]['first']:
                print(contacts[lines])
                break

            #Zilch pairs
        else:
            print("Sorry, there is no person with that name in our system")
            
    #UPDATE
    elif CRUD == 'u':

        #Searching for name
        search = input("Please enter the first name of the contact you would like to update\n")
        
        #For loop to run thru the list of contacts and try to pair the given name with it's key 'first'
        for lines in range(1, len(contacts)):
            if search == contacts[lines]['first']:

                #IF there is a pair we'll open the file
                with open('C:/Users/mudbo/programmingHB2/class_HB2/code/matt/python/lab11_contacts/contacts.csv', 'rt') as file_handle:
                    data = file_handle.read()

                    #Letting the user choose which attribute they would like to update
                    update_attribute = input("Please make a selection from the following choices down below\nType 'f' to update contacts first name\nType 'l' to update contacts last name\nType 'a' to update contacts age\n")
                    
                    #update to first name
                    if update_attribute == 'f':
                        update_first = input('Make edit to first name now\n')
                        data = data.replace(contacts[lines]['first'], update_first)
                    
                    #update to last name
                    elif update_attribute == 'l':
                        update_last = input('Make edit to last name now\n')
                        data = data.replace(contacts[lines]['last'], update_last)
                    
                    #update to age
                    elif update_attribute == 'a':
                        update_age = input('Make edit to age now\n')
                        data = data.replace(contacts[lines]['age'], update_age)
                    
                    #The person can't read and sadly, inputs the wrong information
                    else:
                        print("Sorry, your input didn't match the options presented.")
                    file_handle.close()
                    
                    #updating the information
                    file_handle = open('C:/Users/mudbo/programmingHB2/class_HB2/code/matt/python/lab11_contacts/contacts.csv', 'wt')
                    file_handle.write(data)
                    file_handle.close()
                    break        
        else:
            print("Sorry, there is no person with that name in our system")   

    
    #DELETE
    elif CRUD == 'd':
        

        #Searching for name
        search = input("Please enter the first name of the contact you would like to delete\n")
        
        #For loop to run thru the list of contacts and try to pair the given name with it's key 'first'
        for lines in contacts:
            if lines['first'] == search:
                contacts.remove(lines)

        #Exceptions for when there is no longer a name that matches what was given below       
        try:
            with open('C:/Users/mudbo/programmingHB2/class_HB2/code/matt/python/lab11_contacts/contacts.csv', 'w') as file_handle:
                file_handle.write("first,last,age\n")
                for lines in contacts:
                    first = lines["first"]
                    last = lines["last"]
                    age = lines["age"]
                    file_handle.write(f'{first},{last},{age}\n')
        except:
            print("Name Deleted")
                
    else:
        print("Invalid selection.")

def whole_thing():
    go_contacts()
    crud()

whole_thing()

#VERSION 2 AND 3 COMPLETED