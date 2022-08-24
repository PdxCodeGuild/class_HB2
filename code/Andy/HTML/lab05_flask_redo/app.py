from flask import Flask, render_template, request

app = Flask(__name__)

# print('type of object: ', type(app))
# type of object:  <class 'flask.app.Flask'>

@app.route('/')
def index():
    conversion ={
        'ft':0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
        'yd': 0.9144,
        'in': 0.0250

    }
    result = 'ARMY SUCKS!'
    return render_template('index.html', html_value=result)

app.run(debug=True)