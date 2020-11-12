"""
if, elif, else and iteratable operations
"""

# In Python, we can execute a certain block of code based on a condition. This is useful when you
# only want a program to run IF a condition is satisfied. The most basic form of a condtional
# statement is an "if" statement.

bool1 = True
bool2 = False

if (bool1 == True): # TODO: Teacher, change the if statement from "bool1" to "bool2".
    print("It's true! It's true!")

# In plain english, the example above states that IF bool1 is true, the print statement
# "It's true! It's true!" will be executed.

# Inroduce else

# Introduce elif

####################################################################################################

# TITLE: Using the three conditionals together

num = 3 # TODO: Teacher, try changing this number up to satisfy the different conditions.

if (num > 0):
    print(num, "is a positive number.")
if (num > 2): # any number of if statements will be evaluated upon running the code
    print(num, "is greater than 2.")
elif (num < 0): # the elif statement will only be triggered if none of the "if" statements are true.
    print(num, "is a negative number.")
else: # the else statement will only run if none of the conditions above it are true.
    print(num, "is a zero value.")
