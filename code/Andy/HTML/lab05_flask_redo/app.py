from flask import Flask, render_template, request
from requests import post

app = Flask(__name__, template_folder='templates')
# app = Flask(__name__)

# print('type of object: ', type(app))
# type of object:  <class 'flask.app.Flask'>

@app.route('/')
def index():
    # return "hey we're here"
    return render_template('index.html')

@app.route('/recieve_form/', methods=['GET','POST'])
def converter():
    # print('request.POST', request.form.keys())
    # request.POST dict_keys(['distance', 'in_units'])
    
    if request.method == 'POST':
        distance = request.form['distance']
        in_units = request.form['in_units']
        # print('distance type', type(distance))
        # print('in_units type', type(in_units))


        
        measurments = {
            'ft': 0.3048,
            'mi': 1609.34,
            'm': 1,
            'km': 1000,
            'yd': 0.9144,
            'in': 0.0254,

        }

        in_results = measurments[in_units]
        results = in_results * float(distance)
        return(f"{distance} {in_units} is {results} Meters")

app.run(debug=True)