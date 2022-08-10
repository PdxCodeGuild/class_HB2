
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
  

contact_list = []

headers = lines[0].split(',') 
print('headers here',headers)

rows = lines[1:] #skips first row in zero spot
print('rows here:', rows)

for row in rows:
    column = row.split(',') 
    contact_list.append(dict(zip(headers, column)))
print('contactlist here:', contact_list) 

def create_new(contacts):
    new_user = {

    }
    for header in headers:
        new_user[header]=input(f'please enter your {header}: ')
    
    contacts.append(new_user)
    print('create new here:', contact_list)
    return contacts 
    


def retrieve(contacts):
    search_name = input('Enter a name to search for: ')
    
    print('search name:', search_name)
    for contact in contacts:   
        if search_name == contact["name"]:
           return contact
        else:
            print('search name is not contact')



def update(contacts):
    contact_update = retrieve(contacts)
    user_input = input('which would you like to update: "Name", "Favorite fruit", "Favorite color:"')
    new_attribute = input(f'What would you like to update {user_input} to ')
    contact_update[user_input] = new_attribute
    print(contact_update)
    return contacts

def delete(contacts):
    contact_delete = retrieve(contacts)
    confirm = input('are you sure yes or no: ').lower()
    if confirm == 'yes':
        contacts.remove(contact_delete)
        return contacts
    elif confirm == "no":
        return contacts


def convert_to_csv(contacts):  #.join
    csv_output = []
    csv_output.append(headers)
    for contact in contacts:
        csv_output.append(list(contact.values())) #list creates a list object. .Values() eturns a view object. The view object contains the values of the dictionary, as a list
    print('csv output', csv_output)
    csv_output = [",".join(line) for line in csv_output]
    csv_output = "\n".join(csv_output)
    with open('contacts.csv', 'w') as f:
        f.write(csv_output)





while True:
    choice = input('choice one of the follow : "create", "retrieve" , "update" or "delete": ')
    if choice == "create":

        create_new(contact_list)

    elif choice == "retrieve":
        print('retreive something:' )

        print(retrieve(contact_list))

    elif choice == "update":
  
        update(contact_list)

    elif choice == "delete":
        delete(contact_list)
    else:
        break 
    convert_to_csv(contact_list)