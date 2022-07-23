# with open('example.txt', 'a') as file:
#     text = file.write('\nHappy birthday')
# print(text)


#older approach
# file = open('example2.txt', 'w')
# text = file.write('Legacy Method')
# print(text)
# file.close()

# with open('colors.txt') as file:
#     # colors= file.read()
    
#     # chaining the split(), returns list
#     colors = file.read().split() #['red', 'blue]
    
#     for color in colors:
#         print(color)





#identify colors that have more than 4 chars
# with open('colors.txt') as file:
#     colors = file.read().split(', ')
    
# with open('colors4.txt', 'w') as file4:
#     for color in colors:
#         if len(color)>4:
#             file4.write(color + '\n') 

# import datetime 

# #Read file
# start = datetime.datetime.now()
# with open('phonebook.txt') as file:
#     phone_book = file.read()
# end = datetime.datetime.now()

# print(f'Your file loaded in {end-start}')

with open('phonebook.txt') as file:
    phone_book = file.read()

    phone_book = phone_book.split('\n')
    name = input('Lookup name: ')
    
    found_entry = False
    for entry in phone_book:
        # if name in entry: #Tomas --> Tom
        if name.lower() in entry.lower():
            print(entry)
            found_entry = True
    
    if not found_entry:
        print('Contact not found')  
        name = input('Enter new contact name: ')
        phone_number = input(f'Enter the number for:  {name}')
        
        phone_book.append(name + " " + phone_number)
        
        phone_book.sort()
        with open('phonebook2.txt', 'w') as file2:
            file2.write('\n'.join(phone_book))
        
# print(type(phone_book))
# print(phone_book)
