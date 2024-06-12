from pygame import mixer 
import RPi.GPIO as GPIO
from languageSoundMap import languageSoundMap

redButton = 22 
yellowButton = 18 
blueButton = 16

language = 'English'

def setup():
    mixer.init()
    GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
    # GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
    GPIO.setup(redButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
    GPIO.setup(yellowButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
    GPIO.setup(blueButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>

def playSound(sound):
    mixer.music.load(sound)
    mixer.music.play()

def loop():
    while True:
        if GPIO.input(redButton)==GPIO.LOW: # if button is pressed
            print ('Red Button: button pressed >>>') # print information on terminal
            playSound(languageSoundMap.language['red'])
        if GPIO.input(yellowButton)==GPIO.LOW: # if button is pressed
            print ('Yellow Button: pressed >>>') # print information on terminal
            playSound(languageSoundMap.language['yellowButton'])
        if GPIO.input(blueButton)==GPIO.LOW: # if button is pressed
            print ('Blue Button: pressed >>>') # print information on terminal
            playSound(languageSoundMap.language['blueButton'])

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