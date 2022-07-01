def version1():
    
    return answer

def version2():
    
    return answer

def version3():
    
    return answer

def unit_conversion():
    # Establish dictionary with values to convert meters to other measurements
    conv = {
        'ft': 0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
        'yd': 0.9144,
        'in': 0.0254
    }
    
    input_distance = float(input('What is the distance? '))
    input_measurement = str(input('What is the unit of measurement (ft, mi, m, km, yd, in)? '))
    
    answer = f'{input_distance} {input_measurement} is {input_distance * conv[input_measurement]} m'
    
    return answer

def main():
    
    return 0