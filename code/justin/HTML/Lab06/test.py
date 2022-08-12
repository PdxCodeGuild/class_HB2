import random
from string import ascii_lowercase, ascii_uppercase, punctuation
inputa = input('how many upper?')


password=[]
pwstring = ''
upper = int(inputa)
for x in range(upper):
    password.append(random.choice(ascii_uppercase))
    # code = request.args['upper']
for x in range(upper):
    password.append(random.choice(ascii_lowercase))
for x in range(upper):
    password.append(random.randint(0,9))
for x in range(upper):
    password.append(random.choice(punctuation))
for x in password:
    pwstring += str(x)

print(password)
print(pwstring)