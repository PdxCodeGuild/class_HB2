
#===========
# app.py
#===========
#Version1
#===========

from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')
      
@app.route('/ft_to_m')
def feet():
    ft = int(request.args['ft'])
    ft_to_meters = float(ft) * 0.3048
    print(f"{ft}")
    return render_template('sum.html', code=ft_to_meters)


#===========
#Version2
#===========


@app.route('/convert')
def convert():
    enter_unit_type = request.args['unit_type']
    enter_distance = int(request.args['distance'])
    converted = 0
    

    unit_dict = {
        "ft": 0.3048,
        "mi": 1609.34,
        "m": 1,
        "km": 1000.00,
        "yd": 0.9144,
        "in": 0.0254
    }

    converted = enter_distance * unit_dict[enter_unit_type]


    return render_template('sum.html', code=converted)
    
app.run(debug=True)









