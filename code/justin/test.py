
class Phonebook:
    def __init__(self, name, phone, state, spirit_animal):
        self.name = name
        self.phone = phone
        self.state = state
        self.spirt_animal = spirit_animal
# contact_list = []
# strings_list = ''
# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n')
#     for line in lines:
#         contact_list.append(line.split(','))
#     for contact in contact_list:
#         for variable in contact:
            

j = Phonebook('John', 6016341458, 'MS', 'donkey')
print(type(j.name))

