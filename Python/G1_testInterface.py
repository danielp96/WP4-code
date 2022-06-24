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
from guilib import *

class windowPage1(tk.Frame):
    def __init__(self, parent, dev):
        tk.Frame.__init__(self, parent)
        self.dev = dev

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
            #print('{:%M:%S}'.format(datetime.datetime.now()))
            #dev.getData() #dont use this yet
            #if self.dev.running:
            #ch_columns.create_text(80, ch_columns.texty, text = self.getData())
            #ch_columns.texty=ch_columns.texty+12
            topFrame.after(1000, oneSecondThing)


        def buttonSingleFunction():
            ch1EnableCheckVal.set(True)
            for child in ch1Frame.winfo_children():
                child.configure(state='normal')

            ch2EnableCheckVal.set(True)
            for child in ch2Frame.winfo_children():
                child.configure(state='normal')

            ch3EnableCheckVal.set(True)
            for child in ch3Frame.winfo_children():
                child.configure(state='normal')

            ch4EnableCheckVal.set(True)
            for child in ch4Frame.winfo_children():
                child.configure(state='normal')

            ch5EnableCheckVal.set(True)
            for child in ch5Frame.winfo_children():
                child.configure(state='normal')

            ch6EnableCheckVal.set(True)
            for child in ch6Frame.winfo_children():
                child.configure(state='normal')

            ch7EnableCheckVal.set(True)
            for child in ch7Frame.winfo_children():
                child.configure(state='normal')

            ch8EnableCheckVal.set(True)
            for child in ch8Frame.winfo_children():
                child.configure(state='normal')

            for child in chAllFrame.winfo_children():
                child.configure(state='disable')


        def buttonAllFunction():
            ch1EnableCheckVal.set(False)
            for child in ch1Frame.winfo_children():
                child.configure(state='disable')

            ch2EnableCheckVal.set(False)
            for child in ch2Frame.winfo_children():
                child.configure(state='disable')

            ch3EnableCheckVal.set(False)
            for child in ch3Frame.winfo_children():
                child.configure(state='disable')

            ch4EnableCheckVal.set(False)
            for child in ch4Frame.winfo_children():
                child.configure(state='disable')

            ch5EnableCheckVal.set(False)
            for child in ch5Frame.winfo_children():
                child.configure(state='disable')

            ch6EnableCheckVal.set(False)
            for child in ch6Frame.winfo_children():
                child.configure(state='disable')

            ch7EnableCheckVal.set(False)
            for child in ch7Frame.winfo_children():
                child.configure(state='disable')

            ch8EnableCheckVal.set(False)
            for child in ch8Frame.winfo_children():
                child.configure(state='disable')

            for child in chAllFrame.winfo_children():
                child.configure(state='normal')

# Button once Start is pressed ------------------------------------------------
        def buttonStartFunction():

            if(self.dev.port() == "none"):
                return

            self.dev.setChannel(0, ch1CurrentEntry.get(), ch1TimeEntry.get())
            self.dev.setChannel(1, ch2CurrentEntry.get(), ch2TimeEntry.get())
            self.dev.setChannel(2, ch3CurrentEntry.get(), ch3TimeEntry.get())
            self.dev.setChannel(3, ch4CurrentEntry.get(), ch4TimeEntry.get())
            self.dev.setChannel(4, ch5CurrentEntry.get(), ch5TimeEntry.get())
            self.dev.setChannel(5, ch6CurrentEntry.get(), ch6TimeEntry.get())
            self.dev.setChannel(6, ch7CurrentEntry.get(), ch7TimeEntry.get())
            self.dev.setChannel(7, ch8CurrentEntry.get(), ch8TimeEntry.get())

            self.dev.start()

# Button once Stop is pressed -------------------------------------------------
        def buttonStopFunction():
            if(self.dev.port() == "none"):
                return
            self.dev.stop()

# topFrame second thing
        topFrame.after(1000, oneSecondThing)

