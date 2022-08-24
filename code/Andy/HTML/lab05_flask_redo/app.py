from flask import Flask, render_template, request
from requests import post

app = Flask(__name__, template_folder='template')

# print('type of object: ', type(app))
# type of object:  <class 'flask.app.Flask'>

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/recieve_form/', methods=['GET','POST'])
def converter():
    if request.method == 'POST':
        distance = request.form['unit_distance']
        in_units = request.form['input_units']
        out_units = request.form['output_units']


        measurments = {
            'ft': 0.3048,
            'mi': 1609.34,
            'm': 1,
            'km': 1000,
            'yd': 0.9144,
            'in': 0.0254,

        }

        in_results = measurments[in_units]
        results = 

