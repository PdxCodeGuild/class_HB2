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

def version2():
    
    query_type = input("What would you like to do?\nCreate\nRetrieve\nUpdate\nDelete\n> ")

    if query_type == 'Create':
        with open('contacts.csv', 'a') as file:
            name = input("What is the contact's name? ")
            phone = input("What is the contact's phone? ")
            email = input("What is the contact's email? ")
            file.write(f'\n{name}, {phone}, {email}')
            
    elif query_type == 'Retrieve':
        contacts = version1()
        name = input("What is the contact's name? ")
        index = 0 

        while index < len(contacts):
            if name == contacts[index]['Name']:
                return print(contacts[index])
            index += 1
        else:
            return print("User not found.")
    
    #elif query_type == 'Update':
        
    #elif query_type == 'Delete':
        
    #else:
    
def version3():
    
    return 0

def main():
    #version1()
    version2()

main()