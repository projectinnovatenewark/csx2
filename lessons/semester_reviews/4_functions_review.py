# Title: Functions and Scope

# A function is a block of code that only runs when its called. Funtions are defined using the
# format: "def function_name(parameter_name):" Functions are then called in the format:
# "function_name(argument)" where arguments that are passed get renamed as the parameter in the
# function call. Below is an example of defining a function:

def printer(): # Functions don't always need parameters.
   # Everything within the indent of the function is considered in the function's scope.
  print("Function completed") # This is in the scope of the function

# Now that our code is back to the left-most part of the window, we are out of the scope of
# "printer()".
printer()

# Functions can also be called within other functions. In the below function, a number will be
# passed as an argument to a function called "add_seven()" and then our printer() function will be
# called to let us know the function is complete.

def add_seven(num1): # num1 is a parameter that will take the value of an argument passed.
  new_number = num1 + 7 
  printer()
  return new_number # This is a return statement. Return statements make it possible for
                    # functions to store a value on execution to be used later.


num = add_seven(30) # Functions can be stored in variables too! Now it's value can be used in a
# print statement.
print(num)

# IMPORTANT: Functions vs Methods
# It's important to remember the key difference between functions and methods. Methods are always
# defined within the scope of a class object while functions are defined elsewhere.

# TODO: Teacher: Head back over to fam_cam.py and recap how to call functions from other files.