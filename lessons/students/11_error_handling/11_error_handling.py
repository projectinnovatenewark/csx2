"""
Common errors you will/may have already encounter(ed).
"""

# TITLE: Section 1: No Dividing by Zero! (3 min)
# Below are a few examples of errors you will undoubtedly see in your time as a programmer.
# These errors will show up in your terminal letting you know where the problem is, and the
# type of error it is. Our first error is a ZeroDivisionError. This is pretty self explanatory.
# As we know from math classes, you can't divide a number by 0 and that rule doesn't go away
# in python. Pay attention to the message in the terminal, as it tells you where python thinks 
# there is an error. 

# ZeroDivisionError: division by zero
number = 10 * (1/0) # FIXME: Comment out this line once this error has been demoed.
print(number)

####################################################################################################

# TITLE: Section 2: NameErrors are Easy (3 min)
# You'll see below when we run our code again that we get a 'NameError'. This occurs when you try to 
# use a variable in your program that has not been defined yet. The below code uses the 
# variable 'spam' when 'spam' hasn't been defined (given a value). Again pay attention
# to your terminal. It lets you know where the problem is and gives hints as to what's wrong!

# NameError: name 'spam' is not defined
equation = 4 + spam * 3 # FIXME: Comment out this line once this error has been demoed.
print(equation)

####################################################################################################

# TITLE: Know Your Types (3 min)
# Lastly let's take a look a a 'TypeError'. In this case, the error is occuring
# because we are trying to add together a string with an integer. Because a string is 
# involved, python thinks you are trying to concatenate '2' + 2, instead of using addition. 
# As we know form earlier lessons, we can't concatenate strings and integers, so 
# python throws us this error.

# TypeError: Can't convert 'int' object to str implicitly
four = '2' + 2 # FIXME: Comment out this line once this error has been demoed.
print(four)

# TODO: Complete TODO 8
