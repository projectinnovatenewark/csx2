"""
Importing modules and other files
"""

# TITLE: Section 1 - Importing Modules (4 min)

# Last lesson we used the "math" module which has some useful functions like hypot(), an easier
# way to find the length of a right triangle's hypotenuse. There is a large number of modules
# that can be used which are built into Python. Lets import a built in Python module
# used to generate random numbers called "random".

# As we mentioned in the previous lesson, imports should generally be at the top of the file. For
# the sake of this lesson, they will be placed throughout the file for readability.
import random

# Let's use the "random()" function. This will generate a random float between 0.0 and 1.0.
# We use dot (.) notation to reference the imported module followed by the function from that
# module. You can expect the format of importing to be similar to the following layout:
# module.function_name()
rand_float = random.random()
print(rand_float)

####################################################################################################

# TITLE: Section 1.1 - Importing Specific Funcitons from Modules (5 min)

# In Python, if we only wanted to import a specific function from the "random" module, we can do the
# following:

from random import randrange # This imports the "randrange" function from the "random" module.

# We do not need to use dot notation anymore to reference our "randrange" function. The program can
# now recognize it originates from the "random" module. Let's store a random number between 1 and 10
# in a variable called "rand".

rand = randrange(1,11) # The lower bound (1) is included, but the upper bound (11) is excluded.
rand_plus_two = rand + 2 
print(f"Randomly generted number: {rand}. Here is rand + 2: {rand_plus_two}.")

####################################################################################################

# TITLE: Section 2 - Importing from Files in your directory (6 min)

# You can import data or functions from files that you create. In this folder there's a
# file called "importable_stuff.py". Let's import the file and use things from it. As you learned in
# Section 1, below is one way to import a file.
import importable_stuff

# Then, to access the constant `DAYS_OF_WEEK` from that file,
# you would do so with "dot notation" just as we did in section 1. In this import case,
# we can find the constant by doing:
print(f"Normal dot notation: {importable_stuff.DAYS_OF_WEEK}")  # TIP:
                                                                # DAYS_OF_WEEK is a list. In
                                                                # Python, lists are represented by
                                                                # items separated with commas inside
                                                                # open and closed brackets []. Open
                                                                # importable_stuff.py to check this
                                                                # out.

# You could also rename imports such as:
import importable_stuff as stuff # Now this import can be referred to going forward as "stuff".
print(f"Renaming as stuff: {stuff.DAYS_OF_WEEK}")

# Similar to Section 1, we can import specific objects from importable_stuff.py. If we wanted to
# specifically import DAYS_OF_WEEK, then we use the following:
from importable_stuff import DAYS_OF_WEEK
print(f"Importing the constant: {DAYS_OF_WEEK}")

# You could also combine the last two concepts and rename the object you are importing by doing the
# below:
from importable_stuff import DAYS_OF_WEEK as week
print(f"Importing and renaming the constant: {week}")

# Lastly, if you want to import multiple objects from another file, there's
# an easier way to do that than writing multiple import lines. This would look like the following:
from importable_stuff import DAYS_OF_WEEK, MONTHS
print(f"DAYS_OF_WEEK: {DAYS_OF_WEEK} \nMONTHS: {MONTHS}") # "\n" prints whatever follows on a new line.

# TODO: Complete TODO 10
