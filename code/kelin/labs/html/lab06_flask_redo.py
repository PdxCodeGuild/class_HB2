# Kelin Ray

# # Lab 06: Flask Redo

# Implement one of the following Python labs in a Flask app:

# - [Unit Converter](https://github.com/PdxCodeGuild/class_kiwi/blob/main/1%20Python/labs/01%20Unit%20Converter.md)

#   - Simple version: the user enters the distance and units and the app shows them the converted distance in meters

from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter')
def unitconverter():
    feet_to_meters = {'ft': 0.3048}
    number_feet = int(request.args['feetmeters'])
    algo = (feet_to_meters['ft'] * number_feet)
    
    return render_template('converter.html', code=algo)

# Version 2

# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

@app.route('/converter2')
def unitconverter2():
    distance = int(request.args['distance'])
    meter = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000
    }
    unit = (request.args['units'])
    if unit == 'ft':
        algo = (meter['ft'] * distance)
    elif unit == 'mi':
        algo = (meter['mi'] * distance)
    elif unit == 'm':
        algo = (meter['m'] * distance)
    elif unit == 'km':
        algo = (meter['km'] * distance)
    
    return render_template('converter2.html', code=algo)

#   - Complex version: the user also enters output units


app.run(debug=True)