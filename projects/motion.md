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

Here is a complete version of fam_cam.py just incase there were any hiccups along the way!

        from datetime import datetime
        from gpiozero import Buzzer, LED, MotionSensor
        from signal import pause

        buzzer = Buzzer(4)
        led = LED(14)
        motion_sensor = MotionSensor(18)

        detection = datetime.now() # .now() is a function of the datetime class that creates the timestamp

        def start_motion():
            led.blink(0.5, 0.5)
            buzzer.beep(0.5, 0.5) # This is a method of the Buzzer class. (Watch out its pretty loud!)
            print(f"Motion detected at {detection}")

        def end_motion():
            if(detection): # "If detection has a value, then we want to turn off the led and buzzer"
                led.off() # Method to turn off the LED light
                buzzer.off() # Method to turn off the buzzer

        print("Starting up the sensor...")
        motion_sensor.wait_for_no_motion()
        print("Sensor ready")
        motion_sensor.when_motion = start_motion
        motion_sensor.when_no_motion = end_motion

        pause()

We now have a working file. Test it out by executing the file and waving in front of the sensor. You should see an output in the terminal as well as the light and buzzer going off. In the next section, you will learn how to use an SMTP server and your newly created gmail account to send a notification any time the sensor is triggered.

<div align=center><h2>SMS Alert System</h2></div>

In this section, we will code out the Fam Cam's text message notification system. The cool thing about SMTP is that even though it is an email server, it can send text messages by using SMS gateways. An sms gateway service is what allows a computer to send emails as texts by using a given phone number and carrier specific gateway. If you wanted to send a text to a Verizon number it would like: “1234567890@vtext.com”. We can then utilize the “MIME” module to structure our message. The new Gmail account you created will be used to send this message. If you still need to create the new account, <a href="https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp">click here.</a>
> Don't forget to go allow third party app access or else the message won't send!

**Note:** Text messaging rates might apply, so keep that in mind. If that is an issue, let your teacher know.

1. In your *project-1* folder, create a new file "text_me.py". This is where we will code the SMTP server.

2. At the beginning of this file, we want to import "smtplib", "MIMEText", and "MIMEMultipart".
        
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

3. Next, define a custom function named. "texter()". In it, we will have to provide authentication so the email service can function. For this, we will set two variables; "email" and "password" to store our new email and password to that email as a string. Below is our function so far:

        def texter():
            email = "your.email.here@gmail.com"
            password = "INSERT PASSWORD FOR ABOVE EMAIL"

4. Next we need to store the SMS Gateway address to send the notification to. This can be different depending on your cell phone provider. A list of some major providers and their gateway service addresses can be found <a href="https://dev.to/mraza007/sending-sms-using-python-jkd">here</a>. We will store this in a variable "sms_gateway" and our function now currently looks like the below: 

        def texter():
            email = "your.email.here@gmail.com"
            password = "INSERT PASSWORD FOR ABOVE EMAIL"

            sms_gateway = "PHONE_NUMBER@CARRIER_GATEWAY"

5. Lastly for variables, we need to specify the server and port that it will run on. We will be using the default smtp server and default port. Using these will establish a secure TLS connection. Once the connection is established, we use that to login to the created email and password from earlier.

> TlS is short for "Transport Layer Security" and is the latest security protocol used for ecrypting data and information while its trasferred through the internet.

The "texter()" function now looks like the below:

        def texter():
            email = "your.email.here@gmail.com"
            password = "INSERT PASSWORD FOR ABOVE EMAIL"

            sms_gateway = "PHONE_NUMBER@CARRIER_GATEWAY"

            smtp = "smtp.gmail.com"
            port = 587

            # This starts the email server
            server = smtplib.SMTP(smtp,port)

            server.starttls()

            server.login(email,password)

6. It's time to create the message. First we store the "MIMEMultipart()" function in the variable "msg". We then define the 'From' and 'To' which will be the new email created and the sms gateway variable we defined earlier reapectively. We can set the 'Subject' as well to be "Fam Cam Alert".

After doing so, we will store the body of our message in a variable called "body". We will want to pass the timestamp from earlier into the body of the message as well. We can do this by setting a parameter in the "texter()" function and using f shorthand to pass it to the body. The "texter()" function will now look like the below:

        def texter(timestamp):
            email = "your.email.here@gmail.com"
            password = "INSERT PASSWORD FOR ABOVE EMAIL"

            sms_gateway = "PHONE_NUMBER@CARRIER_GATEWAY"

            smtp = "smtp.gmail.com"
            port = 587

            # This starts the email server
            server = smtplib.SMTP(smtp,port)

            server.starttls()

            server.login(email,password)

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = sms_gateway

            msg['Subject'] = "Fam Cam Alert!\n" # "/n" is used to indicate a new line should be used for the next output
            body = f"Motion has been detected at {timaestamp}!\n"

7. Lastly, we want to attach the body to the message as plaintext using ".attach()" and use the ".as_string()" function to assure the message is read as a string. This will be stored in the variable "sms". Then we send the text and quit out of the server. The complete function now looks like the below:

        def texter(timestamp):
            email = "your.email.here@gmail.com"
            password = "INSERT PASSWORD FOR ABOVE EMAIL"

            sms_gateway = "PHONE_NUMBER@CARRIER_GATEWAY"

            smtp = "smtp.gmail.com"
            port = 587

            # This starts the email server
            server = smtplib.SMTP(smtp,port)

            server.starttls()

            server.login(email,password)

            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = sms_gateway

            msg['Subject'] = "Fam Cam Alert!\n" # "/n" is used to indicate a new line should be used for the next output
            body = f"Motion has been detected at {timaestamp}!\n"

            msg.attach(MIMEText(body, 'plain'))

            sms = msg.as_string()

            server.sendmail(email,sms_gateway,sms)

            server.quit()

8. To use our newly created function, 

**Note:** A common error is failed authentication, meaning one of two things:
1. You could have mistyped your email or password in the "text_me()" function. Re-check that first.
2. If the error persists after option 1, third party app access might not be set to allow access. Please re-check step <!-- FIXME: add step # --> 

Great! You should have a working motion detection and notification system. Let's recap on how we did it.

Takeaways:
- Learned how to configure two new peripherals, the buzzer and motion sensor
- Imported and implmented