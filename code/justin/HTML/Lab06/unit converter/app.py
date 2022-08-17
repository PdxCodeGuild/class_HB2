from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/conversion')
def conversion():
    measurements = {'Feet' : 0.3048, 'Miles': 1609.34, 'Meters': 1, 'Kilometers': 1000}
    num1 = int(request.args['number1'])
    # num2 = int(request.args['number2'])
    units1 = request.args['units1']
    units2 = request.args['units2']
    meter = num1 * measurements[units1]
    conv = round(meter / measurements[units2], 4)
    algo = conv
    return render_template('conversion.html', starting=num1, measure=units1, code=algo, distance=units2)


app.run(debug=True)