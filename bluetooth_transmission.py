import bluetooth
import math

default = [1, 10]

def send_data(data):
    address = bluetooth.discover_devices()[0]
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect(address)
    socket.send(data)
    socket.close()

def simulate_car(X):
    for i in range(len(X)):
        a = X[i]
        print(a)
        if(a[0] == 1 or a[0] == 2 or a[0] == 5):
            j = 0
            while(j<24000):
                data = ''.join(str(x) for x in a)
                send_data(data)
                j += 1
        elif(a[0] == 3 or a[0] == 4):
            x = a[1]*(math.pi)*2500/(180*0.5)
            j = 0
            while(j <= x):
                data = a[0]
                send_data(str(data))
                j += 1
            j = 0
            while(j<24000):
                data = ''.join(str(x) for x in default)
                send_data(data)
                j += 1
        else:
            exit()