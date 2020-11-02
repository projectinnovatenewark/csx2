"""
This is a docstring. They are used to detail files at a high level.
"""

# These lines that start with a pound sign are comments. They do nothing to the program
# except provide instructions, personal notes, or anything that you want really!

# TITLE: Section 1 - Intro to Variables & Types (6 minutes)

# Variables can be thought of as "pointers" to a value. These values have types.
# Types include things like integers, strings, floats, booleans, lists, and dictionaries.
# The name of the variable is on the left of the "=" sign and on the right is the content
# of the variable.

# A number without a decimal point is of the type integer.
number1 = 5

# A number with a decimal point is a float.
float1 = 6.3 # Floating point number
float2 = 7. # This is also a floating point number.

# Anything wrapped in quotation marks is a string.
string1 = "Hello" # String over here!
string2 = "my name is robot" # Literally, anything wrapped in quotes is a string.
string3 = "369" # Yes this is a string too.

# Naming variables is important! This has a capital "S" in string, so it's different
# than the previous variable of 'string1'.
String1 = "Wonderful!"

# You can even combine variables into one variable. We use the "print()" function to produce
# an output to your terminal.
big_string = string1 + string2
print(big_string)

# Let's make the output look a little cleaner. You can add in a string of an empty space
# directly between these variables. Also, variables can have their values changed!
# IMPORTANT: Variable's with changing values is an important concept! More on this topic on line 42.
big_string = string1 + " " + string2
print(big_string)

# Python reads from the top of the file to the bottom. Therefore, when "big_string" is first
# printed on line 40, it's value is "Hellomy name is robot", but since we changed the variable's
# value on line 48, it prints out that new value on line 39, which adds a space.

# You don't have to create a variable to print an output. You can put strings directly into print
# statements!!
print("Hello my name is robot")

# When you see, TODO: Section x of TODO y, you should stop where you are and head over to
# the corresponding assignment for this section of the lesson. The line below instructs
# you to visit section 1 of the 2nd TODO and complete it before moving on to the next section.
# TODO: Section 1 of TODO 2 (2 minutes for students, 1 minute demo)

####################################################################################################

# TITLE: Section 2 - Setting Multiple Variables in One Line and Additional Types (2 minutes)

# Setting multiple variables in one line of code? Yep. This is possible only when you use
# commas to separate each variable. The positions of the varibale names correspond with the values.
var1, var2, var3 = 1, 2, 3
print(var1, var2, var3)

# Booleans are true or false values. Python knows it is a boolean when you capitalize the first
# letter in your value just like below!
boolean = False
boolean2 = True

# if you want to set a variable to an empty value, use the None type.
variable_for_later = None
print("variable for later will equal", variable_for_later)

# TODO: Section 2 of TODO 2 (2 minutes for students, 1 minute demo)

####################################################################################################

# TITLE: Section 3 - "print()" Function Elaboration and Concatenation (5 minutes)

# Print is an example of a function. A function is a block of code that runs when
# it is called upon. The items you place in the parentheses are called arguments. Lets
# call the print function and pass arguments to print them.
string1 = "Hello"
num3 = 45

print("printing things, woohoo!!")
print(2387938457)
print(num3)
print(string1)

# FIXME: The code right here is broken, let's run it for fun to show that strings cannot be
# FIXME: concatenated directly with non-strings. Uncomment and run the code.
# print(string1 + "I am python number " + num3 + ", hear me roar!!") # TIP: Be sure to comment it out
                                                                    # TIP: before moving on.

# You can print any type by separating them with commas, as Python will automatically pass
# them into the print statement as separate "arguments", then convert them all into strings
# separated by one blank space. However, commas have one pitfall- they ALWAYS add in a space!
print(string1, "I am python number", num3, ", hear me roar!!")

# TAKEAWAY:
# Concatentation can only combine strings with other strings, and it does so using the plus
# sign. Concatentation does NOT place a space between your strings, but using a comma automatically
# places a space between your different values.

# TODO: Section 3 of TODO 2 (4 minutes for students, 2 minute demo)

####################################################################################################

# TITLE: Section 4 - Using the "type()" Function (2 minutes)

# Sometimes when you are dealing with variables, you are going to want to check the type of
# the variable to make sure you are correctly using it. Python has a built in function for this!
# To check the type of a variable, simply use type([some_variable_here]). Here's a bunch of
# different variables that we can test this with:

num1, string1, bool1, flt1 = 2, "Any string", True, 12.903

# Now we use type(variable) to check.. Don't forget we need to use print() also to see an output.

print("num1:", type(num1))
print("string1:", type(string1))
print("bool1:", type(bool1))
print("flt1:", type(flt1))

# TODO: Section 4 of TODO 2 (2 minutes for students, 2 minute demo)

####################################################################################################

# TITLE: Section 5 - Type Conversions (4 minutes)

# Python also makes it pretty easy to convert types into other types. For example,
# you can convert integers to strings by wrapping the variable in the string
# function to make concatenation possible as seen below:

player_name = "Lebron James"
player_weight = 250

print(player_name + " weighs " + str(player_weight) + " pounds.")

# Similarly, you can convert a variable that has an integer as its value into a float:

num = 18
floated_num = float(num)
print(floated_num)

# See below on how to convert the different data types

# String: str()
# Float: float()
# Integer: integer()
# Boolean: bool()

# TODO: Section 5 of TODO 2 (5 minutes for students, 3 minute demo)
