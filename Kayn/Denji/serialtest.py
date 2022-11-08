import serial
import time
import os

serialObj = serial.Serial (port='COM4', baudrate=9600, timeout=.1)

os.system("color 0a")
os.system("cls")

print('\ndefault settings')
print ('Port            =', serialObj.port)
print ('Baudrate        =', serialObj.baudrate)
print ('ByteSize        =', serialObj.bytesize)
print ('Parity          =', serialObj.parity)
print ('StopBits        =', serialObj.stopbits)



serialObj.bytesize = 8
serialObj.parity = 'N'
serialObj.stopbits =1



time.sleep(2)

print('\nchanged settings')
print ('Port            =', serialObj.port)
print ('Baudrate        =', serialObj.baudrate)
print ('ByteSize        =', serialObj.bytesize)
print ('Parity          =', serialObj.parity)
print ('StopBits        =', serialObj.stopbits)

def writereading(x):
    serialObj.write(bytes(x, 'ascii'))
    time.sleep(0.05)
    dates = serialObj.readline()
    return dates

while True:
    valor = input ("aperte qualquer tecla...")
    value = writereading(valor)
    print(value)
