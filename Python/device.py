
# IMPORTANT
# TODO: define class to allow several devices in same computer
# TODO: add error checking if port can't be opened

import serial
import time

devicePort = serial.Serial()
devicePort.baudrate = 9600

def getPortList():

    import serial.tools.list_ports

    return [comport.device for comport in serial.tools.list_ports.comports()]

def detect():

    device_port = ""

    ser = serial.Serial(timeout = 5)
    ser.baudrate = 9600


    port_list = getPortList()

    # if no ports available
    if (len(port_list) == 0):
        return "none"

    for p in port_list:

        ser.port = p

        ser.open()
        time.sleep(2) # wait requiered while port opens


        ser.write(b'$PING')
        line = ser.readline().decode("utf-8")
    
        if (line == "PONG:0\n"):
            device_port = ser.port
        else:
            device_port = "none"

        ser.close()

    devicePort.port = device_port

    return device_port

def Write(msg):

    if (not devicePort.is_open):
        devicePort.open()
        time.sleep(2)

    devicePort.write(bytes(msg, 'utf-8'))


def Read():

    if (not devicePort.is_open):
        devicePort.open()
        time.sleep(2)

    line = devicePort.readline().decode("utf-8")

    return line;

def Close():
    devicePort.close()

def Open():
    devicePort.open()

def Start():
    Write("$START:")

def Stop():
    Write("$STOP:")

