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
        ch8EnableCheck = Checkbutton(ch8Frame, text="Enable", variable = IntVar(),background=grismedio)
        ch8EnableCheck.grid(row=3,column=5,padx = 1,pady = 1)

#Data Graph box ---- -----------------------------------------------------------
        box_graphs = Frame(midFrame, width = 400, height = 300, background=grismedio)
        box_graphs.grid(row=2, column=0, padx=19, pady=1)
        GraphFrame = Frame(box_graphs, width = 3, height = 3, background = grismedio)
        GraphFrame.grid(row=0, column=0, padx = 0, pady = 1)
        ButtonGraphFrame = Frame(box_graphs,  width = 3, height = 3, background = grismedio)
        ButtonGraphFrame.grid(row=0, column=1, padx = 0, pady = 1)

#Buttons box ---- --------------------------------------------------------------

        global figOption
        figOption = 1

        def which_button1():
            buttonConnectPort1.config(bg=blanco_boton)
            buttonConnectPort2.config(bg=grismedio)
            buttonConnectPort3.config(bg=grismedio)
            buttonConnectPort4.config(bg=grismedio)
            buttonConnectPort5.config(bg=grismedio)
            buttonConnectPort6.config(bg=grismedio)
            buttonConnectPort7.config(bg=grismedio)
            buttonConnectPort8.config(bg=grismedio)
            buttonConnectPort9.config(bg=grismedio)
            figOption = 1
            y1 = i
            plot1.plot(y1)
            print(figOption)




        def which_button2():
            buttonConnectPort1.config(bg=grismedio)
            buttonConnectPort2.config(bg=blanco_boton)
            buttonConnectPort3.config(bg=grismedio)
            buttonConnectPort4.config(bg=grismedio)
            buttonConnectPort5.config(bg=grismedio)
            buttonConnectPort6.config(bg=grismedio)
            buttonConnectPort7.config(bg=grismedio)
            buttonConnectPort8.config(bg=grismedio)
            buttonConnectPort9.config(bg=grismedio)
            figOption = 2
            y1 = i**2
            plot1.plot(y1)
            print(figOption)



        def which_button3():
            buttonConnectPort1.config(bg=grismedio)
            buttonConnectPort2.config(bg=grismedio)
            buttonConnectPort3.config(bg=blanco_boton)
            buttonConnectPort4.config(bg=grismedio)
            buttonConnectPort5.config(bg=grismedio)
            buttonConnectPort6.config(bg=grismedio)
            buttonConnectPort7.config(bg=grismedio)
            buttonConnectPort8.config(bg=grismedio)
            buttonConnectPort9.config(bg=grismedio)
            figOption = 3
            print(figOption)

        def which_button4():
            buttonConnectPort1.config(bg=grismedio)
            buttonConnectPort2.config(bg=grismedio)
            buttonConnectPort3.config(bg=grismedio)
            buttonConnectPort4.config(bg=blanco_boton)
            buttonConnectPort5.config(bg=grismedio)
            buttonConnectPort6.config(bg=grismedio)
            buttonConnectPort7.config(bg=grismedio)
            buttonConnectPort8.config(bg=grismedio)
            buttonConnectPort9.config(bg=grismedio)
            figOption = 4
            print(figOption)

        def which_button5():
            buttonConnectPort1.config(bg=grismedio)
            buttonConnectPort2.config(bg=grismedio)
            buttonConnectPort3.config(bg=grismedio)
            buttonConnectPort4.config(bg=grismedio)
            buttonConnectPort5.config(bg=blanco_boton)
            buttonConnectPort6.config(bg=grismedio)
            buttonConnectPort7.config(bg=grismedio)
            buttonConnectPort8.config(bg=grismedio)
            buttonConnectPort9.config(bg=grismedio)
            figOption = 5
            print(figOption)

        def which_button6():
            buttonConnectPort1.config(bg=grismedio)
            buttonConnectPort2.config(bg=grismedio)
            buttonConnectPort3.config(bg=grismedio)
            buttonConnectPort4.config(bg=grismedio)
            buttonConnectPort5.config(bg=grismedio)
            buttonConnectPort6.config(bg=blanco_boton)
            buttonConnectPort7.config(bg=grismedio)
            buttonConnectPort8.config(bg=grismedio)
            buttonConnectPort9.config(bg=grismedio)
            figOption = 6
            print(figOption)

        def which_button7():
            buttonConnectPort1.config(bg=grismedio)
            buttonConnectPort2.config(bg=grismedio)
            buttonConnectPort3.config(bg=grismedio)
            buttonConnectPort4.config(bg=grismedio)
            buttonConnectPort5.config(bg=grismedio)
            buttonConnectPort6.config(bg=grismedio)
            buttonConnectPort7.config(bg=blanco_boton)
            buttonConnectPort8.config(bg=grismedio)
            buttonConnectPort9.config(bg=grismedio)
            figOption = 7
            print(figOption)

        def which_button8():
            buttonConnectPort1.config(bg=grismedio)
            buttonConnectPort2.config(bg=grismedio)
            buttonConnectPort3.config(bg=grismedio)
            buttonConnectPort4.config(bg=grismedio)
            buttonConnectPort5.config(bg=grismedio)
            buttonConnectPort6.config(bg=grismedio)
            buttonConnectPort7.config(bg=grismedio)
            buttonConnectPort8.config(bg=blanco_boton)
            buttonConnectPort9.config(bg=grismedio)
            figOption = 8
            print(figOption)

        def which_button9():
            buttonConnectPort1.config(bg=grismedio)
            buttonConnectPort2.config(bg=grismedio)
            buttonConnectPort3.config(bg=grismedio)
            buttonConnectPort4.config(bg=grismedio)
            buttonConnectPort5.config(bg=grismedio)
            buttonConnectPort6.config(bg=grismedio)
            buttonConnectPort7.config(bg=grismedio)
            buttonConnectPort8.config(bg=grismedio)
            buttonConnectPort9.config(bg=blanco_boton)
            figOption = 9
            print(figOption)

        buttonConnectPort1 = Button(ButtonGraphFrame, text="CH1",height = 2, width = 10,background = grisclaro_boton,command=which_button1)
        buttonConnectPort1.grid(row=0,column=0,padx = 0, pady = 0)
        buttonConnectPort2 = Button(ButtonGraphFrame, text="CH2",height = 2, width = 10,background = grismedio,command=which_button2)
        buttonConnectPort2.grid(row=1,column=0,padx = 0, pady = 0)
        buttonConnectPort3 = Button(ButtonGraphFrame, text="CH3",height = 2, width = 10,background = grismedio,command=which_button3)
        buttonConnectPort3.grid(row=2,column=0,padx = 0, pady = 0)
        buttonConnectPort4 = Button(ButtonGraphFrame, text="CH4",height = 2, width = 10,background = grismedio,command=which_button4)
        buttonConnectPort4.grid(row=3,column=0,padx = 0, pady = 0)
        buttonConnectPort5 = Button(ButtonGraphFrame, text="CH5",height = 2, width = 10,background = grismedio,command=which_button5)
        buttonConnectPort5.grid(row=4,column=0,padx = 0, pady = 0)
        buttonConnectPort6 = Button(ButtonGraphFrame, text="CH6",height = 2, width = 10,background = grismedio,command=which_button6)
        buttonConnectPort6.grid(row=5,column=0,padx = 0, pady = 0)
        buttonConnectPort7 = Button(ButtonGraphFrame, text="CH7",height = 2, width = 10,background = grismedio,command=which_button7)
        buttonConnectPort7.grid(row=6,column=0,padx = 0, pady = 0)
        buttonConnectPort8 = Button(ButtonGraphFrame, text="CH8",height = 2, width = 10,background = grismedio,command=which_button8)
        buttonConnectPort8.grid(row=7,column=0,padx = 0, pady = 0)
        buttonConnectPort9 = Button(ButtonGraphFrame, text="ALL",height = 2, width = 10,background = grismedio,command=which_button9)
        buttonConnectPort9.grid(row=8,column=0,padx = 0, pady = 0)



        #grismedio_boton = "#f0f0f0"

