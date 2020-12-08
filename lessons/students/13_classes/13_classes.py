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
​
class Cat:
​
    kind = 'feline'         # class attribute shared by all instances
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
####################################################################################################
​
class Cat:
​
    tricks = []  # mistaken use of a class attribute shared by all Cats due to scope
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
####################################################################################################
​
class Cat:
​
    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates a new empty list for each Cat
​
    def add_trick(self, trick):
        self.tricks.append(trick)
​
d = Cat('Fido')
e = Cat('Bella')
d.add_trick('hit yarn')
e.add_trick('attak bird')
d.tricks
e.tricks
​
class Classmate:
    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age

    # this is a function
    def format_class(self):
        # here we will create a list of items to print within the class definition
        # and then join them to create one string. The dashes are just for readability.
        s = ["----------",
             # the f before each string allows for f-string literals
             # these allow for the format() function to be used, and for
             # curly braces to be used for replacement fields. link for reference:
             # https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498
             f"First Name : {self.first_name}",
             f"Last Name : {self.last_name}",
             f"City : {self.city}",
             f"Age : {self.age}"]
        return print("\n".join(s))
​
# TODO: Section 2 of the TODO 13

####################################################################################################

def complete_form(n_users):
    """The function will ask questions with the helper function of ask_user() and create Classmates.
    This function will return a list with the number of classmates you passed to this function."""
    # here we used a list comprehension to create classes for the amount n_users
    # and add them to the list
    value = [Classmate(ask_user("Enter First Name: ").title(),
                       ask_user("Enter Last Name: ").title(),
                       ask_user("Enter City: ").title(),
                       # this type=int specifies that the age input will
                       # only work if it is passed a number
                       ask_user("Enter Age: ", type=int)
                      )
             for question in range(n_users)
            ]
    # this will print the 3 Classmate objects that we arranged in our list comprehension above
    print(value)
    return value
​
def ask_user(message='', type=str):
    """this is a helper function for getting the class of Classmate's inputs"""
    user_input = ''
    while not user_input:
        try:
            # we added a call to str.strip, so user names like (spaces) and (tabs) are not allowed.
            # if spaces are entered, a ValueError will be thrown and the question will be repeated.
            # since the default type is str (for string), it will convert the input to a string. But
            # when we pass the type as int, it will convert the user input to an integer
            user_input = type(input(message).strip())
        except ValueError:
            # if this recieves a value error, it will reiterate the same question until the input is satisfied
            continue
    return user_input
​
# this line of code is explained very well here:
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# the short answer from that question is here:
# https://stackoverflow.com/a/419986/9662099
​
if __name__ == '__main__':
​
    # here we specify that we want three classes of Classmate to be instantiated
    USERS = complete_form(3)
​
    # since the complete_form function returns a list of Classmates, we can iterate
    # through that list with a for loop. Then, we will call the format_class function for
    # each of those objects
    for a in range(len(USERS)):
        USERS[a].format_class()

#####################################################################################################

# Inheritance is a powerful feature in object oriented programming.

# It refers to defining a new class with little or no modification to an existing class. 
# The new class is called derived (or child) class and the one from 
# which it inherits is called the base (or parent) class.

# Take the below class.
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def identifier(self):
        print("My name is {} {}".format(self.fname, self.lname))

# Let's say we want to create a child class for 'Students'
# That would look something like this:
# By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent.
# Then you can see we are adding Graduation year to the attributes of the Student class.
class Student(Person):
    def __init__(self, fname, lname, grad_year):
        super().__init__(fname, lname)
        self.grad_year = grad_year

    def welcome(self):
        print("This is {} {} and they graduate in {}".format(self.fname, self.lname, self.grad_year))

s1 = Student("Tiny", "Tim", 2020)
# You can still call functions that are defined in the parent class
s1.identifier()
# And here you see that you can call the function from the derived child class
s1.welcome()

# TODO: Section 3 & 4 of the TODO 13
