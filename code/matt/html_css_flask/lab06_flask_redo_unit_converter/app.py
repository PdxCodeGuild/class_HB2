from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate/', methods=['GET','POST'])
def unit_converter():
    if request.method == 'POST':
        distance = request.form['distance']
        units_of_measurement = request.form['units_of_measurement']
        calculation = request.form['calculation']

    units_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
    }  
    
    converter = units_dict[units_of_measurement]
    calculator = converter * float(distance) / units_dict[calculation]
    return (f'{distance} {units_of_measurement} = {calculator} {calculation}')

app.run(debug=True)