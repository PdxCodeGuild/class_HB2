# with open('location.csv', 'w') as file:
#         file.write("Hello World")
        
# # with open(file, 'r') as f:
# #     contents = f.readlines()
# #     print(contents)

# with open(file, 'r') as f:
#     for line in f:
#         list.append(line)
        
# phonebook = {'Dave': '42342', 'Alice': '234234'}
# with open(file, 'w') as location:
#     for name, number in location.items():
#         line = f'{name}{number}\n'
#         location.write(line)



#CSV = comma separated values

# with open('contacts.csv', 'w') as file:
#     lines = file.read().split('\n')
#     print(lines)
    
contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple', 'favorite color':'purple'},
    {'name': 'teeto', 'favorite fruit':'lychee', 'favorite color':'brown'}
]
    
f = open('contacts.csv')

with open('contacts.csv', 'r') as contacts:
    contacts_data = contacts.read().split('\n')
    
dict = []
for line in contacts_data:
    dict.append(contacts_data)
    