with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines, 'lines')


headers = lines[0].split(',') #getting the keys by themselves
print('headers: ', headers)

rows = lines[1:] #values by themselves. need to find more of an explination of [1:] splicing methon\d


# print('answers: ', answer)
# list = {}
for row in rows:
    column = row.split(',')
    # print(column)
    #HEADER:COLUMN  D = dict(zip(keys, values))
    d = dict(zip(headers, column))
    print(d)
 
