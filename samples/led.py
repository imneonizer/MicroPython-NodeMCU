import machine
import time

class LedBlink:
    def __init__(self, pin=2):
        self.pin = machine.Pin(pin, machine.Pin.OUT)

    def loop(self, test=False):
        while True:
            # there is a bug in nodemcu
            # due to which pin.on() actually works opposite
            print("led value => off")
            self.pin.on()
            time.sleep(0.5)

            print("led value => on")
            self.pin.off()
            time.sleep(0.5)
            

            if test:
                # turn off the led
                # and exit program
                self.pin.on()

                break

print("Begin Led toogle program")
LedBlink().loop()