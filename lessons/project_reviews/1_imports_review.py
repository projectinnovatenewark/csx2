# # TITLE: Import modules, packages, and files

# import datetime
# # Here datetime is a module. To use the functionality of a module, package, or file we must use
# # dot (.) notation.
# print(datetime.datetime.now())

# ####################################################################################################

# # Title: Import funcitons and other data types

# from datetime import datetime
# # You can also *import* specific functions, classes, or other data types *from* the module,
# # package, or file.

# # Now when printing the current time and date, we only need to print "datetime.now()"; removing
# # the first "datetime" from the previous example.
# print(datetime.now())

# ####################################################################################################

# Title: Storing imports as a variable

from datetime import datetime as dt
# Lastly, imports can be stored *as* a variable. Then the variable can be used just as it would in
# the previous example.
print(dt.now())