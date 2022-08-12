enterUnitType = input("Choose a unit measurement (ft, mi, m, km, yd, or in): ")
enterDistance = input("Choose a distance: ")
ftToMeters = float(enterDistance) * 0.3048
miToMeters = float(enterDistance) * 1609.34
mToMeters = float(enterDistance) 
kmToMeters = float(enterDistance) * 1000.00
ftToMeters = float(enterDistance) * 0.9144
miToMeters = float(enterDistance) * 0.0254


if enterUnitType == "ft":
    print(f"{enterDistance} ft is {ftToMeters} meters.")
elif enterUnitType == "mi":
    print(f"{enterDistance} miles is {miToMeters} meters.")
elif enterUnitType == "m":
    print(f"{enterDistance} meters is {mToMeters} meters.")
elif enterUnitType == "km":
    print(f"{enterDistance} kilometers is {kmToMeters} meters.")
elif enterUnitType == "yd":
    print(f"{enterDistance} yards is {ftToMeters} meters.")
elif enterUnitType == "in":
    print(f"{enterDistance} inches is {miToMeters} meters.")
else:
    print("Not a valid option")






