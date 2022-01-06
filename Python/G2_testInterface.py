import tkinter as tk
from tkinter import *
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import datetime
import device
import csv

# temp list, replace with list of ports from pyserial --------------------------
portList = device.getPortList()
dev = device.Device()
dev.detect()

# Tkinter initiate -------------------------------------------------------------
root = Tk()
root.title("CALIBRATION")
root.geometry("730x700")
color = "#f5f4f6"
root.configure(background=color)
topFrame = Frame(master=root, width = 20,height = 20, background=color)
topFrame.grid(row=0,column=0,padx = 20,pady = 20)

# oneSecond  ------------------------------------------------------------------
def oneSecondThing():
    print('{:%M:%S}'.format(datetime.datetime.now()))
    #dev.getData() #dont use this yet
    topFrame.after(1000, oneSecondThing)

# Button once Start is pressed ------------------------------------------------
def buttonStartFunction():
    current = ch1CurrentEntry.get()
    time = ch1TimeEntry.get()
    dev.port("COM6")
    dev.setChannel(1, current, time)

# topFrame second thing
topFrame.after(1000, oneSecondThing)

# refresh port  ----------------------------------------------------------------
def buttonRefreshPortFunction():
    portList = device.getPortList()
    portMenuValue.set('')
    portMenu['menu'].delete(0, 'end')
    for port in portList:
        portMenu['menu'].add_command(label=port, command=tk._setit(portMenuValue, port))
    portMenuValue.set(portList[0]) # default value


# Begin port connection frame -------------------------------------------------
portFrame = LabelFrame(topFrame, text="Device Connection",width = 180, height = 200, background=color)
portFrame.grid(row=0,column=0,padx = 10, pady = 10)

portMenuValue = StringVar()
portMenuValue.set(portList[0]) # default value, background=color
portMenu = OptionMenu(portFrame, portMenuValue, *portList)
portMenu.config(width=len(max(portList, key=len)))
portMenu.grid(row=1,column=0,padx = 10, pady = 10)

buttonRefreshPort = Button(portFrame, text="Refresh", command=buttonRefreshPortFunction)
buttonRefreshPort.grid(row=1,column=1,padx = 10, pady = 10)
buttonDetectPort = Button(portFrame, text="Auto Detect")
buttonDetectPort.grid(row=1,column=2,padx = 10, pady = 10)
buttonConnectPort = Button(portFrame, text="Connect")
buttonConnectPort.grid(row=1,column=3,padx = 10, pady = 10)
spacePortFrame = LabelFrame(topFrame, text="     ").grid(row=0,column=1,padx = 10,pady = 10)


# Begin port connection frame --------------------------------------------------
controlFrame = LabelFrame(topFrame, text="Device Control",width = 300, height = 200,background=color)
controlFrame.grid(row=0,column=2,padx = 10,pady = 10)

play = PhotoImage(file="play2.png")
original_play = play.subsample(15,15) # resize image using subsample
buttonStart = Button(controlFrame, text=" 30 sec ", image = original_play, compound = 'left',command = buttonStartFunction)
buttonStart.grid(row=0,column=0,padx = 10,pady = 10)

stop = PhotoImage(file="stop.png")
original_stop = stop.subsample(15,15) # resize image using subsample
buttonStop = Button(controlFrame, text="  Stop  ", image = original_stop, compound = 'left')
buttonStop.grid(row=1,column=0,padx = 10,pady = 10)

pika = PhotoImage(file="Pika3.png")
original_pika = pika.subsample(3,3) # resize image using subsample
Label(root, image=original_pika).grid(row=0, column=1, padx=1, pady=1)

# TODO: create the 8 channels with loop
#Begin channels frame (boxes for current and time )-----------------------------
channelsFrame = LabelFrame(root, text="Channel Control",width = 250, height = 100, background=color)
channelsFrame.grid(row=1,column=0,padx = 20,pady = 0)