#Graph -------------------------------------------------------------------------
        # the figure that will contain the plot


        '''
        while True:
            if (figOption == 1):

            elif (figOption == 2):
                y1 = -i
            elif (figOption == 3):
                y1 = 2*i
            elif (figOption == 4):
                y1 = -2*i
            elif (figOption == 5):
                y1 = i**2
            elif (figOption == 6):
                y1 = -i**2
            elif (figOption == 7):
                y1 = i**3
            elif (figOption == 8):
                y1 = -i**3
            break
        '''

        i = numpy.linspace(1,111)
        fig1 = Figure(figsize = (7, 5.3), dpi = 70)
        plot1 = fig1.add_subplot(111)
        fig1.subplots_adjust(left=0.05, bottom=0.05, right=0.995, top=0.995, wspace=1, hspace=1)
        export_1 = plot1

        '''

        fig1 = Figure(figsize = (7, 5.3), dpi = 70)
        plot1 = fig1.add_subplot(111)
        fig1.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=1, hspace=1)
        export_1 = plot1

        fig1, axis = plt.subplots(4, 2)


        axis[0,0].plot(y1)
        axis[1,0].plot(y1)
        axis[2,0].plot(y1)
        axis[3,0].plot(y1)
        axis[0,1].plot(y1)
        axis[1,1].plot(y1)
        axis[2,1].plot(y1)
        axis[3,1].plot(y1)
        '''


        canvas1 = FigureCanvasTkAgg(fig1, master = GraphFrame)
        canvas1.get_tk_widget().grid(row=0,column=0)

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
