import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

import datetime
import device

# temp list, replace with list of ports from pyserial
portList = device.getPortList()
dev = device.Device()
dev.detect()

root = Tk()

def oneSecondThing():
    print('{:%M:%S}'.format(datetime.datetime.now()))
    dev.getData()
    topFrame.after(1000, oneSecondThing)

def buttonStartFunction():

    current = ch1CurrentEntry.get()

    time = ch1TimeEntry.get()


    device.port = "COM6"
    variable = "$SET_ONE:1," + current + "," + time + ";"

    device.Write(variable)

    print(variable)



topFrame = Frame(root)
topFrame.after(1000, oneSecondThing)

# begin port connection frame
portFrame = LabelFrame(topFrame, text="Device Connection")

portMenuValue = StringVar()
portMenuValue.set(portList[0]) # default value

portMenu = OptionMenu(portFrame, portMenuValue, *portList)
portMenu.config(width=len(max(portList, key=len)))
portMenu.pack(side=LEFT)


def buttonRefreshPortFunction():
    portList = device.getPortList()

    portMenuValue.set('')
    portMenu['menu'].delete(0, 'end')

    for port in portList:
        portMenu['menu'].add_command(label=port, command=tk._setit(portMenuValue, port))

    portMenuValue.set(portList[0]) # default value


buttonRefreshPort = Button(portFrame, text="Refresh", command=buttonRefreshPortFunction)
buttonRefreshPort.pack(side=LEFT)

buttonDetectPort = Button(portFrame, text="Auto Detect")
buttonDetectPort.pack(side=LEFT)

buttonConnectPort = Button(portFrame, text="Connect")
buttonConnectPort.pack(side=LEFT)


portFrame.pack(side=LEFT)
#end port coneection frame

#begin control frame
controlFrame = LabelFrame(topFrame, text="Device Control")

buttonStart = Button(controlFrame, text="Start", command = buttonStartFunction)
buttonStart.pack(side=LEFT)

buttonStop = Button(controlFrame, text="Stop")
buttonStop.pack(side=LEFT)

controlFrame.pack(side=RIGHT)
#end control frame

topFrame.pack()


# TODO: create the 8 channels with loop

#begin channels frame
channelsFrame = LabelFrame(root, text="Channel Control")

#begin CH1
ch1Frame = Frame(channelsFrame)

ch1Label = Label(ch1Frame, text="CH1")
ch1Label.pack(side=LEFT)

ch1CurrentEntry = Entry(ch1Frame, width=6)
ch1CurrentEntry.pack(side=LEFT)

Label(ch1Frame, text="uA").pack(side=LEFT)

ch1TimeEntry = Entry(ch1Frame, width=6)
ch1TimeEntry.pack(side=LEFT)

Label(ch1Frame, text="min").pack(side=LEFT)

ch1EnableCheck = Checkbutton(ch1Frame, text="Enable", variable = IntVar())
ch1EnableCheck.pack(side=LEFT)

ch1Frame.pack()
#end CH1


#begin CH2
ch2Frame = Frame(channelsFrame)

ch2Label = Label(ch2Frame, text="CH2")
ch2Label.pack(side=LEFT)

ch2CurrentEntry = Entry(ch2Frame, width=6)
ch2CurrentEntry.pack(side=LEFT)

Label(ch2Frame, text="uA").pack(side=LEFT)

ch2TimeEntry = Entry(ch2Frame, width=6)
ch2TimeEntry.pack(side=LEFT)

Label(ch2Frame, text="min").pack(side=LEFT)

ch2EnableCheck = Checkbutton(ch2Frame, text="Enable", variable = IntVar())
ch2EnableCheck.pack(side=LEFT)

ch2Frame.pack()
#end CH2


#begin CH3
ch3Frame = Frame(channelsFrame)

ch3Label = Label(ch3Frame, text="CH3")
ch3Label.pack(side=LEFT)

ch3CurrentEntry = Entry(ch3Frame, width=6)
ch3CurrentEntry.pack(side=LEFT)

Label(ch3Frame, text="uA").pack(side=LEFT)

ch3TimeEntry = Entry(ch3Frame, width=6)
ch3TimeEntry.pack(side=LEFT)

Label(ch3Frame, text="min").pack(side=LEFT)

