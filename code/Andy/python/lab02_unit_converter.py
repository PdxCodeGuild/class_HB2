#version 1
units = {
    "feet": 0.3048,
    "meters": 1
}
distance = input("Enter Lenth of feet:")
distance= int(distance)
total = distance * units["feet"]
print(f"{distance} FT is {total} Meters")

#version 2
units_mesurments = {
    "feet": 0.3048,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000
    }

distance = input("what is the distance?")
units = input("what are the units?:")
calling = units_mesurments[units]
distance = int(distance)
total = distance * calling

print(f"{distance} {units} is {total} Meters")

#version 3
units_mesurments = {
    "feet": 0.3048,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000,
    "yards": 0.9144,
    "inches": 0.0254
    }

distance = input("what is the distance?")
units = input("what are the units?:")
calling = units_mesurments[units]
distance = int(distance)
total = distance * calling

print(f"{distance} {units} is {total} Meters")