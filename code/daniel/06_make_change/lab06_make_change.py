import csv

# with open('location.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['City', 'State', 'Zip'])
#     writer.writerow(['Portland', 'OR', '97202'])
#     writer.writerow(['Lake Oswego', 'OR', '97304'])


with open('location.csv') as file:
    reader = csv.reader(file)
    print(list(reader))

    for row in reader:
        print(row)