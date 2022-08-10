def version1():
    with open('contacts.csv', 'r') as file:
        lines = file.read().split('\n')
    contacts = []
    index = 1
    headers = lines[0].split(",")

    while index < len(lines):
        contact = lines[index].split(",")
        contacts.append(dict(zip(headers, contact)))
        index += 1

    return contacts


def version2_3():
    contacts = version1()
    query_type = input("What would you like to do?\nCreate\nRetrieve\nUpdate\nDelete\n> ")

    if query_type == 'Create':
        with open('contacts.csv', 'a') as file:
            name = input("What is the contact's name? ")
            phone = input("What is the contact's phone? ")
            email = input("What is the contact's email? ")
            file.write(f'\n{name}, {phone}, {email}')

    elif query_type == 'Retrieve':
        name = input("What is the contact's name you would like to find? ")
        index = 0

        while index < len(contacts):
            if name == contacts[index]['Name']:
                return print(contacts[index])
            index += 1
        else:
            return print("User not found.")

    elif query_type == 'Update':
        name = input("What is the contact's name you would like to update? ")
        index = 0

        while index < len(contacts):
            if name == contacts[index]['Name']:
                with open('contacts.csv', 'rt') as file:
                    data = file.read()
                    update_type = input('Would you like to update their Name, Phone, or Email? ')
                    
                    if update_type == 'Name':
                        name_change = input('What should their name change to? ')
                        data = data.replace(contacts[index]['Name'], name_change)
                    elif update_type == 'Phone':
                        phone_change = input('What should their phone number be? ')
                        data = data.replace(contacts[index]['Phone'], phone_change)
                    elif update_type == 'Email':
                        email_change = input('What should their email be? ')
                        data = data.replace(contacts[index]['Email'], email_change)
                    else:
                        print('Not a valid selection.')
                    file.close()
                    file = open('contacts.csv', 'wt')
                    file.write(data)
                    file.close()
                    
            index += 1
        
    elif query_type == 'Delete':
        name = input("What is the contact's name you would like to delete? ")
        index = 0

        while index < len(contacts):
            if name == contacts[index]['Name']:
                del contacts[index]
                data = f"{','.join(contacts[0].keys())}\n" 
                for dict in contacts:
                    data = data + f"{','.join(dict.values())}\n"
            index += 1
        file = open('contacts.csv', 'wt')
        file.write(data)
        file.close
                
    else:
        print("Invalid selection.")

def main():
    #version1()
    version2_3()

main()