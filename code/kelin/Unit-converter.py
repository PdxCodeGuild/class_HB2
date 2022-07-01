# kelin-lab02-unit-converter

# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m.

feet_to_meters = {'ft': 0.3048}

number_feet = input("\nPlease enter the number of feet: ")

number_feet = int(number_feet)

meters = (feet_to_meters['ft'] * number_feet)

print(meters)

# Version 2

# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m
# Below is some sample input/output:

# > what is the distance? 100
# > what are the units? mi
# > 100 mi is 160934 m

meter = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000
}

number = input("Enter the distance: ")
unit = input("Enter the unit - ft - mi - m - km: ")








