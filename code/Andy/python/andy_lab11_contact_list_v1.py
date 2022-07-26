with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines, 'lines')


headers = lines[0].split(' , ') #getting the keys by themselves
print('headers: ', headers)

answer = lines[1:]
print('answers: ', answer)
# list = {}
# for line in lines:
