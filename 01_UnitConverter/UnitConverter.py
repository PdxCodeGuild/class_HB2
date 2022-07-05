# Lab 02: Unit Converter
# This lab will involve writing a program that allows the user to convert a number between units.


# ===========
# Version 1
# ===========
# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

# > what is the distance in feet? 12
# > 12 ft is 3.6576 m


# numberOfFeet = input("Enter the number of feet: ")
# feetToMeters = float(numberOfFeet) * 0.3048
# print(f"{numberOfFeet} feet is {feetToMeters} meters.")





# ===========
# Version 2
# ===========
# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

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


enterUnitType = input("Choose a unit measurement (ft, mi, m, or km): ")
enterDistance = input("Choose a distance: ")
ftToMeters = float(enterDistance) * 0.3048
miToMeters = float(enterDistance) * 1609.34
mToMeters = float(enterDistance) 
kmToMeters = float(enterDistance) * 1000.00
# distanceTypes = {
#     "ft": 0.3048,
#     "mi": 1609.34,
#     "m":1,
#     "km": 1000
# }    

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


# ====================
# Version 4 - optional
# ====================
# Now we'll ask the user for the distance, the starting units, and the units to convert to.

# You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

# ft	mi	m	km
# ft	1		0.3048	
# mi		1	1609.34	
# m	1/0.3048	1/1609.34	1	1/1000
# km			1000	1
# But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.

# Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

# Below is some sample input/output:

# > what is the distance? 100
# > what are the input units? ft
# > what are the output units? mi
# 100 ft is 0.0189394 mi
# Turning in your lab
# Make sure you are still on your lab branch with git status. This will also show you a list of files that have been modified.
# Add any files you want git to keep track of using git add filename. Replace filename with the name of your file. You can also use git add . to add everything within the current folder.
# Commit your work using git commit -m "Your commit message". Make sure your commit message is descriptive and describes what has been changed during this commit.
# Finally we can run the command git push to send our files up to Github. This may throw an error, but worry not, there will be a suggested command to run, simply copy and paste that command and you should be good to go.
# Don't forget to visit Github and create a pull request to submit your work for review.
# Footer
# © 2022 GitHub, Inc.
# Footer navigation

#     Terms
#     Privacy
#     Security
#     Status
#     Docs
#     Contact GitHub
#     Pricing
#     API
#     Training
#     Blog
#     About

