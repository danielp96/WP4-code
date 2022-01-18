import tkinter as tk
from tkinter import *
from tkinter import filedialog
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import datetime
import device
import csv
from tkinter import ttk
from PIL import ImageTk

class windowPage1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)


# temp list, replace with list of ports from pyserial --------------------------
        portList = device.getPortList()
        dev = device.Device()
        dev.detect()


# Tkinter initiate -------------------------------------------------------------
        grisclaro_boton = "#fdfdfd"
        blanco_boton = "#ffffff"
        grisclaro_linea = "#f3f3f3"
        grismedio = "#f0f0f0"
        self.configure(background="white")

        upFrame = Frame(master=self, width = 1,height = 1, background="white")
        upFrame.grid(row=0,column=0,padx = 1,pady = 5)
        midFrame = Frame(master=self, width = 1,height = 1, background=grismedio)
        midFrame.grid(row=1,column=0,padx = 1,pady = 0)
        lowFrame = Frame(master=self, width = 842,height = 15, background=grismedio)
        lowFrame.grid(row=2,column=0,padx = 1,pady = 0)

        topFrame = Frame(upFrame, width = 1,height = 1, background="white")
        topFrame.grid(row=0,column=0,padx = 1,pady = 1)
        height_buttom = 3  # no image button size
        width_buttom = 15  # no image button size

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
        titlePortFrame = Label(topFrame, text = "Device Connection", width = 20, height = 3, background = "white")
        titlePortFrame.grid(row=0, column=0, padx = 38, pady = 1)
        portFrame = Frame(topFrame, width = 1, height = 1, background="white")
        portFrame.grid(row=1,column=0,padx = 38, pady = 1)

        portMenuValue = StringVar()
        portMenuValue.set(portList[0]) # default value, background=color
        portMenu = OptionMenu(portFrame, portMenuValue, *portList)
        portMenu.config(background = grisclaro_boton,width=len(max(portList, key=len)))
        portMenu.grid(row=1,column=0,padx = 10, pady = 10)

        buttonRefreshPort = Button(portFrame, text="Refresh", command=buttonRefreshPortFunction, height = height_buttom, width = width_buttom,background = grisclaro_boton)
        buttonRefreshPort.grid(row=1,column=1,padx = 0, pady = 0)
        buttonDetectPort = Button(portFrame, text="Auto Detect",height = height_buttom, width = width_buttom,background = grisclaro_boton)
        buttonDetectPort.grid(row=1,column=2,padx = 0, pady = 0)
        buttonConnectPort = Button(portFrame, text="Connect", height = height_buttom, width = width_buttom,background = grisclaro_boton)
        buttonConnectPort.grid(row=1,column=3,padx = 0, pady = 0)
        spacePortFrame = LabelFrame(topFrame, text="     ").grid(row=0,column=1,padx = 10,pady = 3) # blank space between frames

# Begin port connection frame --------------------------------------------------
        titleControlFrame = Label(topFrame, text = "Device Control", width = 20, height = 3, background = "white")
        titleControlFrame.grid(row=0, column=2, padx = 50, pady = 1)
        controlFrame =Frame(topFrame,width = 1, height = 1, background="white")
        controlFrame.grid(row=1,column=2,padx = 50,pady = 1)

        self.play = PhotoImage(file="play2.png")
        self.original_play = self.play.subsample(15,15) # resize image using subsample
        buttonStart = Button(controlFrame, text="   Play  ", image = self.original_play, compound = "left", width = 90, height = 50, command = buttonStartFunction,background = grisclaro_boton)
        buttonStart.grid(row=0,column=0,padx = 1,pady = 1)

        self.stop = PhotoImage(file="stop.png")
        self.original_stop = self.stop.subsample(15,15) # resize image using subsample
        buttonStop = Button(controlFrame, text="    Stop  ", image = self.original_stop, compound = "left", width = 90, height = 50,background = grisclaro_boton)
        buttonStop.grid(row=0,column=1,padx = 1,pady = 1)

# TODO: create the 8 channels with loop ----------------------------------------
        channelBox = Frame(master = midFrame, width = 10, height = 10, background=grisclaro_linea)
        channelBox.grid(row=1,column=0,padx = 20, pady = 20)
        channelsFrame =Frame(channelBox, width = 250, height = 100, background=grisclaro_linea)
        channelsFrame.grid(row=1,column=1,padx = 1,pady = 1)

#begin CH1 ---------------------------------------------------------------------
        ch1Frame = Frame(channelsFrame,background=grismedio)
        ch1Frame.grid(row=0,column=0,padx = 1,pady = 1)
        ch1Label = Label(ch1Frame, text="CH1",background=grismedio)
        ch1Label.grid(row=0,column=0,padx = 1,pady = 1)
        ch1CurrentEntry = Entry(ch1Frame, width=6)
        ch1CurrentEntry.grid(row=0,column=1,padx = 1,pady = 1)
        Label(ch1Frame, text="uA   ",background=grismedio).grid(row=0,column=2,padx = 1,pady = 1)
        ch1TimeEntry = Entry(ch1Frame, width=6)
        ch1TimeEntry.grid(row=0,column=3,padx = 1,pady = 1)
        Label(ch1Frame, text="min").grid(row=0,column=4,padx = 1,pady = 1)
        ch1EnableCheck = Checkbutton(ch1Frame, text="Enable", variable = IntVar(),background=grismedio)
        ch1EnableCheck.grid(row=0,column=5,padx = 1,pady = 1)
        ch1space = Label(ch1Frame, text="             ",background=grismedio).grid(row=0,column=6,padx = 1,pady = 1)

