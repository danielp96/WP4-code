# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#Libraries

import serial, time
import serial.tools.list_ports as ListPorts
import sys
import glob

#Variables
jsontest = "{\"command\":0,\"channel\":0,\"payload\":48.756080}"
port = 'COM4'
baudrate = 115200
#Main Code

#Port detection with native libraries
def serial_ports():
""" Lists serial port names

 :raises EnvironmentError:
     On unsupported or unknown platforms
 :returns:
     A list of the serial ports available on the system
"""
if sys.platform.startswith('win'):
 ports = ['COM%s' % (i + 1) for i in range(256)]
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
 # this excludes your current terminal "/dev/tty"
 ports = glob.glob('/dev/tty[A-Za-z]*')
elif sys.platform.startswith('darwin'):
 ports = glob.glob('/dev/tty.*')
else:
 raise EnvironmentError('Unsupported platform')

result = []
for port in ports:
 try:
     s = serial.Serial(port)
     s.close()
     result.append(port)
 except (OSError, serial.SerialException):
     pass
return result

#Print automatic port detection
if __name__ == '__main__':
print(serial_ports())

###Port detection using Serial library
##Ports = ListPorts.comports()
###Stores the name of the device
##Portnames = []
##i = 0
###List all ports in the computer
##print("Available devices:\n")
##for port, desc, hwid in sorted(Ports):
##        Portnames.append("{}) {}: {} [{}]".format(i,port, desc, hwid))
##        print(Portnames[i])
##
##        i = i+1
###Show which ones are Arduinos
###Grab the first 6 letters of the desc variable above
###store them in memory space
###using and if find out if it is equal to the word 'Arduino'
###grab its port and initialize accordingly
##
###Initialize Serial communication with Arduino
##arduino = serial.Serial(port, baudrate)
##time.sleep(2)
##arduino.readline()