# Begin port connection frame --------------------------------------------------
        titlePortControl = Label(topFrame, text = "Channel Selection", width = 20, height = 3, background = "white")
        titlePortControl.grid(row=0, column=0, padx = 50, pady = 1)
        controlFrame =Frame(topFrame,width = 1, height = 1, background="white")
        controlFrame.grid(row=1,column=0,padx = 50,pady = 1)

        self.settings = PhotoImage(file="settings.png")
        self.original_settings = self.settings.subsample(15,15) # resize image using subsample
        buttonSingle = Button(controlFrame, text="   Single  ", image = self.original_settings, compound = "left", width = 90, height = 50, command=buttonSingleFunction, background = grisclaro_boton)
        buttonSingle.grid(row=0,column=0,padx = 1,pady = 1)

        self.solutions = PhotoImage(file="solutions.png")
        self.original_solutions = self.solutions.subsample(15,15) # resize image using subsample
        buttonAll = Button(controlFrame, text="    All  ", image = self.original_solutions, compound = "left", width = 90, height = 50,command=buttonAllFunction, background = grisclaro_boton)
        buttonAll.grid(row=0,column=1,padx = 1,pady = 1)

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
        buttonStop = Button(controlFrame, text="    Stop  ", image = self.original_stop, compound = "left", width = 90, height = 50,background = grisclaro_boton, command = buttonStopFunction)
        buttonStop.grid(row=0,column=1,padx = 1,pady = 1)

# TODO: create the 8 channels with loop ----------------------------------------
        channelBox = Frame(master = midFrame, width = 10, height = 10, background=grisclaro_linea)
        channelBox.grid(row=1,column=0,padx = 20, pady = 20)
        channelsFrame =Frame(channelBox, width = 250, height = 100, background=grisclaro_linea)
        channelsFrame.grid(row=1,column=1,padx = 1,pady = 1)
        channelsFrameAll =Frame(channelBox, width = 250, height = 100, background=grisclaro_linea)
        channelsFrameAll.grid(row=1,column=2,padx = 1,pady = 1)

#begin CH1 ---------------------------------------------------------------------

        def ch1EnableCheckFunction():

            if (ch1EnableCheckVal.get()):
                for child in ch1Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch1Frame.winfo_children():
                    child.configure(state='disable')

            ch1EnableCheck.configure(state='normal')

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
        ch1EnableCheckVal = BooleanVar(value=True)
        ch1EnableCheck = Checkbutton(ch1Frame, text="Enable", variable=ch1EnableCheckVal ,background=grismedio, command=ch1EnableCheckFunction)
        ch1EnableCheck.grid(row=0,column=5,padx = 1,pady = 1)
        ch1space = Label(ch1Frame, text="        ",background=grismedio).grid(row=0,column=6,padx = 1,pady = 1)

#begin CH2 ---------------------------------------------------------------------

        def ch2EnableCheckFunction():

            if (ch2EnableCheckVal.get()):
                for child in ch2Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch2Frame.winfo_children():
                    child.configure(state='disable')

            ch2EnableCheck.configure(state='normal')

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
        ch2EnableCheckVal = BooleanVar(value=True)
        ch2EnableCheck = Checkbutton(ch2Frame, text="Enable ", variable=ch2EnableCheckVal ,background=grismedio, command=ch2EnableCheckFunction)
        ch2EnableCheck.grid(row=1,column=5,padx = 1,pady = 1)
        ch2space = Label(ch2Frame, text="       ",background=grismedio).grid(row=1,column=6,padx = 1,pady = 1)

    #begin CH3 ---------------------------------------------------------------------

        def ch3EnableCheckFunction():

            if (ch3EnableCheckVal.get()):
                for child in ch3Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch3Frame.winfo_children():
                    child.configure(state='disable')

            ch3EnableCheck.configure(state='normal')

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
        ch3EnableCheckVal = BooleanVar(value=True)
        ch3EnableCheck = Checkbutton(ch3Frame, text="Enable ", variable = ch3EnableCheckVal,background=grismedio, command=ch3EnableCheckFunction)
        ch3EnableCheck.grid(row=2,column=5,padx = 1,pady = 1)
        ch3space = Label(ch3Frame, text="       ",background=grismedio).grid(row=2,column=6,padx = 1,pady = 1)

