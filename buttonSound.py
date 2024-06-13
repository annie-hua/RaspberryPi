from pygame import mixer 
import RPi.GPIO as GPIO
from languageSoundMap import languageSoundMap

class ButtonSound:
    def __init__(self):
        self.redButton = 22 #GPIO 25 
        self.yellowButton = 18 #GPIO 24
        self.blueButton = 16 #GPIO 23
        self.greenButton = 32 #GPIO 12
        self.orangeButton = 36 #GPIO 16
        self.language = 'English'

    def setup(self):
        mixer.init()
        GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
        GPIO.setup(self.redButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
        GPIO.setup(self.yellowButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
        GPIO.setup(self.blueButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
        GPIO.setup(self.greenButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>
        GPIO.setup(self.orangeButton, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT>

    def playSound(self, sound):
        mixer.music.load(sound)
        mixer.music.play()

    def playSoundButton(self):
        while True:
            if GPIO.input(self.redButton)==GPIO.LOW: # if button is pressed
                print ('Red Button: button pressed >>>')
                self.playSound(languageSoundMap[self.language]['red'])
            if GPIO.input(self.yellowButton)==GPIO.LOW: # if button is pressed
                print ('Yellow Button: pressed >>>')
                self.playSound(languageSoundMap[self.language]['yellow'])
            if GPIO.input(self.blueButton)==GPIO.LOW: # if button is pressed
                print ('Blue Button: pressed >>>')
                self.playSound(languageSoundMap[self.language]['blue'])
            if GPIO.input(self.greenButton)==GPIO.LOW: # if button is pressed
                print ('Green Button: pressed >>>')
                self.playSound(languageSoundMap[self.language]['green'])
            if GPIO.input(self.orangeButton)==GPIO.LOW: # if button is pressed
                print ('Orange Button: pressed >>>')
                self.playSound(languageSoundMap[self.language]['orange'])
        
    def setLanguage(self, language):
        self.language = language

    def destroy(self):
        GPIO.cleanup() # Release GPIO resource