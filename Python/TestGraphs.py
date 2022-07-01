import matplotlib.pyplot as plt
import numpy
import serial
from drawnow import *
import device

tempCH1 = []
tempCH2 = []
tempCH3 = []
tempCH4 = []
arduinoData = serial.Serial('COM6',9600)
plt.ion()
cnt = 0

def figurePlot():
    plt.style.use('ggplot')
    plt.ylim(300,700)
    plt.ylabel('V')
    plt.plot(tempCH1, 'ro-', label = 'Voltage')
    plt.legend(loc='upper left')
    plt2 = plt.twinx()
    plt.ylim(100,200)
    plt2.set_ylabel('uA')
    plt2.plot(tempCH2, 'b-', label = 'Current')
    plt2.legend(loc='upper right')

while True:
    while (arduinoData.inWaiting() == 0):
        pass   # no hacer nada
    arduinoString = arduinoData.readline()
    dataString = str(arduinoString,'utf-8')
    dataArray = dataString.split(",")

    ch1 = float(dataArray[0])
    ch2 = float(dataArray[1])
    ch3 = float(dataArray[1])
    ch4 = float(dataArray[3])

    tempCH1.append(ch1)
    tempCH2.append(ch2)
    tempCH3.append(ch3)
    tempCH4.append(ch4)

    drawnow(figurePlot)
    cnt = cnt + 1
    if (cnt > 30):
        tempCH1.pop(0)
        tempCH2.pop(0)
        tempCH3.pop(0)
        tempCH4.pop(0)
