<div align=center><h1>USing the I/O Devices with Your Raspberry Pi</h1></div>

In this workshop, the student will learn how to properly connect each of the five (5) peripheral devices to the Pi and make them functional using Python. All students should have the Pi turned on and ready to use for the remainded of the workshop.

As a reminder, here is the list of external parts you need besides your Raspberry Pi Desktop that came with your package:

- One (1) Breadboard
- Fifteen (15) Male-Male Jumper Wires
- Fifteen (15) Female-Male Jumper Wires
- Fifteen (15) Female-Female Jumper Wires
- One (1) Motion Sensor
- Five (5) LED Lights (Assorted colors)
- Three (3) Tactile Buttons
- One (1) Buzzer
- Three (3) Ohm Resistors

<div align=center><h2>The Physical Components</h2></div>

<div><h4>1. The Breadboard</h4></div>

A breadboard is a device used for temporary or prototype electronics. Breadboards are solderless, meaning that there is no need to melt any wires to allow for an electrical current to pass through.

<div class=mdImage align=center>
    <img src="./io_workshop_images/1_breadboard.png" width="400" height="auto" />
</div>

There are **three (3)** types of rails on the breadboard we are using. The **red line** marks the *positive* rail, the **blue line** marks the *negative* rail, and the **component rails** are each row of *five pin holes*. Your breadboard has two sides of each seperated by a canal in the middle. Utilizing the different rails will be gone over for each I/O device later in the workshop.

<div><h4>2. Jumoer Wires</h4></div>

<div align=center>Female to Male:</div>

<div class=mdImage align=center>
    <img src="./io_workshop_images/2_female_male.png" width="400" height="auto" />
</div>
<div align=center><i>In the image you can see one side of the wire is used to plug <ins>into another device</ins>, while the opposite side is used to plug <ins>other devices into it</ins>.</i></div>
<br>

<div align=center>Female to Female:</div>

<div class=mdImage align=center>
    <img src="./io_workshop_images/3_female_female.png" width="400" height="auto" />
</div>
<div align=center><i>Both ends of the wire are used to plug <ins>other devices into it</ins>.</i></div>
<br>

<div align=center>Male to Male:</div>

<div class=mdImage align=center>
    <img src="./io_workshop_images/4_male_male.png" width="400" height="auto" />
</div>
<div align=center><i>Both ends of the wire are used to plug <ins>into other devices</ins>.</i></div>

<div><h4>3. The GPIO Pins</h4></div>

<div class=mdImage align=center>
    <img src="./io_workshop_images/5_gpio.png" width="400" height="auto" />
</div>

Now you have heard a little bit about GPIO pins earlier in the semester. GPIO is short for "General Purpose Input/Output". An important thing to note right off the bat is that not all pins act the same . Some pins can provide a power *output* such as <ins>3v3 and 5v pins</ins>, others can receive and measure power *inputs* like <ins>"gnd" or ground pins</ins>. Over all though, a majority of the pins are used for reading inputs or providing outputs. 

How can we tell the difference between the pins? The GPIO Zero Python Library provides a comand line tool that is installed by default on your Raspberry Pi, so users can have a better understanding of their Pi. Open the terminal and enter in the prompt, `pinout`. You will see the following:

<div class=mdImage align=center>
    <img src="./io_workshop_images/6_pinout.png" width="400" height="auto" />
</div>

This provides a layout of each pin on your Raspberry Pi and they type of pin it is. You can also see it provides some information on where some of the physical components of your pi are for reference as well.

Now that we have a better idea about some of the compopnents we will be using to make our i/o devices functional, let's start using them.

Open VS Code on your Pi and in your *python-work* folder, create a folder named *workshop_3*. Inside the *workshop_3* folder, create a file named "button.py".

<div align=center><h2>Tactile Button</h2></div>

A tactile button can be used to give inputs to your Raspberry Pi by clicking the button while a program is running. This clasifies the tactile button as an **input** device. We will first code the button in Python, and then connect physically connect it to the Pi.

1. In button.py, we are first going to import the Button class fomr the "gpiozero" library and the pause function from the "signal" package. To do this, we will enter the following code at the top of button.py:<br>
`from gpiozero import Button ` <br>
`from signal import pause`

2. Next, we can create an instance of the button class by using the number of the GPIO pin used when setting up our tactile button. We are using the **GIPIO4** pin, so we will specify that in the code and set it equal to the variable `button” as so:<br>
`button = Button(4)`
> Specifying "4" is how Python knows which pin we will be using. 

3. Next we are going to define 3 methods for our button: `buttonPressed()”, “buttonHeld()”, and “buttonReleased()”. When these methods are used, each will print a statement regarding the action described in their name. Use the following in your file:
> Methods are simply functions that are specific to a certain class. The above methods would not be able to be used with any other class or data type.

        def buttonPressed():
        	print(“Button was pressed”)
        def buttonHeld():
        	print(“Button was held”)
        def buttonReleased():
        	print(“Button was released”)

4. The functions we have now defined will be used in conjunction with the three event **properties** of pressing, holding, and releasing the button. The Button class has: ".when_pressed", ".when_held", and ".when_released".The two properties that are  self explanatory and do not need much explaining are ".when_pressed" and ".when_released". On the other hand, ".when_held" can take in a specified time for the function to run. This is done by specifying “hold_time=[some_float]”, where some_float is a float data type, within the instantiation of our Button class.

`button = Button(4)` <br>
Will now be:<br>
`button = Button(4, hold_time = 3.0)` <br>
This will specify that for the buton_held function will wait 3 seconds before it executes its code.

5. Lastly, we need to use our “button” variable to call these functions. Use the following to do so:

        button.when_pressed = buttonPressed
        button.when_held = buttonHeld
        Button.when_released = buttonReleased`

now when the tactile button is pressed, the method "buttonPressed" will run and print the statement, “Button was pressed”. If the button is helf for 3 seconds, then the "buttonHeld' method will run. WHat do you think will execute when this method is called? Lastly, when the tactile button is released, the "buttonReleased" method will be called.

6. Our complete file should now look like the following:

        from gpiozero import Button 
        from signal import pause

        button = Button(4, hold_time=3.0)

        def buttonPressed():
            print("Button was pressed.")
        def buttonHeld():
            print("Button was held.")
        def buttonReleased():
            print("Button was released")


        button.when_pressed = buttonPressed
        button.when_held = buttonHeld
        button.when_released = buttonReleased

        pause()

> pause() is used to stop your program from running after the button has been released. We will use "control + c" to quit the program after having finished testing.