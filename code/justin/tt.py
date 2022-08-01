with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    for num, line in enumerate(lines):
        if num == 5:
            print(line)
        print(num, line)