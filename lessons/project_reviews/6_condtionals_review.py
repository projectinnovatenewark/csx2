# TItle: Conditionals

# Conditionals are used to determine if certain blocks of code will run or not. Below are a few
# examples of the different types of conditionals statements:

num1 = 40
num2 = 0
num3 = 40

if (num1 == num3): # This is an if statement. It executes exactly as it reads.
                   #"If something is true, then execute some code."
  print(f"num1 is equal to num3")
elif (num2 < 0): # This is an elif statement. elif statements will only run when all above if
                 # statements are false. Like an if statement, elif statements test on a condition.
  print(f"num2: {num2} is a negative number")
else: # This is an else statement. This will only execute if all other conditions are not met.
  print("None of the above were true!")

# Python supports the usual logical conditions from mathematics:
# == : equal to
# != : is not equal to
# > : greater than
# >= : greater than or equal to
# < : less than
# <= : less than or equal to

# TODO: Hey Teacher, change around the values of the above variable to achieve different outcomes.