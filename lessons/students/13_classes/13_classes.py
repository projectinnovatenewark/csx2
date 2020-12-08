"""
Understanding classes and scope within a class
"""

# TITLE: Section 1 - Classes Introduction (10 minutes)

# Classes are like blueprints for creating objects in programming. Classes will have properties and
# attributes that are privy only to objects instantiated in the given class. We will go over
# instatiating an instance of a class in a bit, but first we will define a class named "Cat".

# TIP:
# Classes are defined with the first letter as a capital and the rest of the name using camel case,
# whereas snake case is generally used to define variables and functions.
# This is "camelCase"
# This is "snake_case"
# This is a "CamelCaseClass"

class Cat: # Here we are defining the class "Cat"

    kind = 'feline' # This is a "property". Properties are shared by all instances of a class.

    # All classes have an "__init__" function.  __init__ is a special Python function that is
    # called automatically on an object creation statement. The computer science term for it is
    # constructor, as its job is to build an object of the type specified by the class.
    
    def __init__(self, name): # The __init__ funciton takes at least 2 parameters; self and 1 or
        self.name = name      # more attributes. The param, "self", refers to itself as an
                              # instantiated object. The param, "name", is an attribute of the "Cat"
                              # class. You assign attributes using "self.var_name = var_name" iwthin
                              #   the scope of the "__init__" function.

# Now we want to instantiate an instance of Cat. To do so, we need to assign each of the attributes
# (other than "self") defined in the "__init__" function above. The instantiation can then be stored
# in a variable in the format "var = ClassName("arg1, arg2")
felix = Cat('Felix') # The Cat class only takes one argument of name, so we instantiate the class
                     # with "Felix".
boots = Cat('Boots') # The Cat class only takes one argument of name, so we instantiate the class
                     # with "Boots".

# Since kind is a property and therefore declared for all cats, the kind will be shared by both
# Felix and Boots. You can use dot notation with the variable names used to store the class
# instantiations to read  a classes of attributes.
print(f"felix.kind: {felix.kind}") # shared by all Cats
print(f"boots.kind: {boots.kind}") # shared by all Cats
print(f"felix.name: {felix.name}") # unique to felix
print(f"boots.name: {boots.name}") # unique to boots

# TODO Section 1 of TODO 13 (7 minutes for students, 5 minute demo)

####################################################################################################

# TITLE: Section 2 - Methods for Classes(5 minutes)

# Methods are functions that are defined within the scope of a class. Since methods are defined
# within the scope of a class, they can only be called with an instantiated class object using dot
# notation. Below we are redefining the "Cat" class and defining a method that will append an
# activity to a given cat's day.

class Cat:

    def __init__(self, name):
        self.name = name
        self.activities = [] # This creates a new empty list for each Cat, but will not be used
                            # to instantiate the class. It doesn't need to be added as an argument
                            # during instantiation because it is not a parameter in the "__init__"
                            # function.

    def add_activity(self, activity):   # This is a method defined within the scope of the
        self.activities.append(activity) # "Cat" class.

felix = Cat('Felix') # The Cat class only takes one argument of name, so we instantiate the class
                     # with "Felix".
boots = Cat('Boots') # The Cat class only takes one argument of name, so we instantiate the class
                     # with "Boots".

# To call the method, we use dot notation in the format of ("var.method(arg1, arg2")
felix.add_activity('hit yarn')      # Here we are appending the activity "hit yarn" to Felix's list
                                    # of activities.
boots.add_activity('attack bird')   # Here we are appending the activity "attack bird" to Boots's list
                                    # of activities.

# We can print the activities just like any other attribute using dot notation.

print(f"Here is a list of {felix.name}'s activities for the day: \n {felix.activities}")
print(f"Here is a list of {boots.name}'s activities for the day: \n {boots.activities}")

# TIP: Remember "\n" will create a new line for anything after it in a print statement.


# TODO Section 2 of TODO 13 (5 minutes for students, 4 minute demo)
