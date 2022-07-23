conv_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
    }

def version1(conv = conv_dict):
    feet = float(input("what is the distance in feet? "))
    answer = f"{feet} ft is {feet * conv['ft']} m"

    return answer

def version2(conv = conv_dict):
    input_distance = float(input('What is the distance? '))
    input_measurement = str(input('What is the unit of measurement (ft, mi, m, km)? '))
    
    answer = f'{input_distance} {input_measurement} is {input_distance * conv[input_measurement]} m'
    
    return answer

def version3(conv = conv_dict):
    input_distance = float(input('What is the distance? '))
    input_measurement = str(input('What is the unit of measurement (ft, mi, m, km, yd, in)? '))
    
    answer = f'{input_distance} {input_measurement} is {input_distance * conv[input_measurement]} m'
    
    return answer

def main():
    print(version1())
    print(version2())
    print(version3())

main()