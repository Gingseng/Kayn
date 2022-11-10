import os
import time
from datetime import datetime
from conf import *

import serial
arquivo = open('conf.txt', 'r')
linha = arquivo.readline()


serialObj = serial.Serial(port = porta("ports"))
baudrate = baud("baudrate")
timeout = timeouta(str("timing"))
bytesize = bytesiz("bytez")
stopbits = stopb ("stopbit")

os.system("color 0a")
os.system("cls")

print('\ndefault settings')
print ('Port            =', serialObj.port)
print ('Baudrate        =', serialObj.baudrate)
print ('ByteSize        =', serialObj.bytesize)
print ('Parity          =', serialObj.parity)
print ('StopBits        =', serialObj.stopbits)

#inserts do usuario
dataehora = datetime.now()
stringer = dataehora.strftime("%d/%m/%Y %H:%M")



print ("\n <<<<\\-----------------test de campo------------------//>>>>\n")
print (stringer, "\n")
print ("Lendo porta... \n")
time.sleep (3)
print ("Designed port set     ->",serialObj.port, ("\n"))
time.sleep (2)
print ("DEFAULT BYTESIZE SET   ->",str(serialObj.bytesize), ("\n"))
time.sleep (2)
print ("Default parity:", serialObj.parity, ("\n"))
time.sleep (2)


serialObj.stopbits = 1
print ("DEFAULT STOP BITS SETED -> ", str(serialObj.stopbits), ("\n"))
time.sleep (2)
os.system ("cls")

baudrate = serialObj.baudrate
porta1 = serialObj.port
bytesz = serialObj.bytesize
paridade = serialObj.parity
stop = serialObj.stopbits








print('\nchanged settings')
print ('Port            =', serialObj.port)
print ('Baudrate        =', serialObj.baudrate)
print ('ByteSize        =', serialObj.bytesize)
print ('Parity          =', serialObj.parity)
print ('StopBits        =', serialObj.stopbits)
#---------------------------------------------------------------

#aqui irá ocorrer o salvamento das variaveis em um arquivo log

file = open("logs.txt","a")
file.write("---------logs---------- \n")
file.write("Date/Time: ")
file.write(stringer)
file.write ("\n")
file.write("Baudrate        =")
file.write ( str (baudrate) )
file.write ("\n")
file.write("Port            =")
file.write ( porta1 )
file.write ("\n")
file.write("ByteSize        =")
file.write(str(bytesz))
file.write ("\n")
file.write("Parity          =")
file.write (str(paridade) )
file.write ("\n")
file.write("StopBits        =")
file.write(str(stop))
file.write ("\n")
time.sleep(1)

def writereading(x):
    serialObj.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    dates = (str(serialObj.readline()))
    return dates

while True:
    value = writereading("x")
    print(("Data:"),value) 
    if (value != ("b''")):
        file = open("logs.txt","a")
        file.write("Valor de leitura        =")
        file.write ("\n")
        file.write (stringer)
        file.write ("\n")
        file.write(str(value))
        file.write ("\n")
        file.write("------------------------------- \n")
        file.close()
    else:
        os.system ("cls")
#ATUALIZADO 10/11/2022 - João Santos 