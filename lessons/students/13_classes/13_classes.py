"""
Understanding classes and scope within a class
"""

# The variable Cat could have been named anything. The "Cat()" says to
# create a new object and to run the strangely named function __init__ (two
# underscores before and after 'init').
# __init__ is a special Python function that it is called automatically on an object
# creation statement. The computer science term for it is constructor, as its
# job is to build an object of the type specified by the class.
# The 'self' parameter in __init__ just refers to the instance being created, in
# this case Cat. __init__ creates the object, putting in default values for all the
# fields, then returns the object into the variable Cat. The main program then
# goes on to set the various fields of the Cat object, and then access and print
# one of them. Note that the fields of an object can be set/accessed with a
# reference of the form:
# object.field
​
# As shown below, we also pass an inital value into the object Cat(). We then set
# the input to "name" inside the init constructor and set the Cat's name value
# to the input it receives
​
# For more info on classes, refer to the Python docs:
# https://docs.python.org/3/tutorial/classes.html

####################################################################################################

# TITLE: Section 1- Classes Introduction (12 minutes)
​
class Cat:
​
    kind = 'feline' # class attribute shared by all instances
​
    def __init__(self, name):
        self.name = name    # instance attribute unique to each instance
​
# this will create two new instances of a Cat class with the self.names of Fido and Bella
d = Cat('Fido')
e = Cat('Bella')
​
# since kind is declared for all cats, the kind will be shared by both Fido and Bella
print("d.kind", d.kind)                  # shared by all Cats
print("e.kind", e.kind)                  # shared by all Cats
print("d.name", d.name)                  # unique to d
print("e.name", e.name)                  # unique to e
​
class Cat:
​
    tricks = [] # mistaken use of a class attribute shared by all Cats due to scope
​
    def __init__(self, name):
        self.name = name
​
    def add_trick(self, trick):
        self.tricks.append(trick)
​
d = Cat('Fido')
e = Cat('Bella')
d.add_trick('hit yarn')
e.add_trick('attack bird')
print(d.tricks)  
​
class Cat:
​
    def __init__(self, name):
        self.name = name
        self.tricks = [] # TIP: creates a new empty list for each Cat, and DOESNT
                         # TIP: set this value upon initializing
​
    def add_trick(self, trick):
        self.tricks.append(trick)
​
d = Cat('Fido')
e = Cat('Bella')
d.add_trick('hit yarn')
e.add_trick('attack bird')
d.tricks
e.tricks

# TODO Section 1 of TODO 13 (7 minutes for students, 5 minute demo)

####################################################################################################

# TITLE: Section 2- Class Instantiation Review (5 minutes)
​
# Take the below class.
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def identifier(self):
        print(f"My name is {self.fname} {self.lname}")

# TODO Section 2 of TODO 13 (5 minutes for students, 3 minute demo)