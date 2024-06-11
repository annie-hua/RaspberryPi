from pygame import mixer 
import RPi.GPIO as GPIO

redButton = 22 
yellowButton = 18 
blueButton = 16


def setup():
    mixer.init()
    GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
    # GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
    GPIO.setup(redButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
    GPIO.setup(yellowButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
    GPIO.setup(blueButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>

# def setLanguage():
#     redSound = '/sounds/English/red.m4a'

def loop():
    while True:
        if GPIO.input(redButton)==GPIO.LOW: # if button is pressed
            print ('Red Button: button pressed >>>') # print information on terminal
            mixer.music.load('./sounds/English/red.m4a')
            mixer.music.play()
        if GPIO.input(yellowButton)==GPIO.LOW: # if button is pressed
            print ('Yellow Button: pressed >>>') # print information on terminal
        if GPIO.input(blueButton)==GPIO.LOW: # if button is pressed
            print ('Blue Button: pressed >>>') # print information on terminal
    # else : # if button is released
    #     print ('button released <<<')
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