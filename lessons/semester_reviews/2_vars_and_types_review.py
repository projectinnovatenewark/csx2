# # # Title: Setting variables and constants

# # A variable is a reserved memory location used to store a given value. All data types can be stored
# # as variables. When defining a variable, the name is on the left side of the "=" and the data
# # being stored is on the right. Below is are a couple examples of this:

# # TIP: variable_name = value
# num1 = 4
# print("num1 is equal to:", num1)

# # Variables can be redefined at any point throughout the file.
# num1 = 5
# print("num1 is now equal to:", num1) 

# song = "We Will Rock You"
# # HINT: Below we are using f shorthand for our print statement.
# print(f"song: {song}")

# # Constants are similar to variables, but are meant to never be changed. A good example of a
# # constant is the numerical value of Pi: 3.14. An indicator of a constant is that it's name is
# # in all caps.

# PI = 3.14
# print(f"PI is equal to: {PI}")

# ####################################################################################################

# # Title: Variable Types

# # You can check a variable's type by using "type(variable)". We will do this throughout the section.

# # A string is a sequence of characters used to represent text. As you can see in the following
# # example, stings are expressed by wrapping a set of characters in single or double quotes.

# stringy = "this is a string"
# print(f"stringy: {stringy} | type: {type(stringy)}")

# # A boolean is a data type used to indicate "True" or "False". 

# true_val = 4 > 2
# print(f"true_val: {true_val}")
# print(f"type: {type(true_val)}")

# false_val = "red" == "blue"
# print(f"ftype: {type(false_val)}")
# print(f"false_val: {false_val}")

# # A "Nonetype" is a variable that has no value.

# none_val = None
# print(f"none_val: {none_val}")
# print(f"type: {type(none_val)}")

# # An integer is any positive or negative whole number.

# integer1 = 45
# negative_integer = -10
# print(f"integer1: {integer1} & negative_integer: {negative_integer}")
# print(f"type of integer1: {type(integer1)} & negative_integer: {type(negative_integer)}")

# # A float is a postive or negative number that carries a decimal point.
# pos_float = 3.5
# neg_float = -45.0 # Even with a ".0" neg_float is still a float
# print(f"pos_float: {pos_float} & neg_float: {neg_float}")
# print(f"type of pos_float: {type(pos_float)} & neg_float: {type(neg_float)}")

# ####################################################################################################

#Title Type Conversion

# Lastly, you can use type conversion to change the data type of a given variable. For example, an
# integer can be converted into a float.

number = 10
print(f"{number} is an {type(number)}")
number_as_float = float(number)
print(f"number_as_float is a {type(number_as_float)} and has a value of {number_as_float}.")

# Type conversions for each type are the following:
int() # is used for converting to integers
float() # is used for converting to floats
str() # is used for converting to strings
bool() # is used for converting to booleans

