# escape chars
greetings = 'Hello World Can\'t'
print(greetings)

greetings = f''' Hello World Can't'''
print(greetings)

greetings = f'''    Hello This is
                a {2*2} Multi-string'''
print(greetings)

# Hello World Can't
#  Hello World Can't
#     Hello This is
#                 a 4 Multi-string

file_path = r"c:user\programming\python\lab01"
print(file_path)

# c:user\programming\python\lab01

page_break = '--' *50
print(page_break)

# ----------------------------------------------------------------------------------------------------

# slicing methods

file_path = r"c:user\programming\python\lab01"
# item_five = file_path[4]
last_char = file_path[len(file_path) -1]
print(last_char) # 1

sub_set = file_path[0:6]
print(sub_set) # c:user

sub_set = file_path[:8]
print(sub_set) # c:user\p

sub_set = file_path[3:]
print(sub_set) # ser\programming\python\lab01

sub_set = file_path[3:15:2]
print(sub_set) # srporm

greeting = 'Hello World'
sub_set = greeting[0:6]

print(sub_set) # Hello

reverse_string = file_path[::-1]
print(reverse_string)

# 10bal\nohtyp\gnimmargorp\resu:c

sub_set = greeting.find('l', 4)
print(sub_set) # 9

print(greeting.upper()) # HELLO WORLD

print(greeting.lower()) # hello world

print(greeting.title()) # Hello World

print(greeting.startswith('H'))
print(greeting.startswith('h'))
print(greeting.endswith('d'))
print(greeting.endswith('w'))

# True
# False
# True
# False

print('hel' in greeting) # False case sensitive
print('Hel' in greeting) # True
print('z' in greeting) # False

print('*'.join(greeting)) # H*e*l*l*o* *W*o*r*l*d

count = 0
for letter in greeting:
    if letter == 'l':
        count +=1
print(f'{count} letter(s) were found')

# 3 letter(s) were found

