import serial
import time

ser = serial.Serial("COM6", 9600, timeout=1)

l = ["Hello World", "Fuck u", "BTP ki maa ki", "MKS paise nikal"]

for x in l:
    #res = struct.pack('10s', bytes(chr(i), 'utf-8'))
    ser.write(bytearray(x, 'ascii'))
    #time.sleep(2)

ser.close()
