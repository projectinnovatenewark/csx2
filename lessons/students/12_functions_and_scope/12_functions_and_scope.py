# """
# Using functions and understanding scope
# """

# # TITLE: Section 1 - Printing Function Outputs
# # A function is a block of code that executes some task. Functions are defined using the format:
# # "def function_name(parameter_name):" The parameter name can be anything you want (just like
# # variables), so whatever you pass as an argument to the function when you "call" it will be
# # renamed to the parameter you set when defining the function. To "call" a function simply means
# # to run it.
# def add_ten(n): # "add_ten" is the name of the function and "n" is the parameter name.
#     new_num = n + 10 # Lines of code indented after the function is defined are considered to be
#                     # in the scope of the function like in loops.
#     return new_num   # This is also in the scope of "add_ten()".

# print("This is not a part of the function") # Since this line is not indented within the function,
#                                             # it is outside the scope of the function and the
#                                             # function definition has therefore ended

#     # print("This is not in the scope of 'add_ten()'") # FIXME: This will not be in the scope of
#     #                                                 # FIXME: add_ten() because the function ended
#     #                                                 # FIXME: in line 14. Comment out to continue.

# # Now that we are at the leftmost part of the page, we have exited the scope of the function above.
# # This function should now take the argument passed, which is 3, and add ten to it. It will then
# # return that value. What you see below is called "calling a function", which basically runs the
# # function with the given input.
# print("First call to add_ten function: ")
# add_ten(3) # "3" is the argument we pass, which will be assigned to the parameter "n" within the
#           # function call.

# # Huh, why didnt this function call create an output?! Well, we didn't print it!! We could either
# # 1) change the "return" value to be a print statement in the function
# # ...OR...
# # 2) we can print the function call itself!

# # To do it the first way, you would just replace "return new_num" with "print(new_num)" within the
# # function definition. Line 13 would then look like the following: "print(new_num)".
# # TODO: Teacher - show the class how to do this.

# # Or to use option 2, you can print the function call like the following. 
# print("Second call to add_ten function: ")
# print(add_ten(5))

# # Functions also don't necessarily need parameters. They can perform some operation that doesn't require an
# # argument. In this case, we will just print a "global" variable that would be accessible to the
# # whole file, including within the scope of this function!
# random_num = 12345
# def give_output():
#     print(random_num)

# # This would call the above function which would print out the "random_num" variable.
# print("Calling our give_output function: ")
# give_output()

# # TODO: Section 1 of TODO 10 (4 min for students, 1 min for demo)
####################################################################################################

# # TITLE: Section 2 - Calling Functions with Other Functions
# # Functions are great because you can have them "return" a value. Generally, this will be whatever
# # you wanted the funciton to accomplish. These return values can then be used elsewhere in your file
# # inluding in other functions. Below we will show you how the "control" of a program will navigate
# # the code. Use "Control #" to follow along how your code is processed.

# def add_two(j):
#     new_num = j + 2
#     return new_num # Control 3: "j", which is equal to the argument of 9 that was passed, has 2
#                   # added to it and 11 is returned.

# added_two = add_two(3)
# print(f"We called 'add_two' and set it's return value equal to a variable. That variable equals {added_two}")

# def add_five(k):
#     return k + 5 # Control 6: "k", which is equal to the arugment of 11 that was passed, has 5
#                  # added to it and that value of 16 is returned.

# def adding_Chain(i):
#     curr_num = add_two(i) # Control 2: add_two function is called and passed "i", which is equal to 9
#     # Control 4: The value of 11 that was returned from the add_two function call is set to a
#     # variable called curr_num

#     new_num = add_five(curr_num) # Control 5: add_five function is called and passed curr_num, which is equal to 11
#     # Control 7: The value of 16 that was returned from the add_five function call is set to a
#     # variable called new_num

#     return new_num # Control 8: The new_num variable, which equals 16, is returned and the
#                    # adding_Chain function call has ended

# print(adding_Chain(9)) # Control 1: the adding_Chain function gets called and passed 9 as an argument
#                       # Control 9: After the function call is complete, the print statement prints
#                       #            the return value.

# # TODO: Section 2 of TODO 10 (4 min for students, 1 min for demo)
####################################################################################################

# TITLE: Section 2.1 - Using Return Values with Conditionals (8 minutes)
# Calling functions within other functions and using conditions.

# Having return values from functions is important when you want to use that value,
# and not just log it in that moment. Here is an example of one such case:

def days_activities(type_of_day):
    """Analyze a user's input and return a message for them"""
    # These if statements check to see if the type_of_day argument is equal to something- in our case
    # we are checking in three different statements if type_of_day is either "fun", "productive",
    # or "relaxing". If one of those if's is true, then we do whatever is within the scope of that if
    # block. If none of the if statements are true, we execute what is in the "else" block.

    if (type_of_day == "fun"):
        day_string = "You should enjoy some of your favorite activities"
    elif (type_of_day == "productive"):
        day_string = "Let's get some work done, player!"
    elif (type_of_day == "relaxing"):
        day_string = "You work too hard, and this day is all about YOU. Do NOTHING and enjoy it, you deserve it :)"
    else:
        day_string = "I can only compute one of the three provided types of days. Try again, chief!"

    # This will return the variable day_string and end the function. When a return statement is run,
    # the function will effectively stop running.
    return day_string

def inquire_day():
    """This function will ask the user what type of day they want to have"""

    # We will take the user input value and pass it as an argument to our "days_activities" function.
    userDay = input("What type of day do you want to have? You can choose from fun, productive, or relaxing. Enter your choice!: ")

    # This variable below would be equal to the return value of the function call
    userMessage = days_activities(userDay)
    print(userMessage)

# This is a regular old function call
inquire_day()

# TODO: Hey, Teach! You should have your students walk you through the control of the above function
# TODO: call. Make sure the class understands the flow of the program 🚀

# TODO: Section 2.1 of TODO 10 (4 min for students, 1 min for demo)
####################################################################################################

<<<<<<< HEAD
# # TITLE: Section 3 - Working with Scope
# # Below are examples of using variables & the timing of a function call to portray scope.
# # Here we call "s" after the function is called, which will return a NameError
# def func():
#     print(s)
# func()
# s = "I love Paris in the summer!"

# # Here, since the variable is declared before the function is called, it will print the "s2" value
# def func2():
#     print(s2)
# s2 = "I love San Diego in the summer!"
# func2()

# # Here, the variable in the function is referenced within the function's scope, therefore it will
# # print the "I love London" statement
# def func3():
#     s3 = "I love London!"
#     print(s3)

# s3 = "I love Malaysia!"
# func3()

# print(s3)
=======
# TITLE: Section 3 - Working with Scope (5 minutes)
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
>>>>>>> 1a5c38be47fc92953e899394e98c6766a7e28785