#begin CH4 ---------------------------------------------------------------------

        def ch4EnableCheckFunction():

            if (ch4EnableCheckVal.get()):
                for child in ch4Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch4Frame.winfo_children():
                    child.configure(state='disable')

            ch4EnableCheck.configure(state='normal')

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
        ch4EnableCheckVal = BooleanVar(value=True)
        ch4EnableCheck = Checkbutton(ch4Frame, text="Enable", variable = ch4EnableCheckVal,background=grismedio, command=ch4EnableCheckFunction)
        ch4EnableCheck.grid(row=3,column=5,padx = 1,pady = 1)
        ch4space = Label(ch4Frame, text="        ",background=grismedio).grid(row=3,column=6,padx = 1,pady = 1)

#begin CH5----------------------------------------------------------------------

        def ch5EnableCheckFunction():

            if (ch5EnableCheckVal.get()):
                for child in ch5Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch5Frame.winfo_children():
                    child.configure(state='disable')

            ch5EnableCheck.configure(state='normal')

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
        ch5EnableCheckVal = BooleanVar(value=True)
        ch5EnableCheck = Checkbutton(ch5Frame, text="Enable", variable = ch5EnableCheckVal,background=grismedio, command=ch5EnableCheckFunction)
        ch5EnableCheck.grid(row=0,column=5,padx = 1,pady = 1)
        ch5space = Label(ch5Frame, text="       ",background=grismedio).grid(row=0,column=6,padx = 1,pady = 1)

#begin CH6 ---------------------------------------------------------------------

        def ch6EnableCheckFunction():

            if (ch6EnableCheckVal.get()):
                for child in ch6Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch6Frame.winfo_children():
                    child.configure(state='disable')

            ch6EnableCheck.configure(state='normal')

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
        ch6EnableCheckVal = BooleanVar(value=True)
        ch6EnableCheck = Checkbutton(ch6Frame, text="Enable", variable = ch6EnableCheckVal,background=grismedio, command=ch6EnableCheckFunction)
        ch6EnableCheck.grid(row=1,column=5,padx = 1,pady = 1)
        ch6space = Label(ch6Frame, text="       ",background=grismedio).grid(row=1,column=6,padx = 1,pady = 1)

#begin CH7 ---------------------------------------------------------------------

        def ch7EnableCheckFunction():

            if (ch7EnableCheckVal.get()):
                for child in ch7Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch7Frame.winfo_children():
                    child.configure(state='disable')

            ch7EnableCheck.configure(state='normal')

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
        ch7EnableCheckVal = BooleanVar(value=True)
        ch7EnableCheck = Checkbutton(ch7Frame, text="Enable", variable = ch7EnableCheckVal,background=grismedio, command=ch7EnableCheckFunction)
        ch7EnableCheck.grid(row=2,column=5,padx = 1,pady = 1)
        ch7space = Label(ch7Frame, text="       ",background=grismedio).grid(row=2,column=6,padx = 1,pady = 1)

#begin CH8 ---------------------------------------------------------------------

        def ch8EnableCheckFunction():

            if (ch8EnableCheckVal.get()):
                for child in ch8Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch8Frame.winfo_children():
                    child.configure(state='disable')

            ch8EnableCheck.configure(state='normal')

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
        ch8EnableCheckVal = BooleanVar(value=True)
        ch8EnableCheck = Checkbutton(ch8Frame, text="Enable", variable = ch8EnableCheckVal,background=grismedio, command=ch8EnableCheckFunction)
        ch8EnableCheck.grid(row=3,column=5,padx = 1,pady = 1)
        ch8space = Label(ch8Frame, text="       ",background=grismedio).grid(row=3,column=6,padx = 1,pady = 1)

        chAllspace1 = Label(channelsFrameAll, text="                       ",background=grismedio).grid(row=0,column=0,padx = 1,pady = 1)
        chAllspace2 = Label(channelsFrameAll, text="                       ",background=grismedio).grid(row=3,column=0,padx = 1,pady = 1)
        chAllLabel = Label(channelsFrameAll, text="      All CH     ",background=grismedio)
        chAllLabel.grid(row=1,column=0,padx = 1,pady = 1)
        chAllFrame = Frame(channelsFrameAll,background=grismedio)
        chAllFrame.grid(row=2,column=0,padx = 1,pady = 1)
        ch1CurrentEntry = Entry(chAllFrame, width=6)
        ch1CurrentEntry.grid(row=0,column=0,padx = 1,pady = 1)
        Label(chAllFrame, text="uA   ",background=grismedio).grid(row=0,column=1,padx = 1,pady = 1)
        ch1TimeEntry = Entry(chAllFrame, width=6)
        ch1TimeEntry.grid(row=1,column=0,padx = 1,pady = 1)
        Label(chAllFrame, text="min").grid(row=1,column=1,padx = 1,pady = 1)

