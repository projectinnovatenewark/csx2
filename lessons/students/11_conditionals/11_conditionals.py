"""
if, elif, else and iteratable operations
"""

# TITLE: Section 1 - If Statements
# In Python, we can execute a certain block of code based on a condition. This is useful when you
# only want a program to run IF a condition is satisfied. The most basic form of a condtional
# statement is an "if" statement.

bool1 = True
bool2 = False

if (bool1 == True): # TODO: Teacher, change the if statement from "bool1" to "bool2".
    print("It's true! It's true!")

# In plain english, the example above states that IF bool1 is true, the print statement
# "It's true! It's true!" will be printed.

# You might have noticed the "==". Using a "==" is Python for "equal to". We can't use a single "="
# because Python would think you are setting a variable. Below are some of the many ways you can
# test conditions (formatted as "symbol" : "plain english"):
# == : equal to
# != : is not equal to
# > : greater than
# >= : greater than or equal to
# < : less than
# <= : less than or equal to

pin = "Project Innovate Newark"

if (pin != "Project Initiate Newark"): # Testing if the value of "pin" is not equal to the string,
                                       # "Project Initiate Newark"
    print("This isn't what PIN stands for!") # TODO: Will this statement be printed?

####################################################################################################

# TITLE: Section 1.1 - Else Statements
# An else statement is a conditional statement that will be executed when all other conditions
# haven't been met. An else statements always comes after an if statement and cannot be used as a 
# standalone conditional.

num = 2 # TODO: Teacher, try changing this number up to satisfy the different conditions.

if (num > 20): 
    print("It's true! It's true!")
else: # Here we use an else statement to say, "if the above condition is not true, then execute
      # the following code"
    print("The variable is not greater than 20!")

# You can see in the above that num is not greater than 20, so the statement "The variable is not
# greater than 20!" is printed. There isn't a condition in an else statement because it only runs if
# every conditional above is not met. 

# Here is an example from earlier with an else statement used as well. Which statement will
# be printed?
pin = "Project Innovate Newark"

if (pin == "Project Initiate Newark"):
    print("This is what PIN stands for!")
else:
    print("This isn't what PIN staands for!")

####################################################################################################

# TITLE: Section 1.2 - Elif statements
# An elif statement is like a combination of an if and else statement. An elif statement will only
# be executed when conditions above it are not met (like an else statement), BUT also test it's own
# condition (like an if statement). An elif statement will mostly come after an if statement and
# before an else statement. It also can't be used as a standalone conditional like else statements.

num1 = 10

if (num1 < 10):
    print("the number is less than 10")
elif (num1 > 5):
    print("the number is greater than 5")

# The output here is "the number is greater than 5". Python first evaluate the if statement. Since
# num1 is not less than 10, the elif is executed.

# Let's take a look now if both the first and second condition can be satisfied. What do you think
# the output will be?

num2 = 6

if (num2 < 10):
    print("the number is less than 10")
elif (num2 > 5):
    print("the number is greater than 5")

# Only the if statement was executed. That's where the "else" of the elif comes in. Remeber that an
# elif statement will only run if the above conditions are not met.

####################################################################################################

# TITLE: Section 1.3 - Using the three conditionals together

# Below we are using each of the three conditionals that we learned in the previous sections. Notice
# the order of the conditionals. The if statements are tested first, then the elif, and lastly the
# else is run if all other conditions were false. 

num = 3 # TODO: Teacher, try changing this number up to satisfy the different conditions.

if (num > 0):
    print(f"{num} is a positive number.")
if (num > 2): # Any number of if statements will be evaluated upon running the code
    print(f"{num} is greater than 2.")
elif (num < 0): # The elif statement will only be triggered if none of the "if" statements are true.
    print(f"{num} is a negative number.")
else: # The else statement will only run if none of the conditions above it are true.
    print(f"{num} is a zero value.")

# TODO: Section 1 of TODO 11

####################################################################################################

# TITLE: Section 2 - Using "and" and "or"

# If you want to test for multiple conditions that apply to the same data, you can use "and" or "or"
# statements. These are useful to make your code more readable and use less lines of code.

# Below, we are using booleans to show examples of how "and" and "or" statements return either
# true or false.

# Using "and" is great for when all conditions need to be returned as True for a single outcome.
# Basically, "if one item is true and another item is true, then return True". If one of the
# conditions returns false though, the entire if statement will return false and the block of code
# will not run.

if (True and True): # A True condition AND a True condition will return true
    print("True and True is true")

if (True and False): # A False condition AND a True condition will return false
    print("True and False is true")

if (False and False): # A False condition AND a False condition will return false
    print("False and False is true")

# Using "or" is different in that only one condition needs to be me for the if statement to 
# return True. So, "If one item is true OR another item is true, then return True." The "or" will
# cause the if statement to return true as long as one condition is satisfied.

if (True or True): # A True condition OR a True condition will return true
    print("True or True is true")

if (True or False): # A False condition OR a True condition will return true
    print("True or False is true")

if (False or False): # A False condition OR a False condition will return false
    print("False or False is true")

# TODO: Section 2 of TODO 11