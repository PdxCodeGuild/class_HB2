class PhoneBook:
    # attributes, characteristics
    def __init__(self):
        self.contacts = [] #list of contacts
        self.path = '' #path to csv
        self.headers = [] #stored headers


    def load(self, path):
        """
        returns a list of dictionaries representating a contact list csv
        reads csv
        """
        self.path = path #set path
        with open(self.path) as f:
            lines = f.read().split('\n')

        # process csv into list of dictionaries
        self.headers = lines[0].split(',')
        for i in range(1, len(lines)):
            row = lines[i].split(',')
            contact = dict(zip(self.headers, row))
            self.contacts.append(contact)
        return len(self.contacts)

    def count(self):
        """return the length of self.contacts"""

        return len(self.contacts)

    def save(self):
        """
        1) open 'self.file' with open 'w' for write
        2) convert the dictionaries into lines
        3) & write each line into to the file
        """
        lines = []
        for contact in self.contacts:
            lines.append( ",".join(list(contact.values())))

        with open(self.path, 'w') as phone_book_file:
            phone_book_file.write('\n'.join(lines))


    def print(self):
        """
        loop over self.contacts
        print the information for each contact
        """
        for contact in self.contacts:
            print(contact)

    def add(self, name, phone_number, state):
        """
        create a new dictionary
        add the new dictionary to self.contacts
        """

        new_contact = {
            "name": f"{name}",
            "phone_number": f"{phone_number}",
            "state": f"{state}"
        }

        self.contacts.append(new_contact)

    def remove(self, name):
        """
        find the contact in self-contacts with the given name
        remove the element at that index
        """
        for i in self.contacts:
            if i["name"] == name:
                self.contacts.remove(i)

    def update(self, old_name, new_name, new_phone_number, new_state):
        """
        find the contact in self.contacts with the given old_name
        set that contacts' name, phone number, etc to the given values
        """
        for i in self.contacts:
            if i["name"] == old_name:
                self.add(new_name, new_phone_number, new_state)
                self.remove(old_name)
