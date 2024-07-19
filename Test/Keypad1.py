# This Raspberry Pi code is made available for public use without any restriction
# For comprehensive instructions and wiring diagrams, please visit:
# https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-keypad

from pygame import mixer 

import RPi.GPIO as GPIO
import time
from languageSoundMap import languageSoundMapButtons14

class ButtonSound:
    def __init__(self):
#   Define keypad layout
        self.KEYPAD = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        # Define GPIO pins for rows and columns

        self.COLS = [4, 17, 27, 22]
        self.ROWS = [5, 6, 13, 19]

        # Initialize GPIO
        GPIO.setmode(GPIO.BCM)

        # Set up row pins as inputs with pull-up resistors
        for row_pin in self.ROWS:
            GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Set up column pins as outputs
        for col_pin in self.COLS:
            GPIO.setup(col_pin, GPIO.OUT)
            GPIO.output(col_pin, GPIO.HIGH)
        
        self.level = 1
        self.language = 'English'




    def get_key(self):
        key = None

        # Scan each column
        for col_num, col_pin in enumerate(self.COLS):
            GPIO.output(col_pin, GPIO.LOW)

            # Check each row
            for row_num, row_pin in enumerate(self.ROWS):
                if GPIO.input(row_pin) == GPIO.LOW:
                    key = self.KEYPAD[row_num][col_num]

                    # Wait for key release
                    while GPIO.input(row_pin) == GPIO.LOW:
                        time.sleep(0.05)

            GPIO.output(col_pin, GPIO.HIGH)

        return key
    
    def playSound(self, sound):        
        mixer.music.load(sound)
        mixer.music.play()
    
    def getSound(self, keyPressed):

        if self.level == 1:
            return languageSoundMapButtons14[self.language]['level_1'][keyPressed]
        else:
            return languageSoundMapButtons14[self.language]['level_2'][keyPressed]
        
    def loop(self):
        try:
            while True:
                pressed_key = self.get_key()

                if pressed_key is not None:
                    if pressed_key == 14:
                        if self.level == 1:
                            self.level = 2
                        else:
                            self.level = 1
                    self.getSound(pressed_key)
                    print(f"Pressed: {pressed_key}")
                time.sleep(0.1)

        except KeyboardInterrupt:
            GPIO.cleanup()