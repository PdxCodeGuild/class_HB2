#Matt Nichols
#HB2 Lab02

#Version 1

#Variable for ft to meters
ft = 0.3048

#While loop to allow the user to continue to put in different calculations
while True:
    user_input = input("Enter a number in feet to convert to meters\nType 'done' to exit\n")
    if user_input == "done":
        print("Okay, thanks for your time ")
        break
 #Try and except for converter.
    try:
        converter = float(user_input)
        calc = converter * ft
        print(f'{user_input} in feet = {calc} in meters')
    except:
        print("Sorry, that input was invalid. Please enter numerals 0-9\nMake sure there are no spaces in between your numerals ")

#Version 2

#Dictionary with measurements for future converting
unit_converter = {
'ft': 0.3048,
'mi': 1609.34,
'm': 1,
'km': 1000
}

#While loop for the user to continue putting in different calculations
while True:

#User input for either exiting the program or pulling something from the dictionary
    unit_input = input("Enter your unit of measurement in 'ft', 'mi', 'm', or 'km' to convert to meters:\nType 'done' to exit\n")
    
    #Exit 
    if unit_input == 'done':
        result = "Okay, thank you for your time"
        print(result)
        break

    #unit converter/calculator/easy out if user input is invalid with try and except
    try: 
        converter = unit_converter[unit_input]
        numbers = float(input("Now enter the length of measurement:\n"))
        calculator = numbers * converter
        print(f'{numbers} {unit_input} = {calculator} in meters' )
    except:
        print("Oops, something went wrong. Make sure that you type the options that are presented\nFirst section - Type 'ft', 'mi', 'm', 'km', or 'done'.\nSecond section - Type numerals 0-9 and ensure there are no spaces between your numerals")

#Version 3

#Dictionary with measurements for future converting
unit_converter = {
'ft': 0.3048,
'mi': 1609.34,
'm': 1,
'km': 1000,
'yard': 0.9144,
'inch': 0.0254
}

#While loop for the user to continue putting in different calculations
while True:

#User input for either exiting the program or pulling something from the dictionary
    unit_input = input("Enter your unit of measurement in 'ft', 'mi', 'm', 'km', 'yard', or 'inch' to convert to meters:\nType 'done' to exit\n")
    
    #Exit 
    if unit_input == 'done':
        result = "Okay, thank you for your time"
        print(result)
        break

    #unit converter/calculator/easy out if user input is invalid with try and except
    try: 
        converter = unit_converter[unit_input]
        numbers = float(input("Now enter the length of measurement:\n"))
        calculator = numbers * converter
        print(f'{numbers} {unit_input} = {calculator} in meters' )
    except:
        print("Oops, something went wrong. Make sure that you type the options that are presented\nFirst section - Type 'ft', 'mi', 'm', 'km', or 'done'.\nSecond section - Type numerals 0-9 and ensure there are no spaces between your numerals")

