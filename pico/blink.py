<<<<<<< HEAD
from machine import Pin
from time import sleep

led = Pin('LED', Pin.OUT)
print('Blinking LED Example')

while True:
  led.value(not led.value())
  sleep(0.5)
=======
import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
	led_onboard.value(1)
	utime.sleep(1)
	led_onboard.value(0)
	utime.sleep(1)
>>>>>>> 1899d616e8ad7acba14c4ba92f9e852193411ed7
