import PhoneBook

def main():
    phone_book = PhoneBook.PhoneBook()  # create an instance of our class
    print('Welcome to the Phone Book')
    while True:
        command = input('Enter a command: ')
        if command == 'load':
            path = input('Enter the path to your CSV: ')
            phone_book.load(path)
            print(f'Loaded {phone_book.count()} contacts.')
        elif command == 'save':
            phone_book.save()
            print(f'Saved {phone_book.count()} contacts.')
        elif command == 'print':
            phone_book.print()
        elif command == 'add':
            print('Enter info of contact to add:')
            name = input('Name: ')
            phone_number = input('Phone Number: ')
            state = input('state: ')
            phone_book.add(name, phone_number, state)
        elif command == 'remove':
            name = input('Name of contact to remove: ')
            phone_book.remove(name)
        elif command == 'update':
            print('Enter info of contact to add:')
            old_name = input('Name of contact to update: ')
            new_name = input('New Name: ')
            new_phone_number = input('New Phone Number: ')
            new_state = input('New state: ')
            phone_book.update(old_name, new_name, new_phone_number,
                                new_state)
        elif command == 'help':
            print('Available commands:')
            print('load   - load all contacts from the file')
            print('save   - save contacts to a file')
            print('print  - print all contacts')
            print('add    - add a new contact')
            print('remove - remove a contact')
            print('update - update a contact')
            print('q   - quit the program')
        elif command == 'q':
            break
        else:
            print('Command not recognized')


if __name__ == "__main__":
    main()