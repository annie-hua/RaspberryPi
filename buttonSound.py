from pygame import mixer 
import RPi.GPIO as GPIO
from languageSoundMap import languageSoundMap

redButton = 22 
yellowButton = 18 
blueButton = 16
greenButton = 32 #GPIO 12
orangeButton = 36 #GPIO 16

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
            print ('Red Button: button pressed >>>')
            playSound(languageSoundMap[language]['red'])
        if GPIO.input(yellowButton)==GPIO.LOW: # if button is pressed
            print ('Yellow Button: pressed >>>')
            playSound(languageSoundMap[language]['yellow'])
        if GPIO.input(blueButton)==GPIO.LOW: # if button is pressed
            print ('Blue Button: pressed >>>')
            playSound(languageSoundMap[language]['blue'])
        if GPIO.input(greenButton)==GPIO.LOW: # if button is pressed
            print ('Green Button: pressed >>>')
            playSound(languageSoundMap[language]['green'])
        if GPIO.input(orangeButton)==GPIO.LOW: # if button is pressed
            print ('Orange Button: pressed >>>')
            playSound(languageSoundMap[language]['orange'])
    

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