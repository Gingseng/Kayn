import serial
import time

serialObj = serial.Serial ('COM6')

print('\ndefault settings')
print ('Port            =', serialObj.port)
print ('Baudrate        =', serialObj.baudrate)
print ('ByteSize        =', serialObj.bytesize)
print ('Parity          =', serialObj.parity)
print ('StopBits        =', serialObj.stopbits)


serialObj.baudrate = 9600
serialObj.bytesize = 8
serialObj.parity = 'N'
serialObj.stopbits =1

time.sleep(3)

print('\nchanged settings')
print ('Port            =', serialObj.port)
print ('Baudrate        =', serialObj.baudrate)
print ('ByteSize        =', serialObj.bytesize)
print ('Parity          =', serialObj.parity)
print ('StopBits        =', serialObj.stopbits)

Receivedstring = serialObj.readline()
print (Receivedstring)

serialObj.close()