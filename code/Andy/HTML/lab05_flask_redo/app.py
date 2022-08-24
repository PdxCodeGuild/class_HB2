from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

# print('type of object: ', type(app))
# type of object:  <class 'flask.app.Flask'>

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/recieve_form/', methods=['GET','POST'])
def converter():
