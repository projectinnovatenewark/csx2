"""
if, elif, else and iteratable operations
"""

num = 3 # FIXME: Teacher, try changing this number up to satisfy the different conditions.

if (num > 0):
    print(num, "is a positive number.")
if (num > 2): # any number of if statements will be evaluated upon running the code
    print(num, "is greater than 2.")
elif (num < 0): # the elif statement will only be triggered if none of the "if" statements are true.
    print(num, "is a negative number.")
else: # the else statement will only run if none of the conditions above it are true.
    print(num, "is a zero value.")

####################################################################################################

# notice how we used the same variable of "num" from the above function but reassigned its value.
# we can do that because it is a variable and NOT a constant

num = 2
num = 533

if (num % 2 == 0):
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

# TODO: Section 1 of TODO 11

####################################################################################################

# lets take 6 and add each number between it and zero to a variable (i.e. 6 + 5 + 4.....0)
countdown = 6
countdown_sum = 0

while countdown > 0:
    countdown_sum += countdown # += or -= will add/subtract a number to a variable and then
                               # reassign the NEW value to that variable. In this example,
                               # we are doing `countdown_sum = countdown_sum + countdown`
                               # on this line.

    countdown -= 1 # in this case of -= it will subtract one from countdown and then countdown will
                   # equal countdown - 1. so, in the first iteration of the while loop, countdown
                   # will go from 6 to 5
    print("countdown equals", countdown)
    print("countdown sum equals", countdown_sum)

# this code below the while loop will NOT run until the while loop 'breaks', which would happen when
# the condition of countdown > 0 is no longer true
print("countdown now equals: ", countdown)

print("the final countdown equals: ", countdown_sum)

# TODO: Section 2 of TODO 11

####################################################################################################

# As a reminder, before jumping into a new way of iterating through a list, here is a review on
# list comprehensions from week 2. They may seem similar to the functions in the next section,
# but its important to not confuse them and understand each individually.

# List comprehensions are ways to define potentially lengthy lists in one line. In this case, we are
# iterating through every number between 0 and 9, squaring the number, and then putting it in a list
# called "squares".
squares = [i**2 for i in range(10)]
print("Squares list", squares)

# What if we wanted to only find the squares of odd numbers? We can add a condition to the list
# comprehension. The order of a list comprehension is action - for loop - conditional (optional).
squares_of_odd_numbers = [i**2 for i in range(1, 10) if i % 2 != 0]
print("Squares of odd numbers list", squares_of_odd_numbers)

####################################################################################################

# In the next 3 sections, you can see that the condition actually comes before the "for" statement.
# This differs from list comprehensions, where the action comes before the "for" statement.

number_list = [3, 15, 31, 1, 11, 107]

# `all` is helpful when you want to assess every value of a set
# lets check if all the number are odd
if all(number % 2 != 0 for number in number_list):
    print("all the numbers are odd")

####################################################################################################

number_list = [3, 15, 31, 1, 11, 107]

# `not in` checks to see if an item is not in a list
if (1000000 not in number_list):
    print("there is not one million in the number list")

# `in` checks to see if an item is in a list
if (15 in number_list):
    print("fifteen is in the number list")

####################################################################################################

number_list = [3, 15, 31, 1, 11, 107]

# `any` is helpful when you want to see if a single value (or more!) satisfies your conditional
if any(number % 2 == 0 for number in number_list):
    print("there is at least one even number")

####################################################################################################

number_list = [3, 15, 31, 1, 11, 107]

# `enumerate` gives you the index position and actual value of the items in a list
for number in enumerate(number_list):
    print(number) # enumerate returns you a tuple in the form of (index, value). Remember- tuples are
                  # lists that cannot be changed!
    print(number[0]) # this will be the index number
    print(number[1]) # this will be the item

# TODO: Section 3 of TODO 11
####################################################################################################

# `switch` statements are common in other languages. What a switch statement does is take a
# case and apply it. Say you want to know what the name of the day is by it's place in the
# week. This function is the equivalent of a switch case

def week(i):
    """this function serves as a switch case equivalent in Python"""

    switcher = {
        1:'Sunday',
        2:'Monday',
        3:'Tuesday',
        4:'Wednesday',
        5:'Thursday',
        6:'Friday',
        7:'Saturday'
    }
    # this will return the printed statement of the number being passed as an argument
    # or it will return "invalid day of the week" if that number isn't in the switcher dictionary
    return print(switcher.get(i, "Invalid day of week"))

week(9)
