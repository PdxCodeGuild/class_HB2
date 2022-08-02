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
    
# print(contact_list) 

def create_new():
    new_user = {

    }
    for header in headers:
        new_user[header]=input(f'please enter your {header}: ')
    # print(new_user)
    return new_user #it saves it and returns that data 
print(contact_list)
contact_list.append(create_new())
print(contact_list)
# print(test)#just outputs the data and doesnt save it 
# def retrieve():

# def update():

# def delete():





#for  i in range(1,len(lines)) the one in front would start shit after the 0 indicie