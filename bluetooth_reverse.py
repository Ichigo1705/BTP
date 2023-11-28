import serial
import time

ser = serial.Serial("COM6", 9600, timeout=1)
reference = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}
#l = [['c', 180], ['d', 90], ['d', 360], ['c', 360], ['e']]
#l = "a80b80c30d60a100b60a120a50c30d30b100ee"
#delay = -1

def program(l):
 for x in range(len(l)):
    #res = struct.pack('10s', bytes(chr(i), 'utf-8'))
    a = l[x]
    a[0] = reference[a[0]]
    print(a)
    if(a[0] == 'a' or a[0] == 'b' or a[0] == 'e'):
        data = ''.join(str(x) for x in a)
        ser.write(bytearray(data, 'ascii'))
        p = 'f'
        ser.write(bytearray(str(p), 'ascii'))
        time.sleep(4)
    elif(a[0] == 'c' or a[0] == 'd'):
        data = ''.join(str(x) for x in a)
        delay = (3.158/180)*a[1]
        ser.write(bytearray(data, 'ascii'))
        p = 'f'
        ser.write(bytearray(str(p), 'ascii'))
        time.sleep(delay)
 #ser.close()
    #ser.write(bytearray(l[x], 'ascii'))
    #print(l[x])
    #if(pos == '')
    #time.sleep(1.5)

    #time.sleep(2)

#program(l)