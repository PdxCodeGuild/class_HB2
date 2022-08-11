with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines, 'lines')


headers = lines[0].split(',') #getting the keys by themselves
# print('headers: ', headers)

rows = lines[1:] #values by themselves. [1:] splicing methon\d

contact_list = []

for row in rows:
    column = row.split(',') #the .split('.') is getting what was in rows and spliting them with commas 
    # print(column)
    #HEADER:COLUMN  D = dict(zip(keys, values))
    contact_list.append(dict(zip(headers, column)))
    
print('contacts before add ', contact_list) 

def create_new(contacts):
    new_user = {

    }
    for header in headers:
        new_user[header]=input(f'please enter your {header}: ')
    # print(new_user)
    contacts.append(new_user)
    return contacts #it saves it and returns that data 

# create_new(contact_list)

print('contacts after add', contact_list)
# print(test)#just outputs the data and doesnt save it 

def retrieve(contacts):
    # search_name = input('Enter a name to search for: ')
    search_name = 'Arturo'
    print('search name:', search_name)
    for contact in contacts:   # contact is a dict and contacts is a list of dict 
        if search_name == contact["Name"]:
            print('search name is the contact: ')
            return contact
        else:
            print('search name is not contact')

contact_to_display = retrieve(contact_list)
print('returning all contacts info', contact_to_display)
# def update():

# def delete():





#for  i in range(1,len(lines)) the one in front would start shit after the 0 indicie

while True:
    choice = input('choice one of the follow : "create", "retrieve" , "update" or "delete" ')
    if choice == "create":
        print()
    elif choice == "retrieve":
        print()
    elif choice == "update":
        print()
    elif choice == "delete":
        print()
    else:
        break 
nums = []
while True:
    num = input('enter number: ')
    if num == 'done':
        break
    nums.append(int(num))
print(nums)