#begin CH2 ---------------------------------------------------------------------
        ch2Frame = Frame(channelsFrame,background=grismedio)
        ch2Frame.grid(row=1,column=0,padx = 1,pady = 1)
        ch2Label = Label(ch2Frame, text="CH2",background=grismedio)
        ch2Label.grid(row=1,column=0,padx = 1,pady = 1)
        ch2CurrentEntry = Entry(ch2Frame, width=6)
        ch2CurrentEntry.grid(row=1,column=1,padx = 1,pady = 1)
        Label(ch2Frame, text="uA   ",background=grismedio).grid(row=1,column=2,padx = 1,pady = 1)
        ch2TimeEntry = Entry(ch2Frame, width=6)
        ch2TimeEntry.grid(row=1,column=3,padx = 1,pady = 1)
        Label(ch2Frame, text="min").grid(row=1,column=4,padx = 1,pady = 1)
        ch2EnableCheck = Checkbutton(ch2Frame, text="Enable ", variable = IntVar(),background=grismedio)
        ch2EnableCheck.grid(row=1,column=5,padx = 1,pady = 1)
        ch2space = Label(ch2Frame, text="            ",background=grismedio).grid(row=1,column=6,padx = 1,pady = 1)

    #begin CH3 ---------------------------------------------------------------------
        ch3Frame = Frame(channelsFrame,background=grismedio)
        ch3Frame.grid(row=2,column=0,padx = 1,pady = 1)
        ch3Label = Label(ch3Frame, text="CH3",background=grismedio)
        ch3Label.grid(row=2,column=0,padx = 1,pady = 1)
        ch3CurrentEntry = Entry(ch3Frame, width=6)
        ch3CurrentEntry.grid(row=2,column=1,padx = 1,pady = 1)
        Label(ch3Frame, text="uA   ",background=grismedio).grid(row=2,column=2,padx = 1,pady = 1)
        ch3TimeEntry = Entry(ch3Frame, width=6)
        ch3TimeEntry.grid(row=2,column=3,padx = 1,pady = 1)
        Label(ch3Frame, text="min").grid(row=2,column=4,padx = 1,pady = 1)
        ch3EnableCheck = Checkbutton(ch3Frame, text="Enable ", variable = IntVar(),background=grismedio)
        ch3EnableCheck.grid(row=2,column=5,padx = 1,pady = 1)
        ch3space = Label(ch3Frame, text="            ",background=grismedio).grid(row=2,column=6,padx = 1,pady = 1)

#begin CH4 ---------------------------------------------------------------------
        ch4Frame = Frame(channelsFrame,background=grismedio)
        ch4Frame.grid(row=3,column=0,padx = 1,pady = 1)
        ch4Label = Label(ch4Frame, text="CH4",background=grismedio)
        ch4Label.grid(row=3,column=0,padx = 1,pady = 1)
        ch4CurrentEntry = Entry(ch4Frame, width=6)
        ch4CurrentEntry.grid(row=3,column=1,padx = 1,pady = 1)
        Label(ch4Frame, text="uA   ",background=grismedio).grid(row=3,column=2,padx = 1,pady = 1)
        ch4TimeEntry = Entry(ch4Frame, width=6)
        ch4TimeEntry.grid(row=3,column=3,padx = 1,pady = 1)
        Label(ch4Frame, text="min").grid(row=3,column=4,padx = 1,pady = 1)
        ch4EnableCheck = Checkbutton(ch4Frame, text="Enable", variable = IntVar(),background=grismedio)
        ch4EnableCheck.grid(row=3,column=5,padx = 1,pady = 1)
        ch4space = Label(ch4Frame, text="             ",background=grismedio).grid(row=3,column=6,padx = 1,pady = 1)

#begin CH5----------------------------------------------------------------------
        ch5Frame = Frame(channelsFrame,background=grismedio)
        ch5Frame.grid(row=0,column=1,padx = 1,pady = 1)
        ch5Label = Label(ch5Frame, text="CH5",background=grismedio)
        ch5Label.grid(row=0,column=0,padx = 1,pady = 1)
        ch5CurrentEntry = Entry(ch5Frame, width=6)
        ch5CurrentEntry.grid(row=0,column=1,padx = 1,pady = 1)
        Label(ch5Frame, text="uA   ",background=grismedio).grid(row=0,column=2,padx = 1,pady = 1)
        ch5TimeEntry = Entry(ch5Frame, width=6)
        ch5TimeEntry.grid(row=0,column=3,padx = 1,pady = 1)
        Label(ch5Frame, text="min").grid(row=0,column=4,padx = 1,pady = 1)
        ch5EnableCheck = Checkbutton(ch5Frame, text="Enable", variable = IntVar(),background=grismedio)
        ch5EnableCheck.grid(row=0,column=5,padx = 1,pady = 1)

