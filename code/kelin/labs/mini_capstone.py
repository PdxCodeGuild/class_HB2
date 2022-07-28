import emoji

# https://pypi.org/project/emoji/ emoji 2.0.0
# pip install emoji
# emoji list https://carpedm20.github.io/emoji/

# Using emoji package to help describe my understanding of Python lessons:
# Fundamentals
# Exceptions + Testing
# Numbers + Arithmetic
# Booleans + Comparisons + Conditionals
# Imports + Modules + Packages
# Random
# While + For Loops
# Strings
# Lists + Tuples
# Functions
# Dictionaries
# Regular Expressions in Python
# Datetimes
# Classes
# Requests
# Docstrings
# File IO
# Sets
# Virtual Environments

print(emoji.emojize(f'Learning Python is :downcast_face_with_sweat: sometimes, and it can even make my head :exploding_head: !!!'))

# emojize takes the code and displays the emoji


lessons = []
while True:

    fundamentals = input(emoji.demojize(f'Fundamentals enter an emoji code: \n✅\nor\n❌ '))
    exceptions = input(emoji.demojize(f'Exceptions + Testing enter an emoji code: \n✅\nor\n❌ '))
    
    # demojize takes the emoji and displays the code for it

    lessons.append ({
        'Fundamentals': fundamentals
        })
    
    print(emoji.emojize(str(lessons)))

    # if fundamentals == (':check_mark_button:'):
    #     lessons.append ({
    #     'Fundamentals': fundamentals
    #     })
    # else if fundamentals == (':cross_mark:')
    #      lessons.append ({
    #     'Fundamentals': fundamentals
    #     })

    # exceptions = input(emoji.demojize(f'Exceptions + Testing enter ✅ if reviewed: '))
    # if exceptions == (':check_mark_button:'):
    #     lessons.append ({
    #     'Exceptions + Testing': exceptions
    #     })
    # else:
    #     print('Please review Exceptions + Testing')

    # print(emoji.emojize(str(lessons)))

    
    # Fundamentals\nExceptions + Testing\nNumbers + Arithmetic\nBooleans + Comparisons + Conditionals\nImports + Modules + Packages\nRandom\nWhile + For Loops\nStrings\nLists + Tuples\nFunctions\nDictionaries\nRegular Expressions in Python\nDatetimes\nClasses\nRequests\nDocstrings\nFile IO\nSets\nVirtual Environments\n\nEnter a lesson to see my description: ')
    
    # if lesson == 'Fundamentals':
    #     print(emoji.emojize(f'Fundamentals :school: is about different data types from strings :COOL_button: to integers :input_numbers: and also goes over dictionaries and lists.'))
    # elif lesson == 'Exceptions':
    #     print(emoji.emojize(f'Exceptions and Testing :test_tube: is about Python finding errors in your code and giving you a message :spiral_notepad:" including the line :pencil:" the error occured on.'))
    # elif lesson == 'Numbers':
    #     print(emoji.emojize(f'Numbers and Arithmetic :input_numbers: in Python is about different types of numbers from Integers to Floats and mathematical operations to get a result from those numbers'))
    
    # lessons.append ({
    #     'Fundamentals': fundamentals})



# variable = pippackage.getpipthing('parameters')

# print(variable)