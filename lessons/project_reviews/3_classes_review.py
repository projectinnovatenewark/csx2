# Title: Creating a Python Class

# Classes are like blueprints for creating objects in programming. Classes will have "properties",
# "attributes", and "methods" that are specific to objects that are instances of that given class.

# Below, we are defining the class "Athlete" with the attributes first_name, last_name, sport,
# and skill_level.

class Athlete:

  # The __init__ function is a special Python function called automatically on creation of objects.
  # Doing so classifies the __init__ function as a "constructor" in computer science terms. To use
  # the __init__ function, you must pass at least 2 parameters, "self", and 1 or more attributes.

  def __init__(self, first_name, last_name, sport, skill_level):
    self.first_name = first_name
    self.last_name = last_name
    self.sport = sport
    self.skill_level = skill_level

# Now that we have our class mappedout, we want to create an instance of "Athlete", also known as
# instantiating. We will assign each attribute a value from the __init__ function above and store
# the instantiation in a variable.

# variable = ClassName(first_name, last_name, sport, skill_level)
lbj = Athlete("LeBron", "James", "basketball", "professional")

# Now that the class is instantiated, it can be referenced throughout the rest of the file using dot
# notation in the format "variable.attribute".
print(f"{lbj.first_name} {lbj.last_name} is a {lbj.skill_level} {lbj.sport} player.")

####################################################################################################

# Title: Class Methods

# Below we are redefining the class from the previous section.
class Athlete:

  def __init__(self, first_name, last_name, sport, skill_level):
    self.first_name = first_name
    self.last_name = last_name
    self.sport = sport
    self.skill_level = skill_level

  # Below we are now defining a method. Methods are functions defined within the scope of a class.
  # That means only instantiated classes of "Athlete" will be able to be used to call the method.
  # Our below method will print the print statement from earlier, but will be able to be used more
  # efficiently for more than one class instantiation.

  def printer(self): # Here, self is the only parameter we need, which gives the function access to
                     # the instantiated class.
    # "self" is then used to reference each attribute of the given class.
    print(f"{self.first_name} {self.last_name} is a {self.skill_level} {self.sport} player.")

meg_rap = Athlete("Megan", "Rapinoe", "soccer", "professional") # This is a class instantiation
kd = Athlete("Karl", "Durant", "basketball", "amateur") # Another class instantiation
meg_rap.printer() # Calling the "printer()" method
kd.printer() # Another call to the "printer()" method

####################################################################################################

# Title: Class Properties

  # Properties are used for getting and setting class data. Properties are intended to give the
  # option of defining a function that takes 0 arguments. This allows the user to interact with the
  # property as if it was an actual attribute of the class. You can tell when a proprty is defined
  # when there is a "@property" decorator above it's definition.

  # Here we have our class from earlier in the lesson with a new attribute "year_born". 

class Athlete:

  def __init__(self, first_name, last_name, sport, skill_level, year_born):
    self.first_name = first_name
    self.last_name = last_name
    self.sport = sport
    self.skill_level = skill_level
    self.year_born = year_born

  def printer(self):
    print(f"{self.first_name} {self.last_name} is a {self.skill_level} {self.sport} player.")

  @property # This is the decorator.
  def age(self): # Properties only take a parameter of "self" to give access to its class
                     # instantiation
    year = 2021
    age = year - self.year_born # Age will be a quick calculation accessible as if it was an
                                # attribute.
    return age # Here we return age so that we get an output

trout = Athlete("Mike", "Trout", "baseball", "professional", 1991) # Instantiating with the new
                                                                   # attribute year_born.

# Since we have a new instance of class, we can use dot notation to find the age of our athlete for
# the year 2021.

print(trout.age)


# TODO: Hey Teacher, head back over to fam_cam.py and recap how we use the different classes from 
# TODO: the gpiozero library.