#begin CH1 ---------------------------------------------------------------------
ch1Frame = Frame(channelsFrame)
ch1Frame.grid(row=0,column=0,padx = 1,pady = 1)
ch1Label = Label(ch1Frame, text="CH1")
ch1Label.grid(row=0,column=0,padx = 1,pady = 1)
ch1CurrentEntry = Entry(ch1Frame, width=6)
ch1CurrentEntry.grid(row=0,column=1,padx = 1,pady = 1)
Label(ch1Frame, text="uA   ").grid(row=0,column=2,padx = 1,pady = 1)
ch1Invert = Checkbutton(ch1Frame, text="Invert   ", variable = IntVar())
ch1Invert.grid(row=0,column=3,padx = 1,pady = 1)
ch1EnableCheck = Checkbutton(ch1Frame, text="Enable", variable = IntVar())
ch1EnableCheck.grid(row=0,column=5,padx = 1,pady = 1)
ch1space = Label(ch1Frame, text="       ").grid(row=0,column=6,padx = 1,pady = 1)


#begin CH2 ---------------------------------------------------------------------
ch2Frame = Frame(channelsFrame)
ch2Frame.grid(row=1,column=0,padx = 1,pady = 1)
ch2Label = Label(ch2Frame, text="CH2")
ch2Label.grid(row=1,column=0,padx = 1,pady = 1)
ch2CurrentEntry = Entry(ch2Frame, width=6)
ch2CurrentEntry.grid(row=1,column=1,padx = 1,pady = 1)
Label(ch2Frame, text="uA   ").grid(row=1,column=2,padx = 1,pady = 1)
ch2Invert = Checkbutton(ch2Frame, text="Invert   ", variable = IntVar())
ch2Invert.grid(row=1,column=3,padx = 1,pady = 1)
ch2EnableCheck = Checkbutton(ch2Frame, text="Enable", variable = IntVar())
ch2EnableCheck.grid(row=1,column=5,padx = 1,pady = 1)
ch2space = Label(ch2Frame, text="       ").grid(row=1,column=6,padx = 1,pady = 1)


#begin CH3 ---------------------------------------------------------------------
ch3Frame = Frame(channelsFrame)
ch3Frame.grid(row=2,column=0,padx = 1,pady = 1)
ch3Label = Label(ch3Frame, text="CH3")
ch3Label.grid(row=2,column=0,padx = 1,pady = 1)
ch3CurrentEntry = Entry(ch3Frame, width=6)
ch3CurrentEntry.grid(row=2,column=1,padx = 1,pady = 1)
Label(ch3Frame, text="uA   ").grid(row=2,column=2,padx = 1,pady = 1)
ch3Invert = Checkbutton(ch3Frame, text="Invert   ", variable = IntVar())
ch3Invert.grid(row=2,column=3,padx = 1,pady = 1)
ch3EnableCheck = Checkbutton(ch3Frame, text="Enable", variable = IntVar())
ch3EnableCheck.grid(row=2,column=5,padx = 1,pady = 1)
ch3space = Label(ch3Frame, text="       ").grid(row=2,column=6,padx = 1,pady = 1)


#begin CH4 --------------------------------------------------------------------
ch4Frame = Frame(channelsFrame)
ch4Frame.grid(row=3,column=0,padx = 1,pady = 1)
ch4Label = Label(ch4Frame, text="CH4")
ch4Label.grid(row=3,column=0,padx = 1,pady = 1)
ch4CurrentEntry = Entry(ch4Frame, width=6)
ch4CurrentEntry.grid(row=3,column=1,padx = 1,pady = 1)
Label(ch4Frame, text="uA   ").grid(row=3,column=2,padx = 1,pady = 1)
ch4Invert = Checkbutton(ch4Frame, text="Invert   ", variable = IntVar())
ch4Invert.grid(row=3,column=3,padx = 1,pady = 1)
ch4EnableCheck = Checkbutton(ch4Frame, text="Enable", variable = IntVar())
ch4EnableCheck.grid(row=3,column=5,padx = 1,pady = 1)
ch4space = Label(ch4Frame, text="       ").grid(row=3,column=6,padx = 1,pady = 1)


