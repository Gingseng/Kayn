import serial
import time
import os
from datetime import datetime



serialObj = serial.Serial (port='COM4', baudrate=9600,timeout =.1)

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
serialObj.port = input ("insira a porta: \n")
time.sleep (1)

serialObj.bytesize = 8
print ("DEFAULT BYTESIZE SET   ->",str(serialObj.bytesize), ("\n"))
time.sleep (1)

serialObj.parity = input ("inserir paridade \n (N,E,O,S): \n")
time.sleep (1)

serialObj.stopbits = 1
print ("DEFAULT STOP BITS SETED -> ", str(serialObj.stopbits), ("\n"))
time.sleep (1)
os.system ("cls")

baudrate = serialObj.baudrate
porta = serialObj.port
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
file.write("---------usuario logs---------- \n")
file.write("VALOR LIDO: ")
file.write ("\n")
file.write("Date/Time: ")
file.write(stringer)
file.write ("\n")
file.write("Baudrate        =")
file.write ( str (baudrate) )
file.write ("\n")
file.write("Port            =")
file.write ( porta )
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
    serialObj.write(bytes(x, 'UTF-8'))
    time.sleep(5)
    dates = serialObj.readline()
    return dates

while True:
    valor = input ("aperte qualquer tecla...")
    value = writereading(valor)
    print(value)
    break
file = open("logs.txt","a")
file.write("Valor de leitura        =")
file.write(str(value))
file.write ("\n")
file.write("------------------------------- \n")
file.close()
#ATUALIZADO 10/11/2022 - João Santos 