#begin CH6 ---------------------------------------------------------------------
        ch6Frame = Frame(channelsFrame,background=grismedio)
        ch6Frame.grid(row=1,column=1,padx = 1,pady = 1)
        ch6Label = Label(ch6Frame, text="CH6",background=grismedio)
        ch6Label.grid(row=1,column=0,padx = 1,pady = 1)
        ch6CurrentEntry = Entry(ch6Frame, width=6)
        ch6CurrentEntry.grid(row=1,column=1,padx = 1,pady = 1)
        Label(ch6Frame, text="uA   ",background=grismedio).grid(row=1,column=2,padx = 1,pady = 1)
        ch6TimeEntry = Entry(ch6Frame, width=6)
        ch6TimeEntry.grid(row=1,column=3,padx = 1,pady = 1)
        Label(ch6Frame, text="min").grid(row=1,column=4,padx = 1,pady = 1)
        ch6EnableCheck = Checkbutton(ch6Frame, text="Enable", variable = IntVar(),background=grismedio)
        ch6EnableCheck.grid(row=1,column=5,padx = 1,pady = 1)

#begin CH7 ---------------------------------------------------------------------
        ch7Frame = Frame(channelsFrame,background=grismedio)
        ch7Frame.grid(row=2,column=1,padx = 1,pady = 1)
        ch7Label = Label(ch7Frame, text="CH7",background=grismedio)
        ch7Label.grid(row=2,column=0,padx = 1,pady = 1)
        ch7CurrentEntry = Entry(ch7Frame, width=6)
        ch7CurrentEntry.grid(row=2,column=1,padx = 1,pady = 1)
        Label(ch7Frame, text="uA   ",background=grismedio).grid(row=2,column=2,padx = 1,pady = 1)
        ch7TimeEntry = Entry(ch7Frame, width=6)
        ch7TimeEntry.grid(row=2,column=3,padx = 1,pady = 1)
        Label(ch7Frame, text="min").grid(row=2,column=4,padx = 1,pady = 1)
        ch7EnableCheck = Checkbutton(ch7Frame, text="Enable", variable = IntVar(),background=grismedio)
        ch7EnableCheck.grid(row=2,column=5,padx = 1,pady = 1)

#begin CH8 ---------------------------------------------------------------------
        ch8Frame = Frame(channelsFrame,background=grismedio)
        ch8Frame.grid(row=3,column=1,padx = 1,pady = 1)
        ch8Label = Label(ch8Frame, text="CH8",background=grismedio)
        ch8Label.grid(row=3,column=0,padx = 1,pady = 1)
        ch8CurrentEntry = Entry(ch8Frame, width=6)
        ch8CurrentEntry.grid(row=3,column=1,padx = 1,pady = 1)
        Label(ch8Frame, text="uA   ",background=grismedio).grid(row=3,column=2,padx = 1,pady = 1)
        ch8TimeEntry = Entry(ch8Frame, width=6)
        ch8TimeEntry.grid(row=3,column=3,padx = 1,pady = 1)
        Label(ch8Frame, text="min").grid(row=3,column=4,padx = 1,pady = 1)
        ch8EnableCheck = Checkbutton(ch8Frame, text="Enable", variable = IntVar(),background=grismedio)
        ch8EnableCheck.grid(row=3,column=5,padx = 1,pady = 1)

#Data Table box ---- -----------------------------------------------------------
        box_graphs = Frame(midFrame, width = 400, height = 300, background=grismedio)
        box_graphs.grid(row=2, column=0, padx=19, pady=1)

        ch_columns = Canvas(box_graphs, width = 551,height = 330, background="#ffffff")
        ch_columns.grid(row=0,column=0,rowspan = 100)

        scroll = Scrollbar(box_graphs, orient='vertical', command = ch_columns.yview)
        scroll.grid(row = 0, column = 2, rowspan = 100, sticky = 'ns')
        ch_columns.config(yscrollcommand = scroll.set)

        dataFrame = Frame(ch_columns, bg='white')
        ch_columns.create_window((10,0),window=dataFrame,anchor='nw')

#Export Excel -----------------------------------------------------------------
        exportExcel = Frame(midFrame, width = 62, height = 50, background=grismedio)
        exportExcel.grid(row=2,column=1,padx = 1,pady = 1)

        def write_Excel():
            file = filedialog.asksaveasfile(defaultextension='.xls',filetypes=[("Excel file",".xls"),("CSV file",".csv")])
            filetext = str("hola")
            file.write(filetext)
            file.close()

        self.excelImage = PhotoImage(file="excel.png")
        self.original_excelImage = self.excelImage.subsample(55,55) # resize image using subsample
        buttonReExcel = Button(exportExcel, text="    Excel ", image = self.original_excelImage, compound = tk.LEFT,command=lambda: write_Excel(),height = 50, width = 100,background=grismedio)
        buttonReExcel.grid(row=0,column=0,padx = 60, pady = 1)


#Finish ------------------------------------------------------------------------
        return
