
# ====
# app.py
# ====

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




# ===============
@app.route('/convert')
def convert():
    enter_unit_type = request.args['unit_type']
    enter_distance = int(request.args['distance'])
    converted = 0
    
    ft_to_meters = float(enter_distance) * 0.3048
    mi_to_meters = float(enter_distance) * 1609.34
    m_to_meters = float(enter_distance)
    km_to_meters = float(enter_distance) * 1000.00
    yd_to_meters = float(enter_distance) * 0.9144
    in_to_meters = float(enter_distance) * 0.0254

    if enter_unit_type == "ft":
        converted = str(enter_distance * ft_to_meters)
        return converted
    elif enter_unit_type == "mi":
        converted = str(enter_distance * mi_to_meters)
        return converted
    elif enter_unit_type == "m":
        converted = str(enter_distance * m_to_meters)
        return converted
    elif enter_unit_type == "km":
        converted = str(enter_distance * km_to_meters)
        return converted
    elif enter_unit_type == "yd":
        converted = str(enter_distance * yd_to_meters)
        return converted
    elif enter_unit_type == "in":
        converted = str(enter_distance * in_to_meters)
        return converted
    else:
        return ("Not a valid option")

    return render_template('sum.html', code=converted)
    
app.run(debug=True)









