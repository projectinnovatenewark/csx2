"""
Using functions and understanding scope
"""

# TITLE: Section 1 - Printing Function Outputs
# A function is a block of code that executes some task. Functions are defined using the format:
# "def functionName(parameterName):" The parameter name can be anything you want (just like
# variables), so whatever you pass as an argument to the function when you "call" it will be
# renamed to the parameter you set when defining the function. To "call" a function simply means
# to run it.
def addTen(n): # "addTen" is the name of the function and "n" is the parameter name.
    newNum = n + 10 # Lines of code indented after the function is defined are considered to be
                    # in the scope of the function.
    return newNum   # This is also in the scope of "addTen()".

print("This is not a part of the function") # Since this line is not indented within the function,
                                            # it is outside the scope of the function and the
                                            # function definition has therefore ended

    print("This is not in the scope of 'addTen()'") # FIXME: This will not be in the scope of
                                                    # FIXME: addTen() because the function ended
                                                    # FIXME: in line 14. Comment out to continue.

# Now that we are at the leftmost part of the page, we have exited the scope of the function above.
# This function should now take the argument passed, which is 3, and add ten to it. It will then
# return that value. What you see below is called "calling a function", which basically runs the
# function with the given input.
print("First call to addTen function: ")
addTen(3) # "3" is the argument we pass, which will be assigned to the parameter "n" within the
          # function call.

# Huh, why didnt this function call create an output?! Well, we didn't print it!! We could either
# 1) change the "return" value to be a print statement in the function
# ...OR...
# 2) we can print the function call itself!

# To do it the first way, you would just replace "return newNum" with "print(newNum)" within the
# function definition. Line 13 would then look like the following: "return print(newNum)".

# Or to use option 2, you can print the function call like the following. 
print("Second call to addTen function: ")
print(addTen(5))

# Functions also don't necessarily parameters. They can perform some operation that doesn't require an
# argument. In this case, we will just print a "global" variable that would be accessible to the
# whole file- including within the scope of this function!
randomNumVar = 12345
def giveOutput():
    print(randomNumVar)

# This would call the above function which would print out the randomNumVar variable.
print("Calling our giveOutput function: ")
giveOutput()

# TODO: Section 1 of TODO 10 (4 min for students, 1 min for demo)
####################################################################################################

# TITLE: Section 2 - Calling Functions with Other Functions
# Functions are great because you can have them "return" a value. Generally, this will be whatever
# you wanted the funciton to accomplish. These return values can then be used elsewhere in your file
# inluding in other functions. Below we will show you how the "control" of a program will navigate
# the code. Use "Control #" to follow along how your code is processed.

def addTwo(j):
    newNum = j + 2
    return newNum # Control 3: "j", which is equal to the argument of 9 that was passed, has 2
                  # added to it and 11 is returned.

added_two = addTwo(3)
print(f"We called 'addTwo' and set it's return value equal to a variable. That variable equals {added_two}")

def addFive(k):
    return k + 5 # Control 6: "k", which is equal to the arugment of 11 that was passed, has 5
                 # added to it and that valur of 16 is returned.

def addingChain(i):
    curr_num = addTwo(i) # Control 2: addTwo function is called and passed "i", which is equal to 9
    # Control 4: The value of 11 that was returned from the addTwo function call is set to a
    # variable called curr_num

    new_num = addFive(curr_num) # Control 5: addFive function is called and passed curr_num, which is equal to 11
    # Control 7: The value of 16 that was returned from the addFive function call is set to a
    # variable called new_num

    return new_num # Control 8: The new_num variable, which equals 16, is returned and the
                   # addingChain function call has ended

print(addingChain(9)) # Control 1: the addingChain function gets called and passed 9 as an argument
# Control 9: After the function call is complete, the print statement prints the return value.

# TODO: Section 2 of TODO 10 (4 min for students, 1 min for demo)
####################################################################################################

# TITLE: Section 2.1 - Using Return Values with Conditionals
# Calling functions within other functions and using conditions.

# Having return values from functions is important when you want to use that value,
# and not just log it in that moment. Here is an example of one such case:

def daysActivities(typeOfDay):
    """Analyze a user's input and return a message for them"""
    # These if statements check to see if the typeOfDay argument is equal to something- in our case
    # we are checking in three different statements if typeOfDay is either "fun", "productive",
    # or "relaxing". If one of those if's is true, then we do whatever is within the scope of that if
    # block. If none of the if statements are true, we execute what is in the "else" block.

    if (typeOfDay == "fun"):
        dayString = "You should enjoy some of your favorite activities"
    elif (typeOfDay == "productive"):
        dayString = "Let's get some work done, player!"
    elif (typeOfDay == "relaxing"):
        dayString = "You work too hard, and this day is all about YOU. Do NOTHING and enjoy it, you deserve it :)"
    else:
        dayString = "I can only compute one of the three provided types of days. Try again, chief!"

    # This will return the variable dayString and end the function. When a return statement is run,
    # the function will effectively stop running.
    return dayString

def inquireDay():
    """This function will ask the user what type of day they want to have"""

    # We will take the user input value and pass it as an argument to our "daysActivities" function.
    userDay = input("What type of day do you want to have? You can choose from fun, productive, or relaxing. Enter your choice!: ")

    # This variable below would be equal to the return value of the function call
    userMessage = daysActivities(userDay)
    print(userMessage)

# This is a regular old function call
inquireDay()

# TODO: Hey, Teach! You should have your students walk you through the control of the above function
# TODO: call. Make sure the class understands the flow of the program 🚀

# TODO: Section 2.1 of TODO 10 (4 min for students, 1 min for demo)
####################################################################################################

# TITLE: Section 3 - Looping in Functions
# Here are a couple of dictionaries that we will work with.
example_dict_1 = {"Abigail": 78, "Brian": 86, "Carlito": 95, "Debbie": 100, "Erion": 88}
example_dict_1 = {"Andy": 73, "Brovan": 90, "Celeste": 65, "Danilo": 84, "Epsilo": 78}

# One important concept of functions is that they can be reused. Therefore, we can execute the
# same function to perform operations on BOTH of the above dictionaries.
def dictionary_reader(dictionary):
    """This function will format and print a dictionary. Just as a file gets a doc string,
    functions get one too!"""
    print("Let's output a dictionary \n")

    for student in dictionary:
        print(f"{student} got a score of {dictionary[student]} on their exam!")

    print("\n This function has finished running.")

# Here we pass the function an argument for our first dictionary:
dictionary_reader(example_dict_1)

print("\n")

# Here we see the same function performing operations with our second dictionary:
dictionary_reader(example_dict_2)

# TODO: Section 3 of TODO 10 (4 min for students, 2 min for demo)
###################################################################################################

# TITLE: Section 4 - Working with Scope
# Below are examples of using variables & the timing of a function call to portray scope.
# Here we call "s" after the function is called, which will return a NameError
def func():
    print(s)
func()
s = "I love Paris in the summer!"

# Here, since the variable is declared before the function is called, it will print the "s2" value
def func2():
    print(s2)
s2 = "I love San Diego in the summer!"
func2()

# Here, the variable in the function is referenced within the function's scope, therefore it will
# print the "I love London" statement
def func3():
    s3 = "I love London!"
    print(s3)

s3 = "I love Malaysia!"
func3()

print(s3)
