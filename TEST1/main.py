# main.py -- put your code here!

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
  led.value(not led.value())
  print("Test pass")
  sleep(0.1)