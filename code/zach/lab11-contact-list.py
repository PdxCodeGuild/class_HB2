def version1():
    with open('contacts.csv', 'r') as file:
        lines = file.read().split('\n')
        #print(lines)
    
    index = 1
    headers = lines[0].split(",")
    
    while index < len(lines):
        contact = lines[index].split(",")
        print(dict(zip(headers, contact)))
        index += 1

def version2():
    
    return 0

def version3():
    
    return 0

def main():
    version1()

main()