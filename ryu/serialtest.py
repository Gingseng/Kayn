
import os
from datetime import *
import serial
import configparser
import time
#leitura e declaração de arquivos

cfgini = configparser.ConfigParser()
cfgini.read('config.ini')

serialObj = serial.Serial(
    port = cfgini.get('Setup', 'Porta'),
    baudrate = cfgini.getint('Setup','Brate'),
    bytesize = cfgini.getint('Setup','Bytesize'),
    parity = cfgini.get('Setup','Parity'),
    stopbits = cfgini.getint('Setup', 'Stop-bits'))
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




def writereading(x):
    serialObj.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    dates = (str(serialObj.readline()))
    return dates

while True:
    value = writereading("x") 
    print(("entry:"),value) 
    if (value != ("b''")):
        

#aqui irá ocorrer o salvamento das variaveis em um arquivo log
        loglead = dataehora.strftime("%d-%m")
        logleadp = loglead+'.log'
        file = open(logleadp,"a")
#17/11/2022 10:03, Baudrate: 9600, Port: COM5, ByteSize: 8,Parity: N,StopBits: 1
        
        file.writelines(stringer)
        file.writelines("Setup de porta serial: ")
        file.write("Port: ")
        file.write ( porta1 )
        file.write (" ,")
        file.write("Valor de leitura:")
        file.write(value)
        file.write (" ,")
        file.write ("saving sucess")
        file.write("\n")
    else:
        os.system ("cls")
#ATUALIZADO 10/11/2022 - João Santos 
