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
    
print(contact_list) 
