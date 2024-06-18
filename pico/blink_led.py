from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)
print('Blinking LED Example')

while True:
  led.value(not led.value())
  print('bo')
  sleep(0.5)
