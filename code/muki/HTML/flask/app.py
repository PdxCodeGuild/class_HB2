# app.py for flask lab

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_form/', methods=['POST'])
def temperature():
    print(request.form) # {'person_name': 'Jane', 'person_age': 34}
    person_name = request.form['person_name'] # Jane
    person_age = request.form['person_age'] # 34
    return redirect('/')




meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'mm': 0.001,
    'yd': 0.9144,
    'in': 0.0254,
}

convert_amount = input('####')
convert_unit = input('ft, mi, km, mm, yd, in\t')

def prod(amount, unit):
    product = round(float(amount) * meters[unit], 2)
    return product
product = prod(convert_amount, convert_unit)
print(f'{product} meters')