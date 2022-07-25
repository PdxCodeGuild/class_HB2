letters = ['r', 'z', 'a']
zeros = [0] *10
letters_i = ['i'] *5
print(letters, zeros, letters_i)

# ['r', 'z', 'a'] [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ['i', 'i', 'i', 'i', 'i']

concat_lists = letters + zeros + letters_i

print(concat_lists)

# ['r', 'z', 'a', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'i', 'i', 'i', 'i', 'i']

numbers = list(range(21))
print(numbers)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

chars = list("July 2022")
print(chars)

# ['J', 'u', 'l', 'y', ' ', '2', '0', '2', '2']

print(len(chars)) # 9 characters in July 2022

letters = ['r', 'z', 'a', 'o', 'd', 'b']
print(letters)
print(letters[0]) # returns 1st element/position r
letters[0] = 'R'
print(letters) # ['R', 'z', 'a', 'o', 'd', 'b']

print(letters[0:3]) # ['R', 'z', 'a']

print (letters[:3]) # returns same first 3 letters

letters[-1] = 'DD'

print(letters) # ['R', 'z', 'a', 'o', 'd', 'DD']

print(letters[::2]) # ['R', 'a', 'd']

nums = list(range(21))
print(nums[::2]) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] prints every other number to 21

print(nums[::-1]) # starts at end and counts back 

# [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 

# Unpacking lists

nums = [4, 8, 12]
first_num = nums[0]
second_num = nums[1]
thrid_num = nums[2]

first_num, second_num, third_num = nums
print(first_num, second_num, third_num) # 4 8 12

nums = [4, 8, 12, 89, 3901, -1, 78, 100]
first_num, second_num, *msc = nums
print(first_num)
print(second_num)
print(msc)

# 4 first_num
# 8 second_num
# [12, 89, 3901, -1, 78, 100] (msc) puts in seperate list

'''loop'''
letters = ['k', 'p', 'c', 'q']
for l in letters:
    print(l)

# k
# p
# c
# q

for l in enumerate(letters):
    print(l)

# (0, 'k')
# (1, 'p')
# (2, 'c')
# (3, 'q')

for l in enumerate(letters):
    print(l[0], l[1]) # prints them outside the tuple

# 0 k
# 1 p
# 2 c
# 3 q

for i, l in enumerate(letters):
    print(i, l)

# 0 k
# 1 p
# 2 c
# 3 q

letter_25 = [25, 'y']
index, letter = letter_25
print(index, letter)

#  25 y

# unpack a tuple

letter_25 = (25, 'z')
index, letter = letter_25
print(index, letter)

# 25 z same

letters = ['a', 'b', 'c']
letters.append('z') # adds z at the end
letters.insert(0, '>') # adds > at first position
print(letters)

# ['>', 'a', 'b', 'c', 'z']

letters.insert(2, '<')
print(letters)

# ['>', 'a', '<', 'b', 'c', 'z']

letters.pop()
print(letters) # ['>', 'a', '<', 'b', 'c'] z removed

# letters.pop([0]) # does not need [] notation
print(letters)

letters.pop(0)
print(letters) # ['a', '<', 'b', 'c'] > sign removed

letters.remove('c')
print(letters) # ['a', '<', 'b'] first occurance of c removed

dup_letters = ['a', 'b', 'c', 'c', 'd', 'z', 'f', 'f']
non_dup_letters = []
print(dup_letters, 'b4 loop')

for item in dup_letters:
    if item not in non_dup_letters:
        non_dup_letters.append(item)
print(non_dup_letters, 'after loop')

# ['a', 'b', 'c', 'c', 'd', 'z', 'f', 'f'] b4 loop
# ['a', 'b', 'c', 'd', 'z', 'f'] after loop

del dup_letters[1]
print(dup_letters)

# ['a', 'c', 'c', 'd', 'z', 'f', 'f'] b removed

del dup_letters[0:5]
print(dup_letters) # ['f', 'f'] removed first 5 items

dup_letters.clear()
print(dup_letters, 'clear the list') # [] clear the list

names = ['Logan', 'Jean', 'Peter']
print(names.index('Jean')) # 1

# print(names.index('Bruce')) # value error not in the list

if 'Bruce' in names:
    print(names.index('Bruce')) # Doesn't print a value

if 'Logan' in names:
    print(names.index('Logan')) # 0

dup_letters = ['a', 'b', 'c', 'c', 'd', 'z', 'f', 'f']
print(dup_letters.count('f')) # 2 f's
if 'f' in dup_letters:
    print(dup_letters.index('f'))

nums = [7, 4, 8, 0, -1, 333]
nums.sort() # ascending default
print(nums) # [-1, 0, 4, 7, 8, 333]

nums.sort(reverse=True)
print(nums) # [333, 8, 7, 4, 0, -1]

# sort modiefies the original list
# sorted does not modify the original list, returns a new list

print(sorted(nums), 'sorted method')
print(nums, 'original list')

# [-1, 0, 4, 7, 8, 333] sorted method
# [333, 8, 7, 4, 0, -1] original list

print(sorted(nums), 'sorted method')

dict_a = {'city': 'portland', 'state': 'or'}
print(dict_a) # {'city': 'portland', 'state': 'or'}

# city = dict_1[0] # will return error

city = dict_a['city']
print(city) # portland

state = dict_a['state']
print(state) # or

dict_a['state'] = 'ct'

print(dict_a) # state updated to ct {'city': 'portland', 'state': 'ct'}

dict_a['zip'] = 90210

print(dict_a)  # {'city': 'portland', 'state': 'ct', 'zip': 90210}

# print(dict_a['address']) KeyError

if 'address' in dict_a:
    print(dict_a['address']) # Does not return anything

print(dict_a.get('address')) # None return

print(dict_a.get('state')) # ct return

print(dict_a.get('address', 'Hey value not found')) # Hey value not found return