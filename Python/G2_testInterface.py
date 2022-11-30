import tkinter as tk
from tkinter import *
from tkinter import filedialog
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import datetime
import device
import csv
import numpy
from tkinter import ttk
from PIL import ImageTk

class windowPage2(tk.Frame):
    def __init__(self, parent, dev):
        tk.Frame.__init__(self, parent)

# temp list, replace with list of ports from pyserial --------------------------
        #portList = device.getPortList()
        #dev = device.Device()
        #dev.detect()

# Tkinter initiate -------------------------------------------------------------
        grisclaro_boton = "#fdfdfd"
        blanco_boton = "#ffffff"
        grisclaro_linea = "#f3f3f3"
        grismedio = "#f0f0f0"

        global y
        y = 0


        self.configure(background="white")

        upFrame = Frame(master=self, width = 1,height = 1, background="white")
        upFrame.grid(row=0,column=0,padx = 1,pady = 5)
        midFrame = Frame(master=self, width = 1,height = 1, background=grismedio)
        midFrame.grid(row=1,column=0,padx = 1,pady = 0)
        lowFrame = Frame(master=self, width = 837,height = 15, background=grismedio)
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
            #dev.port("COM6")
            dev.setChannel(1, current, time)

# topFrame second thing
        #topFrame.after(1000, oneSecondThing)


# Begin port connection frame --------------------------------------------------
        titlePortControl = Label(topFrame, text = "Fast Test", width = 20, height = 3, background = "white")
        titlePortControl.grid(row=0, column=0, padx = 50, pady = 1)
        controlFrame =Frame(topFrame,width = 1, height = 1, background="white")
        controlFrame.grid(row=1,column=0,padx = 50,pady = 1)

        self.playF = PhotoImage(file="play2.png")
        self.original_playF = self.playF.subsample(15,15) # resize image using subsample
        buttonStart = Button(controlFrame, text="   30 sec  ", image = self.original_playF, compound = "left", width = 90, height = 50, command = buttonStartFunction,background = grisclaro_boton)
        buttonStart.grid(row=0,column=0,padx = 1,pady = 1)

# Begin port connection frame --------------------------------------------------
        titleControlFrame = Label(topFrame, text = "Device Control", width = 20, height = 3, background = "white")
        titleControlFrame.grid(row=0, column=2, padx = 50, pady = 1)
        controlFrame =Frame(topFrame,width = 1, height = 1, background="white")
        controlFrame.grid(row=1,column=2,padx = 50,pady = 1)

        self.play = PhotoImage(file="play2.png")
        self.original_play = self.play.subsample(15,15) # resize image using subsample
        buttonStart = Button(controlFrame, text="   Start ", image = self.original_play, compound = "left", width = 90, height = 50, command = buttonStartFunction,background = grisclaro_boton)
        buttonStart.grid(row=0,column=0,padx = 1,pady = 1)

        self.stop = PhotoImage(file="stop.png")
        self.original_stop = self.stop.subsample(15,15) # resize image using subsample
        buttonStop = Button(controlFrame, text="    Stop  ", image = self.original_stop, compound = "left", width = 90, height = 50,background = grisclaro_boton)
        buttonStop.grid(row=0,column=1,padx = 1,pady = 1)



#Data Graph box ---- -----------------------------------------------------------
        box_graphs = Frame(midFrame, width = 400, height = 300, background=grismedio)
        box_graphs.grid(row=2, column=0, padx=19, pady=1)
        GraphFrame = Frame(box_graphs, width = 3, height = 3, background = grismedio)
        GraphFrame.grid(row=0, column=0, padx = 285, pady = 180)





#Calibrate -- ------------------------------------------------------------------

        CalibratelBox = Frame(master = midFrame, width = 10, height = 10, background=grisclaro_linea)
        CalibratelBox.grid(row=1,column=1,padx = 20, pady = 20)

        multimeterLabel = Label(CalibratelBox, text="Real Current - uA")
        multimeterLabel.grid(row=0,column=0,padx = 1,pady = 1)
        currentEntry = Entry(CalibratelBox, width=6)
        currentEntry.grid(row=1,column=0,padx = 1,pady = 1)

        self.setImage = PhotoImage(file="set.png")
        self.original_setImage = self.setImage.subsample(25,25) # resize image using subsample
        buttonCalibrate = Button(CalibratelBox, text="  Calibrate", image = self.original_setImage, compound = 'left',height = 50, width = 100,background=grismedio)
        buttonCalibrate.grid(row=2,column=0,padx = 10, pady = 10)




#Export Excel & JPG -- ---------------------------------------------------------
        exportExcel = Frame(midFrame, width = 62, height = 50, background=grismedio)
        exportExcel.grid(row=2,column=1,padx = 1,pady = 1)

        def write_Excel():
            file = filedialog.asksaveasfile(defaultextension='.xls',filetypes=[("Excel file",".xls"),("CSV file",".csv")])
            filetext = str("hola")
            file.write(filetext)
            file.close()

        def write_graph():
            filename = filedialog.asksaveasfilename(defaultextension='.png',filetypes=[("PNG file",".png"),("JPG file",".jpg")])
            figure1 = export_1.figure
            figure1.set_size_inches(18.5, 10.5)
            figure1.savefig(filename)

        self.excelImage = PhotoImage(file="excel.png")
        self.original_excelImage = self.excelImage.subsample(55,55) # resize image using subsample
        buttonReExcel = Button(exportExcel, text="    Excel ", image = self.original_excelImage, compound = tk.LEFT,command=lambda: write_Excel(),height = 50, width = 100,background=grismedio)
        buttonReExcel.grid(row=0,column=0,padx = 60, pady = 1)

        self.graphImage = PhotoImage(file="profits.png")
        self.original_graphImage = self.graphImage.subsample(15,15) # resize image using subsample
        buttonReExcel = Button(exportExcel, text="     PNG  ", image = self.original_graphImage, compound = 'left',command=lambda: write_graph(),height = 50, width = 100,background=grismedio)
        buttonReExcel.grid(row=1,column=0,padx = 60, pady = 1)

#Finish ------------------------------------------------------------------------
        return
