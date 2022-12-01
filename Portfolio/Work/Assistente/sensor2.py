from ctypes.wintypes import PINT
from os import utime
from turtle import distance
import time

from numpy import PINF

trigger = PINF(7, PINT.OUT)
echo = PINF(11, PINT.IN)

def getDistancia():
    trigger.low()
    time.sleep(2)
    trigger.high()
    time.sleep(5)
    trigger.low()

    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance= (timepassed * 0.0343)/2
    return distance

if __name__ == '__main__':
    while True:
        distancia = getDistancia()
        print("A distância do objeto é: " + str(distancia))
        time.sleep(1)