""" 
In this lesson, we will go over some more function work as well as using a 
funcitons return value in other functions.
"""

# First, let's review a concept from lesson 6: pop(). If you recall, pop()
# is used to remove items from a list (typically the last item) and return that value.
# Here's a little refresher on how that works!

teams = ["NY Liberty", "Chicago Sky", "Atlanta Dream"]
popped_team = teams.pop()
print(popped_team)

# This is possible because pop() is an in-built python function and returns the value of pop().
# This practice is also possible by using 'return' in custom python functions which we will be
# going over in this lesson. 

###################################################################################################

# Let's walk through how to use functions and return values with one another. We will
# write a program that specifies what type of pizza pie a user wants with separate functions
# for each of the following. One function should ask a user what size they want and only
# accept small, medium, or large. Another function should ask about toppings, but tell the
# user they don't have pepperoni (if they ask for pepperoni). Our last function should confirm
# the order with the user.

def sizeInquiry():
    """Ask a user what size pizza they want and return it if it is a valid response"""

    sizeOfPie = input("What size pie do you want? (small, medium, or large): ")
    acceptableInputs = ["small", "medium", "large"]
    if (sizeOfPie not in acceptableInputs):
        print("Try again and enter a valid pizza size.")
        return False
    else:
        return sizeOfPie

def toppingsInquiry():
    """
    Ask a user what toppings they want- make sure to let them know we dont 
    have pepperoni if they ask!
    """

    toppings = input("What toppings would you like to have with your pizza?: (separate your toppings with commas and no spaces in between) ")
    # Lets split the user's string into separate items in a list. We want to make sure 
    # they didnt try to order pepperoni!
    listOfToppings = toppings.split(",")

    if ("pepperoni" in listOfToppings):
        followUp = input("Sorry dog, we don't have pepperoni. Do you want to change your order? (y/n) ")
        if (followUp == "y"):
            return False
        if (followUp == "n"):
            listOfToppings.remove("pepperoni")
            toppingsString = ", ".join(listOfToppings)
            return toppingsString
    else:
        return toppings

def formatOrder(s, t):
    """Create a basic formatted string to output to our user"""

    userMessage = f"Your order is for a {s} pizza with {t}"
    return userMessage

def main():
    """Guide a user through ordering a pizza"""

    # The return value of a function call can be set equal to a variable.
    size = sizeInquiry()
    if (size is False):
        # If the input value was incorrect and returned False, then we want to return 
        # a main function call to start over.
        return main()

    toppings = toppingsInquiry()
    if (toppings is False):
        # If the input value was incorrect and returned False, then we want 
        # to return a main function call to start over.
        return main()

    message = formatOrder(size, toppings)
    print(message)

main()

####################################################################################################

# Let's develop a small program using multiple functions to create a game. A user will input how
# many times they want to play the game. The game is to guess a number between one and ten.
# If they guess the number correctly, the program should tell the user they won. If they guess
# incorrectly, it should tell them they were wrong.

# Python has some pre-defined packages you can import functions from. We will explore this more in-
# depth later in the course. The "random" package has a function used to generate a random integer.

from random import randint # Remember import statements generally belong at the top of a file.

def inquireUserGames():
    """ask a user how many times they want to play"""

    timesToPlay = input("How many times would you like to play the 'Guess the Number' game?: ")
    numTimesToPlay = int(timesToPlay)
    userStartedGameString = f"You've signed on to play {timesToPlay} games!"
    # Let's return TWO variables to display some cool Python functionality. We can now
    # set two variables equal to the value of calling this function.
    return numTimesToPlay, userStartedGameString

def playTheGame():
    """ask user for a number between 1 and 10, generate a random number between 1 and 10, then see
    if those numbers match. If they do, congratulate the user! If not, tell 'em they guess wrong."""

    # Generate a random number between 1 and 10.
    randomNumber = randint(1, 10)
    # Get an input from the user.
    promptUserForNumber = input("Guess a number between 1 and 10: ")
    # Convert their input into an integer so you can check for equality between
    # the input and the random number generated.
    userNumber = int(promptUserForNumber)

    # Check if the random number and user number equal each other.
    if (randomNumber == userNumber):
        print("You guessed correctly! Number", userNumber, "was the correct guess.", "\n")
    else:
        print("Wrong Answer!!! Number", randomNumber, "doesnt equal", userNumber, "\n")

def initializeGame():
    """Lets initialize our game and call the inquireUserGames function."""

    # The first variable will equal the first returned value, and the second variable
    # will equal the second returned value.
    userGameCount, userWelcomeString = inquireUserGames()
    print("\n", userWelcomeString, "\n")

    # userGameCount will equal the user's input from their desired number of games to play.
    # userWelcomeString will equal the output "You've signed on to play {userGameCount} games!"
    # This while loop will continue to run until userGameCount equals zero.
    while userGameCount:
        playTheGame()
        # Every time we run the playTheGame function we want to decrement the userGameCount
        # by one until it hits zero, at which point the while loop will stop running.
        userGameCount -= 1

# Lets call the initializeGame function to get things going!
initializeGame()

# TODO: Complete TODO 13
