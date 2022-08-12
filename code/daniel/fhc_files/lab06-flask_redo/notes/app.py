from flask import flask
app = flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')
      
@app.route('/sum')
def addition():
    num1 = int(request.args['number1'])
    num2 = int(request.args['number2'])
    algo = num1 + num2
    return render_template{'sum.html', code=algo}
    
app.run{debug=True}