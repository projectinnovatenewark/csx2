<div align=center><h1>The Fam Cam Motion Detection Device</h1></div>

In this workshop, the student will learn:
- How to wire and use more peripheral devices
- How to use functions aacross multiple files to build a project
- How to use the Python SMTP Library to send text message notifications

Here is the list of external parts you need besides your Raspberry Pi Desktop that came with your package:

<!-- FIXME: Insert List -->

<!-- FIXME: Create gmail -->

<!-- FIXME: Insert Steps to build Project -->

<div align=center><h2>Coding the Fam Cam</h2></div>

In this section, we will be creating the program that runs the Fam Cam. Although we will be using new peripherals such as the buzzer and motion sensor, using Python to code them will feel familiar as it is a similar process as the peripherals in workshop 3.

1. In your *python-work* folder, create a new folder called *project-1*. In *project-1*, create a file named "fam_cam.py".

2. First we need to import the `datetime` module. This is a Python module used for it's ability to create time stamps. Since we will eventually be using a notification system, it's a good idea to know when someone sets off the motion detector.

        from datetime import datetime 

3. Now we can import the three classes we will need from the gpiozero library; Buzzer, LED, and MotionSensor. When the motion sensor is set off, the LED light and buzzer will be triggered as well. We will also import the pause function from the signal module just as we did in workshop 3.

        from gpiozero import Buzzer, LED, MotionSensor
        from signal import pause

4. Let's instantiate each peripheral class with its respective GPIO pin. Remember we used **GPIO4** for the buzzer, **GPIO14** for the LED light, and **GPIO18** for the motion sensor.

        buzzer = Buzzer(4)
        led = LED(14)
        motion_sensor = MotionSensor(18)

5. We shoudld also store the timestamp in a variable so it is easy to use in the rest of our program. We can do so with the following:

        detection = datetime.now() # .now() is a function of the datetime class that creates the timestamp

6. Next, we want to create two functions, one that runs when motion is detected, and another that runs afterwards.
    - The first function we create will be `start_motion()`. This will be called when the motion sensor goes off. In this function, we will call the LED light to blink every 0.5 seconds, turn on the buzzer to beep every 0.5 seconds, and print the time the motion sensor is triggered as an output to the terminal.
    - Second, we need a function `end_motion()` that will stop the led light and buzzer from going off. Creating this function will eliminate the need to constantly restart your program and instead continue running.
        def start_motion():
            led.blink(0.5, 0.5)
            buzzer.beep(0.5, 0.5) # This is a method of the Buzzer class. (Watch out its pretty loud!)
            print(f"Motion detected at {detection}")

        def end_motion():
            if(detection): # "If detection has a value, then we want to turn off the led and buzzer"
                led.off() # Method to turn off the LED light
                buzzer.off() # Method to turn off the buzzer

6. Lastly for this file, we want to print to the terminal when we are starting up the motion sensor and when the sensor is ready. Of course we will also need to store the custom functions as the respective motion sensor methods.

To do so, we will use three methods from the MotionSensor class. The first being "wait_for_no_motion()". This method prevents the motion sensor from going off immediately on startup. The second method is ".when_motion()", which is what is triggered when the motion sensor detects any motion. Lastly, ".when_no_motion()" is used when the motion sensor is no longer detecting motion.

        print("Starting up the sensor...")
        motion_sensor.wait_for_no_motion()
        print("Sensor ready")
        motion_sensor.when_motion = start_motion
        motion_sensor.when_no_motion = end_motion

        pause()

