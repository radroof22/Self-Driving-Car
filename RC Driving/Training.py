import RPi.GPIO as GPIO
import camera as Cam

GPIO_Dir = {
    "F": 12,
    "R": 21,
    "L": 16,
    "R": 20
    }

def reset():
    for dire in GPIO_Dir:
        GPIO.output(GPIO_Dir[dire], False)

def setup():
    GPIO.setmode(GPIO.BCM)
    for dire in GPIO_Dir:
        GPIO.setup(GPIO_Dir[dire], GPIO.OUT)

def main():

    setup()
    
    iteration = 0
    while True:
        action = input("> ")
        # Loop through control options
        if action == 'w':
            # Forward
            GPIO.output(GPIO_Dir["F"], True)
        elif action == 'a':
            # Left
            GPIO.output(GPIO_Dir["L"], True)
        elif action == 'd':
            # Right
            GPIO.output(GPIO_Dir["R"], True)
        elif action == 's':
            # Reverse
            GPIO.output(GPIO_Dir["R"], True)
        elif action == " ":
            # Stop
            reset()
        elif action == "e":
            # End
            reset()
            GPIO.cleanup()
            import sys
            sys.quit()
        
        Cam.take_picture(action, iteration)
        iteration += 1
        
