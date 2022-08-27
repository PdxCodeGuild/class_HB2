from flask import Flask, render_template, request
app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_form/', methods=['GET','POST'])
def unitconverter():
    if request.method == 'POST':
        distance = request.form['input_distance']
        input_units = request.form['input_units']
        output_units = request.form['output_units']

        conversion = {
        'feet': 0.3048,
        'miles': 1609.34,
        'meters': 1,
        'km': 1000,
        'yard': 0.9144,
        'inch': 0.0254,
        }

        inputresults = conversion[input_units]
        result = (inputresults * int(distance)) / conversion[output_units]
    return (f"\n{distance} {input_units} is {result} {output_units}")

app.run(debug=True)
