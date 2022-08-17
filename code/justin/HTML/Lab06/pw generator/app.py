from string import ascii_lowercase, ascii_uppercase, punctuation
from flask import Flask, render_template, request
import random


app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/generator')
def password():
    password=[]
    pwstring = ''
    upper = int(request.args['upper'])
    lower = int(request.args['lower'])
    numbers = int(request.args['numbers'])
    special = int(request.args['special'])
    for x in range(upper):
        password.append(random.choice(ascii_uppercase))
    for x in range(lower):
        password.append(random.choice(ascii_lowercase))
    for x in range(numbers):
        password.append(random.randint(0,9))
    for x in range(special):
        password.append(random.choice(punctuation))
    for x in password:
        pwstring += str(x)
    pwstring = ''.join(random.sample(pwstring,len(pwstring)))   
    code = pwstring 
    return render_template('generator.html', code=code)


app.run(debug=True)