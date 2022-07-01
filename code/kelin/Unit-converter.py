# kelin-lab02-unit-converter

# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m.

from operator import truediv


feet_to_meters = {'ft': 0.3048}

number_feet = input("\nPlease enter the number of feet: ")

number_feet = int(number_feet)

meters = (feet_to_meters['ft'] * number_feet)

print((number_feet), "feet is", (meters), "meters")

# Version 2

# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m

meter = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}

while True:
    number = input("Enter the distance: ")
    unit = input("Enter the unit - ft - mi - m - km - yd - in: ")
    if unit == 'ft':
        print((number), "feet is", (int(number) * (meter["ft"])), "meters")
    elif unit == 'mi':
        print((number), "miles is", (int(number) * (meter["mi"])), "meters")
    elif unit == 'm':
        print((number), "meters is", (int(number) * (meter["m"])), "meters")
    elif unit == 'km':
        print((number), "kilometers is", (int(number) * (meter["km"])), "meters")
    elif unit == 'yd':
        print((number), "yards", (int(number) * (meter["yd"])), "meters")
    elif unit == 'in':
        print((number), "inches is", (int(number) * (meter["in"])), "meters")
    else:
        print("Invalid unit")

# Verson 3

# Added support for yards, and inches.

# 1 yard is 0.9144 m
# 1 inch is 0.0254 m



