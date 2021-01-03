# Title: Creating a Python Class

# Classes are like blueprints for creating objects in programming. Classes will have "properties",
# "attributes", and "methods" that are specific to objects that are instances of that given class.

# Below, we are defining the class "Athlete" with the attributes first_name, last_name, sport,
# and skill_level.

class Athlete:

  # The __init__ function is a special Python function called automatically on creation of objects.
  # Doing so classifies the __init__ function as a "constructor" in computer science terms. To use
  # the __init__ function, 

  def __init__(self, first_name, last_name, sport, skill_level):
    self.first_name = first_name
    self.last_name = last_name
    self.sport = sport
    self.skill_level = skill_level


# creating a python class
# attributes
# methods
# instantiation

# relate to Buzzer(4) # 4 is a gpio pin
# .beep is a method of buzzer
# FIXME
# .when_motion is a property