#Data Table box ---- -----------------------------------------------------------
        box_graphs = Frame(midFrame, width = 400, height = 300, background=grismedio)
        box_graphs.grid(row=2, column=0, padx=19, pady=1)

        box_graphsLabel = Frame(box_graphs, width = 400, height = 1, background="#ffffff")
        box_graphsLabel.grid(row=0, column=0, padx=1, pady=1)

        ch1List = Label(box_graphsLabel, text="CH1",background="#ffffff")
        ch1List.grid(row=0,column=0,padx = 23,pady = 1)

        ch2List = Label(box_graphsLabel, text="CH2",background="#ffffff")
        ch2List.grid(row=0,column=1,padx = 23,pady = 1)

        ch3List = Label(box_graphsLabel, text="CH3",background="#ffffff")
        ch3List.grid(row=0,column=2,padx = 23,pady = 1)

        ch4List = Label(box_graphsLabel, text="CH4",background="#ffffff")
        ch4List.grid(row=0,column=3,padx = 23,pady = 1)

        ch5List = Label(box_graphsLabel, text="CH5",background="#ffffff")
        ch5List.grid(row=0,column=4,padx = 23,pady = 1)

        ch6List = Label(box_graphsLabel, text="CH6",background="#ffffff")
        ch6List.grid(row=0,column=5,padx = 23,pady = 1)

        ch7List = Label(box_graphsLabel, text="CH7",background="#ffffff")
        ch7List.grid(row=0,column=6,padx = 23,pady = 1)

        ch8List = Label(box_graphsLabel, text="CH8",background="#ffffff")
        ch8List.grid(row=0,column=7,padx = 23,pady = 1)

        ch_columns = Canvas(box_graphs, width = 605,height = 345, background="#ffffff")
        ch_columns.grid(row=1,column=0,rowspan = 100)
        ch_columns.texty = 0

        scroll = Scrollbar(box_graphs, orient='vertical', command = ch_columns.yview)
        scroll.grid(row = 0, column = 2, rowspan = 100, sticky = 'ns')
        #ch_columns.config(yscrollcommand = scroll.set)

        dataFrame = Frame(ch_columns, bg='white')
        ch_columns.create_window((10,0),window=dataFrame,anchor='nw')

#Export Excel -----------------------------------------------------------------
        exportExcel = Frame(midFrame, width = 50, height = 50, background=grismedio)
        exportExcel.grid(row=2,column=1,padx = 1,pady = 1)

        def write_Excel():
            file = filedialog.asksaveasfile(defaultextension='.xls',filetypes=[("Excel file",".xls"),("CSV file",".csv")])
            filetext = str("hola")
            file.write(filetext)
            file.close()

        self.excelImage = PhotoImage(file="excel.png")
        self.original_excelImage = self.excelImage.subsample(55,55) # resize image using subsample
        buttonReExcel = Button(exportExcel, text="    Excel ", image = self.original_excelImage, compound = tk.LEFT,command=lambda: write_Excel(),height = 50, width = 100,background=grismedio)
        buttonReExcel.grid(row=0,column=0,padx = 31, pady = 1)


#Finish ------------------------------------------------------------------------
        return
