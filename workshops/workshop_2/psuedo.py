"""
Pseudocode and problem solving with code.
"""

# TITLE: Definitions

# Computer code is a set of instructions given to a computer to execute some functionality.

# Pseudocode is a set of instructions written in plain English to describe what a program
# is supposed to do.

####################################################################################################

# TITLE: System Design

# 1. Gather requirements: What is the use case? Who is the end-user? Why is this needed?

# 2. Project constraints: Are there limitations? What is allowed and not allowed?

# 3. Designing for your user: What are the steps an end-user would take to use this program?

# TITLE: Profit Report Program

# Project Description: A user should submit their total revenue, subtract each expense individually,
# and calculate the profit (revenue - expenses).

####################################################################################################

# TITLE: System Design

# TODO: Review the system design steps as a class and design the program below.

# 1) Requirements: 

# 2) Constraints:

# 3) Design:

####################################################################################################

# TITLE: Pseudocode

# TODO: Pseudocode the program by outlining the steps needed to code it.

####################################################################################################

# TITLE: Computer Code

# TODO: Review for loops and while loops at the bottom of the file, teach functions
# TODO: and function return values.

####################################################################################################

# TITLE: Review for Program


# Loops

listy = [1, 2, 3, 4, 5]
dicty = {"key1": "value1", "key2": "value2"}
stringy = "Hello I'm awesome"

val = dicty["key2"]
print(val)
print(dicty["key2"])

for l in listy:
    print(l)

for d in dicty:
    print(d)
    print(dicty[d])

for l in stringy:
    print(l)

while listy:
    remove = listy.pop()
    print(remove)
    print(listy)

number = 5
while number:
    print(number)
    number = number - 1

number = 8
while number > 5:
    print(number)
    number = number - 1

# Conditions

user_input = input("Would you like to continue the program? (Yes/No)")

if (user_input == "Yes"):
    print("We can continue the program")
elif (user_input == "Y" or user_input == "y" or user_input == "yes"):
    print("We can continue the program- but enter 'Yes' next time!")
else:
    print("Thanks for using the program!")

# Functions