#begin CH5----------------------------------------------------------------------
ch5Frame = Frame(channelsFrame)
ch5Frame.grid(row=0,column=1,padx = 1,pady = 1)
ch5Label = Label(ch5Frame, text="CH5")
ch5Label.grid(row=0,column=0,padx = 1,pady = 1)
ch5CurrentEntry = Entry(ch5Frame, width=6)
ch5CurrentEntry.grid(row=0,column=1,padx = 1,pady = 1)
Label(ch5Frame, text="uA   ").grid(row=0,column=2,padx = 1,pady = 1)
ch5Invert = Checkbutton(ch5Frame, text="Invert   ", variable = IntVar())
ch5Invert.grid(row=0,column=3,padx = 1,pady = 1)
ch5EnableCheck = Checkbutton(ch5Frame, text="Enable", variable = IntVar())
ch5EnableCheck.grid(row=0,column=5,padx = 1,pady = 1)


#begin CH6 ---------------------------------------------------------------------
ch6Frame = Frame(channelsFrame)
ch6Frame.grid(row=1,column=1,padx = 1,pady = 1)
ch6Label = Label(ch6Frame, text="CH6")
ch6Label.grid(row=1,column=0,padx = 1,pady = 1)
ch6CurrentEntry = Entry(ch6Frame, width=6)
ch6CurrentEntry.grid(row=1,column=1,padx = 1,pady = 1)
Label(ch6Frame, text="uA   ").grid(row=1,column=2,padx = 1,pady = 1)
ch6Invert = Checkbutton(ch6Frame, text="Invert   ", variable = IntVar())
ch6Invert.grid(row=1,column=3,padx = 1,pady = 1)
ch6EnableCheck = Checkbutton(ch6Frame, text="Enable", variable = IntVar())
ch6EnableCheck.grid(row=1,column=5,padx = 1,pady = 1)


#begin CH7 --------------------------------------------------------------------
ch7Frame = Frame(channelsFrame)
ch7Frame.grid(row=2,column=1,padx = 1,pady = 1)
ch7Label = Label(ch7Frame, text="CH7")
ch7Label.grid(row=2,column=0,padx = 1,pady = 1)
ch7CurrentEntry = Entry(ch7Frame, width=6)
ch7CurrentEntry.grid(row=2,column=1,padx = 1,pady = 1)
Label(ch7Frame, text="uA   ").grid(row=2,column=2,padx = 1,pady = 1)
ch7Invert = Checkbutton(ch7Frame, text="Invert   ", variable = IntVar())
ch7Invert.grid(row=2,column=3,padx = 1,pady = 1)
ch7EnableCheck = Checkbutton(ch7Frame, text="Enable", variable = IntVar())
ch7EnableCheck.grid(row=2,column=5,padx = 1,pady = 1)

#begin CH8 --------------------------------------------------------------------
ch8Frame = Frame(channelsFrame)
ch8Frame.grid(row=3,column=1,padx = 1,pady = 1)
ch8Label = Label(ch8Frame, text="CH8")
ch8Label.grid(row=3,column=0,padx = 1,pady = 1)
ch8CurrentEntry = Entry(ch8Frame, width=6)
ch8CurrentEntry.grid(row=3,column=1,padx = 1,pady = 1)
Label(ch8Frame, text="uA   ").grid(row=3,column=2,padx = 1,pady = 1)
ch8Invert = Checkbutton(ch8Frame, text="Invert   ", variable = IntVar())
ch8Invert.grid(row=3,column=3,padx = 1,pady = 1)
ch8EnableCheck = Checkbutton(ch8Frame, text="Enable", variable = IntVar())
ch8EnableCheck.grid(row=3,column=5,padx = 1,pady = 1)

#Calibrtion --------------------------------------------------------------------

calibrationArea = LabelFrame(root, text="Calibration",width = 100, height = 50, background=color)
calibrationArea.grid(row=1,column=1,padx = 20,pady = 0)

multimeterLabel = Label(calibrationArea, text="Real Current - uA")
multimeterLabel.grid(row=0,column=0,padx = 1,pady = 1)
currentEntry = Entry(calibrationArea, width=6)
currentEntry.grid(row=1,column=0,padx = 1,pady = 1)

