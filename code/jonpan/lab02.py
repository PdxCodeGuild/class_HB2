## VERSION 1 BELOW
#distance = input("what is the distance in feet: ")  
#meters = {
#    'ft': 0.3048
#}
#a = int(distance)
#result = 1
#for i in meters:
#    result = a*meters[i]
#print(f"\n{distance} ft is {result} m")

## VERSION 2 AND 3 COMBINED BELOW

# distance = input("\nWhat is the distance? ") 
# units = input("\nWhat are the units? Your choices are feet, miles, meters, km, yard, or inch. ")
# conversion = {
#    'feet': 0.3048,
#    'miles': 1609.34,
#    'meters': 1,
#    'km': 1000,
#    'yard': 0.9144,
#    'inch': 0.0254,
# }

# selectedunit = conversion[units]
# result = selectedunit * int(distance)

## VERSION 4 BELOW

distance = input("\nWhat is the distance? ") 
input_units = input("\nWhat are the input units? Your choices are feet, miles, meters, km, yard, or inch. ")
output_units = input("\nWhat are the output units? Your choices are feet, miles, meters, km, yard, or inch. ")

conversion = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254,
}

inputresults = conversion[input_units]
result = (inputresults * int(distance)) / conversion[output_units]

print(f"\n{distance} {input_units} is {result} {output_units}")