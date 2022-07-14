# Lab 02: Unit Converter
# This lab will involve writing a program that allows the user to convert a number between units.


# ===========
# Version 1
# ===========
# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
# > what is the distance in feet? 12
# > 12 ft is 3.6576 m
# ===============================================================


numberOfFeet = input("Enter the number of feet: ")
feetToMeters = float(numberOfFeet) * 0.3048
print(f"{numberOfFeet} feet is {feetToMeters} meters.")





# ===========
# Version 2
# ===========
# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.=
# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m
# Below is some sample input/output:
# > what is the distance? 100
# > what are the units? mi
# > 100 mi is 160934 m
# from math import dist
# from turtle import distance
# ===============================================================


enterUnitType = input("Choose a unit measurement (ft, mi, m, or km): ")
enterDistance = input("Choose a distance: ")
ftToMeters = float(enterDistance) * 0.3048
miToMeters = float(enterDistance) * 1609.34
mToMeters = float(enterDistance) 
kmToMeters = float(enterDistance) * 1000.00


if enterUnitType == "ft":
    print(f"{enterDistance} ft is {ftToMeters} meters.")
elif enterUnitType == "mi":
    print(f"{enterDistance} miles is {miToMeters} meters.")
elif enterUnitType == "m":
    print(f"{enterDistance} meters is {mToMeters} meters.")
elif enterUnitType == "km":
    print(f"{enterDistance} kilometers is {kmToMeters} meters.")
else:
    print("Not a valid option")






# ===========
# Version 3
# ===========
# Add support for yards, and inches.
# 1 yard is 0.9144 m
# 1 inch is 0.0254 m
# ===============================================================

enterUnitType = input("Choose a unit measurement (yd or in): ")
enterDistance = input("Choose a distance: ")
ftToMeters = float(enterDistance) * 0.9144
miToMeters = float(enterDistance) * 0.0254

if enterUnitType == "yd":
    print(f"{enterDistance} yards is {ftToMeters} meters.")
elif enterUnitType == "in":
    print(f"{enterDistance} inches is {miToMeters} meters.")


# ====================
# Version 4 - optional
# ====================
# to be continued...