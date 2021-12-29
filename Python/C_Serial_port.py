
import serial
import time


import serial.tools.list_ports

port_list = [comport.device for comport in serial.tools.list_ports.comports()]

device_port = ""

ser = serial.Serial(timeout = 5)
ser.baudrate = 9600

for p in port_list:

    ser.port = p

    ser.open()
    time.sleep(2) # wait requiered while port opens


    ser.write(b'PING')
    line = ser.readline().decode("utf-8")
    
    if (line == "PONG:0\n"):
        device_port = ser.port

    ser.close()

print(device_port)