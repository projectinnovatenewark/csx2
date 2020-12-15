from datetime import datetime
from gpiozero import Buzzer, LED, MotionSensor
from signal import pause
from text_me import texter # new import statement

buzzer = Buzzer(4)
led = LED(14)
motion_sensor = MotionSensor(18)

def start_motion():
  detection = datetime.now() # .now() is a function of the datetime class that creates the timestamp
  led.blink(0.5, 0.5)
  buzzer.beep(0.5, 0.5) # This is a method of the Buzzer class. (Watch out its pretty loud!)
  print(f"Motion detected at {detection}")
  texter(detection) # calling the texter function and passing through detection

def end_motion():
  led.off() # Method to turn off the LED light
  buzzer.off() # Method to turn off the buzzer

print("Starting up the sensor...")
motion_sensor.wait_for_no_motion()
print("Sensor ready")
motion_sensor.when_motion = start_motion
motion_sensor.when_no_motion = end_motion

pause()