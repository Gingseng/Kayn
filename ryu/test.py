import os
import serial
from conf import *





serialObj = serial.Serial ()
port= porta("port")
baudrate = baud("baudrate")
time = timeout("timing")
print(port)
print(baudrate)
print(time)