ch3EnableCheck = Checkbutton(ch3Frame, text="Enable", variable = IntVar())
ch3EnableCheck.pack(side=LEFT)

ch3Frame.pack()
#end CH3


#begin CH4
ch4Frame = Frame(channelsFrame)

ch4Label = Label(ch4Frame, text="CH4")
ch4Label.pack(side=LEFT)

ch4CurrentEntry = Entry(ch4Frame, width=6)
ch4CurrentEntry.pack(side=LEFT)

Label(ch4Frame, text="uA").pack(side=LEFT)

ch4TimeEntry = Entry(ch4Frame, width=6)
ch4TimeEntry.pack(side=LEFT)

Label(ch4Frame, text="min").pack(side=LEFT)

ch4EnableCheck = Checkbutton(ch4Frame, text="Enable", variable = IntVar())
ch4EnableCheck.pack(side=LEFT)

ch4Frame.pack()
#end CH4


#begin CH5
ch5Frame = Frame(channelsFrame)

ch5Label = Label(ch5Frame, text="CH5")
ch5Label.pack(side=LEFT)

ch5CurrentEntry = Entry(ch5Frame, width=6)
ch5CurrentEntry.pack(side=LEFT)

Label(ch5Frame, text="uA").pack(side=LEFT)

ch5TimeEntry = Entry(ch5Frame, width=6)
ch5TimeEntry.pack(side=LEFT)

Label(ch5Frame, text="min").pack(side=LEFT)

ch5EnableCheck = Checkbutton(ch5Frame, text="Enable", variable = IntVar())
ch5EnableCheck.pack(side=LEFT)

ch5Frame.pack()
#end CH5


#begin CH6
ch6Frame = Frame(channelsFrame)

ch6Label = Label(ch6Frame, text="CH6")
ch6Label.pack(side=LEFT)

ch6CurrentEntry = Entry(ch6Frame, width=6)
ch6CurrentEntry.pack(side=LEFT)

Label(ch6Frame, text="uA").pack(side=LEFT)

ch6TimeEntry = Entry(ch6Frame, width=6)
ch6TimeEntry.pack(side=LEFT)

Label(ch6Frame, text="min").pack(side=LEFT)

ch6EnableCheck = Checkbutton(ch6Frame, text="Enable", variable = IntVar())
ch6EnableCheck.pack(side=LEFT)

ch6Frame.pack()
#end CH6


#begin CH7
ch7Frame = Frame(channelsFrame)

ch7Label = Label(ch7Frame, text="CH7")
ch7Label.pack(side=LEFT)

ch7CurrentEntry = Entry(ch7Frame, width=6)
ch7CurrentEntry.pack(side=LEFT)

Label(ch7Frame, text="uA").pack(side=LEFT)

ch7TimeEntry = Entry(ch7Frame, width=6)
ch7TimeEntry.pack(side=LEFT)

Label(ch7Frame, text="min").pack(side=LEFT)

ch7EnableCheck = Checkbutton(ch7Frame, text="Enable", variable = IntVar())
ch7EnableCheck.pack(side=LEFT)

ch7Frame.pack()
#end CH7


#begin CH8
ch8Frame = Frame(channelsFrame)

ch8Label = Label(ch8Frame, text="CH8")
ch8Label.pack(side=LEFT)

ch8CurrentEntry = Entry(ch8Frame, width=6)
ch8CurrentEntry.pack(side=LEFT)

Label(ch8Frame, text="uA").pack(side=LEFT)

ch8TimeEntry = Entry(ch8Frame, width=6)
ch8TimeEntry.pack(side=LEFT)

Label(ch8Frame, text="min").pack(side=LEFT)

ch8EnableCheck = Checkbutton(ch8Frame, text="Enable", variable = IntVar())
ch8EnableCheck.pack(side=LEFT)

ch8Frame.pack()
#end CH8

channelsFrame.pack(side=LEFT)

#end channels frame


plotFrame = Frame(root)

# the figure that will contain the plot
fig = Figure(figsize = (3, 3),
                dpi = 100)

# list of squares
y = [i**2 for i in range(101)]

# adding the subplot
plot1 = fig.add_subplot(111)

# plotting the graph
plot1.plot(y)

# creating the Tkinter canvas
# containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master = plotFrame)
canvas.draw()

# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack()

plotFrame.pack()

root.mainloop()
