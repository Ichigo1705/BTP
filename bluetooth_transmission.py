import bluetooth
import math
import serial
import time

default = [1, 10]

reference = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e'}

def simulate_car(X):
    ser = serial.Serial("COM6", 9600, timeout=1)
    for i in range(len(X)):
        a = X[i]
        print(a)
        if(a[0] == 1 or a[0] == 2 or a[0] == 5):
            j = 0
            while(j<140):
                data = ''.join(str(x) for x in a)
                print(data)
                ser.write(bytearray(data, 'ascii'))
                j += 1
        elif(a[0] == 3 or a[0] == 4):
            x = a[1]*(math.pi)*2500/(180*0.5)
            j = 0
            while(j <= x):
                data = a[0]
                print(data)
                ser.write(bytearray(str(data), 'ascii'))
                j += 1
            j = 0
            while(j<140):
                data = ''.join(str(x) for x in default)
                print(data)
                ser.write(bytearray(str(data), 'ascii'))
                j += 1
        else:
            exit()
    ser.close()

def simulate_car_2(X):
    ser = serial.Serial("COM6", 9600, timeout=1)
    for i in range(len(X)):
        a = X[i]
        print(a)
        if(a[0] == 1 or a[0] == 2 or a[0] == 5):
            data = ''.join(str(x) for x in a)
            data = list(data)
            data[0] = reference[data[0]]
            data = "".join(data)
            print(data)
            ser.write(bytearray(data, 'ascii'))
            time.sleep(4)
        elif(a[0] == 3 or a[0] == 4):
            x = a[1]*(math.pi)*2500/(180*0.5)
            data = ''.join(str(x) for x in a)
            data = list(data)
            data[0] = reference[data[0]]
            data = "".join(data)
            print(data)
            ser.write(bytearray(str(data), 'ascii'))
            time.sleep(4)
            data = ''.join(str(x) for x in default)
            data = list(data)
            data[0] = reference[data[0]]
            data = "".join(data)
            print(data)
            ser.write(bytearray(str(data), 'ascii'))
            time.sleep(4)
        else:
            exit()
    ser.close()