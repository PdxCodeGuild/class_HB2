# This combines version 2 and 3

class ContactList:

    contacts = {}

    def __init__(self):
      
        with open('contacts2.csv', 'r') as file: # open the file
            lines = file.read().split('\n') #when encounter a new line character, store into lines variable

        header = lines[0].split(',')

        contacts_list = []

        for line in lines:
            contacts_dict = {}
            elements = line.split(',')
            for i in range(len(header)):
                contacts_dict.update({header[i]: elements[i]})
            contacts_list.append(contacts_dict)
        contacts_list.pop(0)
        self.contacts = contacts_list

    def create_record(self):
        name = input("What is the name?")
        email = input("What is the email?")
        phone = input("what is the phone number?")

        newrecord = {"name": name, 
                    "email": email, 
                    "phone": phone
                    }

        self.contacts.append(newrecord)

        with open('contacts2.csv', 'a') as file:
            file.write(f'\n{name},{email},{phone}')
    
    def print_list(self):
        print(self.contacts)


    def retrieve_record(self):
        search_name = input("What name are you searching for?")
        for i in self.contacts:
            if i['name'].lower() == search_name.lower():
                print(i)

    def update_record(self):
        search_name = input("Which name do you want to update?")
        updated_attribute = input("Which field do you want to update? Options are name, email, phone.")
        change_attribute = input("What do you want to update the field to be?")
        for i in self.contacts:
            if i['name'].lower() == search_name.lower():
                i[updated_attribute.lower()] = change_attribute     

        # print(self.contacts)

        with open('contacts2.csv', 'w') as file:
            file.write("name,email,phone\n")
            for i in self.contacts:
                name = i["name"]
                email = i["email"]
                phone = i["phone"]
                file.write(f'{name},{email},{phone}\n')

    def delete_record(self):
        search_name = input("Which contact do you want to delete? Enter their name")
        for i in self.contacts:
            if i['name'].lower() == search_name.lower():
                self.contacts.remove(i)

        with open('contacts2.csv', 'w') as file:
            file.write("name,email,phone\n")
            for i in self.contacts:
                name = i["name"]
                email = i["email"]
                phone = i["phone"]
                file.write(f'{name},{email},{phone}\n')

contacts_test = ContactList()
while True:
    command = input('Enter a command: ')
    if command == 'retrieve':
        contacts_test.retrieve_record()
        print("Record retrieved")
    elif command == 'create':
        contacts_test.create_record()
        print("Record created")
    elif command == 'update':
        contacts_test.update_record()
        print("Record updated")
    elif command == 'delete':
        contacts_test.delete_record()
        print("Record deleted")
    elif command == 'help':
        print('Available commands:')
        print('retrieve  - retrieve a record')
        print('create  - create a record')
        print('update - update a record')
        print('delete - delete a record')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')