# main.py

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
  print("led:", "on" if led.value() else "off")
  led.value(not led.value())
  sleep(0.5)