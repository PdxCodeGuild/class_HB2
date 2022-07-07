


#         VERSION 1           #


from inspect import formatannotation


conversion_list = {
    'foot': 0.3048,
    'mile': 1609.34,
    'meter': 1,
    'kilometers': 1000
    
}

# 

# while True:
    
#     principle_unit = input("\nWhat is the distance in feet?: ")
#     total = (conversion_list['foot']) * int(principle_unit)
    
#     print(f"{principle_unit} feet is in {total} m")
    
#     break


#         VERSION 2            #

# conversion_list = {
#     'foot': 0.3048,
#     'feet': 0.3048,
#     'mile': 1609.34,
#     'miles': 1609.34,
#     'meter': 1,
#     'meters': 1,
#     'kilometer': 1000,
#     'kilometers': 1000,
#     'yard': 0.9144,
#     'yards': 0.9144,
#     'inch': 0.0254,
#     'inches': 0.0254
#     }

# user = True
# while user:
    
#     users_unit_input = input("\nWhat is the unit to convert to meters?: ")
    
#     users_unit_input == conversion_list[users_unit_input]
    
#     print(users_unit_input)
#     # print(users_distance_input)
#     users_distance_input = int(input("\nWhat is the distance to convert to meters?: "))
    
#     distance = users_distance_input * conversion_list[users_unit_input]
#     # print(distance)
#     print(f"{users_distance_input} {users_unit_input} is {((users_distance_input) * conversion_list[users_unit_input])} meters")
    
#     user = False
    
#            VERSION 3               #

# conversion_list = {
#     'foot': 0.3048,
#     'feet': 0.3048,
#     'mile': 1609.34,
#     'miles': 1609.34,
#     'meter': 1,
#     'meters': 1,
#     'kilometer': 1000,
#     'kilometers': 1000,
#     'yard': 0.9144,
#     'yards': 0.9144,
#     'inch': 0.0254,
#     'inches': 0.0254
#     }
# user = True
# while user:
    
#     users_unit_input = input("\nWhat is the unit to convert to meters?: ")
    
#     users_unit_input == conversion_list[users_unit_input]
    
#     print(users_unit_input)
#     # print(users_distance_input)
#     users_distance_input = int(input("\nWhat is the distance to convert to meters?: "))
    
#     distance = users_distance_input * conversion_list[users_unit_input]
#     # print(distance)
#     print(f"{users_distance_input} {users_unit_input} is {((users_distance_input) * conversion_list[users_unit_input])} meters")
    
#     user = False
    
    #        VERSION 4         #
    
    
conversion_list = {
    'foot': 0.3048,
    'feet': 0.3048,
    'mile': 1609.34,
    'miles': 1609.34,
    'meter': 1,
    'meters': 1,
    'kilometer': 1000,
    'kilometers': 1000,
    'yard': 0.9144,
    'yards': 0.9144,
    'inch': 0.0254,
    'inches': 0.0254
    }

user = True
while user: 
    users_distance_input = int(input("\nWhat is the distance to convert?: "))
    
    users_unit_input = input("\nWhat is the unit to convert from?: ")
    
    users_unit_input == conversion_list[users_unit_input]
    
    users_unit_output = input("\nWhat is the unit to convert to?: ")
    
    users_unit_output == conversion_list[users_unit_output]
    
    result = users_distance_input * conversion_list[users_unit_input]
    
    result = result / conversion_list[users_unit_output]
    
    print(f"{users_distance_input} {users_unit_input} is {result}")
        
    user = False
    