setImage = PhotoImage(file="set.png")
original_setImage = setImage.subsample(25,25) # resize image using subsample
buttonCalibrate = Button(calibrationArea, text="  Calibrate", image = original_setImage, compound = 'left')
buttonCalibrate.grid(row=2,column=0,padx = 10, pady = 10)

#Export Excel -- ----------------------------------------------------------------

exportExcel = LabelFrame(root, text="Export",width = 100, height = 50, background=color)
exportExcel.grid(row=2,column=1,padx = 20,pady = 0)


def write_Excel():
    file = filedialog.asksaveasfile(defaultextension='.xls',filetypes=[("Excel file",".xls"),("CSV file",".csv")])
    filetext = str("hola")
    file.write(filetext)
    file.close()

def write_graph():
    file = filedialog.asksaveasfile(defaultextension='.png',filetypes=[("PNG file",".png"),("JPG file",".jpg")])
    filetext = str("hola")
    file.write(filetext)
    file.close()

excelImage = PhotoImage(file="excel.png")
original_excelImage = excelImage.subsample(55,55) # resize image using subsample
buttonReExcel = Button(exportExcel, text="  Excel", image = original_excelImage, compound = 'left',command=lambda: write_Excel())
buttonReExcel.grid(row=0,column=0,padx = 10, pady = 10)

graphImage = PhotoImage(file="profits.png")
original_graphImage = graphImage.subsample(15,15) # resize image using subsample
buttonReExcel = Button(exportExcel, text="   PNG  ", image = original_graphImage, compound = 'left',command=lambda: write_graph())
buttonReExcel.grid(row=1,column=0,padx = 10, pady = 10)


#Data box ---- ----------------------------------------------------------------

box_graphs = LabelFrame(root, text="Graph",width = 500, height = 300, bg=color)
box_graphs.grid(row=2, column=0, padx=10, pady=10)

buttonArea = Frame(box_graphs, width = 30, height = 300, background=color)
buttonArea.grid(row=0,column=0,padx = 1, pady = 3)

buttonGraph1 = Button(buttonArea, text=" CH1 ")
buttonGraph1.grid(row=0,column=0,padx = 1,pady = 3)

buttonGraph2 = Button(buttonArea, text=" CH2 ")
buttonGraph2.grid(row=1,column=0,padx = 1,pady = 3)

buttonGraph3 = Button(buttonArea, text=" CH3 ")
buttonGraph3.grid(row=2,column=0,padx = 1,pady = 3)

buttonGraph4 = Button(buttonArea, text=" CH4 ")
buttonGraph4.grid(row=3,column=0,padx = 1,pady = 3)

buttonGraph5 = Button(buttonArea, text=" CH5 ")
buttonGraph5.grid(row=4,column=0,padx = 1,pady = 3)

buttonGraph6 = Button(buttonArea, text=" CH6 ")
buttonGraph6.grid(row=5,column=0,padx = 1,pady = 1)

buttonGraph7 = Button(buttonArea, text=" CH7 ")
buttonGraph7.grid(row=6,column=0,padx = 1,pady = 3)

buttonGraph8 = Button(buttonArea, text=" CH8 ")
buttonGraph8.grid(row=7,column=0,padx = 1,pady = 3)

buttonGraphAll = Button(buttonArea, text="  All  ")
buttonGraphAll.grid(row=8,column=0,padx = 1,pady = 3)

graphArea = Frame(box_graphs, width = 450, height = 300, background=color)
graphArea.grid(row=0,column=1,padx = 1, pady = 1)

# the figure that will contain the plot
fig = Figure(figsize = (4.65, 3), dpi = 100)
# list of squares
y = [i**2 for i in range(101)]
# adding the subplot
plot1 = fig.add_subplot(111)
# plotting the graph
plot1.plot(y)

# creating the Tkinter canvas
# containing the Matplotlib figure
canvas = FigureCanvasTkAgg(fig, master = graphArea)
#anvas.draw()
# placing the canvas on the Tkinter window
canvas.get_tk_widget().grid(row=0,column=0)

root.mainloop()
