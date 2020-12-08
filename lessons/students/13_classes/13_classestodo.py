"""
Creating classes for your classmates
"""

# TODO: Section 1
# Define a class of "Dog". Ensure that all of the class instantiations of "Dog" have an
# attribute of "animal_type" set to "mammal". This dog should have some attributes set
# in it's init function including name, breed, and age. It should also have a list set to
# one of it's attributes by default- the attribute should be called "activities". Define a
# function on this class that allows a user to add an acitivity to an instance of a "Dog" class.

####################################################################################################

# TODO: Section 2
# Instantiate the class defined below with the correct data types for each attribute.
# Make sure to assign the right type of data to the class instantiation based on it's name.

class Country:
  def __init__(self, name, age, population, colors):
    self.name = name
    self.age = age
    self.population = population
    self.colors = colors
