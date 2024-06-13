import multiprocessing
import queue
import time

import dbus

from demo.ble_process import BLEProcess
from buttonSound import ButtonSound

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    buttonSound = ButtonSound()
    buttonSound.setup()
    output_queue = multiprocessing.Queue()
    ble_process = BLEProcess(output_queue)
    ble_process.start()
    try:
        buttonSound.loop()
        while True:
            try:
                curr_value = output_queue.get(timeout=1)
                print(f"Value written to Characteristic with UUID {curr_value['uuid']}: {curr_value['value']}")
                newLangage = curr_value['value']
                if curr_value:
                    buttonSound.setLanguage(newLangage)
            except queue.Empty:
                time.sleep(1)
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        buttonSound.destroy()   

    