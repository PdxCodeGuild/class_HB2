# Lab11 v1

with open('contacts.csv', 'r') as file: # open the file
    lines = file.read().split('\n') # when encounter a new line character, store into lines variable

header = lines[0].split(',')

contacts_list = []

for line in lines:
    contacts_dict = {}
    elements = line.split(',')
    for i in range(len(header)):
        contacts_dict.update({header[i]: elements[i]})
    contacts_list.append(contacts_dict)

contacts_list.pop(0)

for lines in contacts_list:
    print(lines)
