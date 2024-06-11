import RPi.GPIO as GPIO

redButton = 22 
yellowButton = 18 
blueButton = 16


def setup():
    GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
    # GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
    GPIO.setup(redButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
    GPIO.setup(yellowButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
    GPIO.setup(blueButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>


def loop():
    while True:
        print('looping')
        if GPIO.input(redButton)==GPIO.LOW: # if button is pressed
            print ('button pressed >>>') # print information on terminal
        if GPIO.input(yellowButton)==GPIO.LOW: # if button is pressed
            print ('button pressed >>>') # print information on terminal
        if GPIO.input(blueButton)==GPIO.LOW: # if button is pressed
            print ('button pressed >>>') # print information on terminal
    else : # if button is released
        print ('button released <<<')
def hello():
    print('Hello')

def destroy():
    # GPIO.output(ledPin, GPIO.LOW)     # turn off led 
    GPIO.cleanup()                    # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()