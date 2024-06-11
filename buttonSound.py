import RPi.GPIO as GPIO

redButton = 19 
yellowButton = 18 
blueButton = 17


def setup():
    GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT) # set ledPin to OUTPUT mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>

def loop():
    while True:
        if GPIO.input(redButton)==GPIO.LOW: # if button is pressed
                print ('led turned on >>>') # print information on terminal
    else : # if button is released
        GPIO.output(ledPin,GPIO.LOW) # turn off led
        print ('led turned off <<<')
def hello():
    print('Hello')

def destroy():
    GPIO.output(ledPin, GPIO.LOW)     # turn off led 
    GPIO.cleanup()                    # Release GPIO resource

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()