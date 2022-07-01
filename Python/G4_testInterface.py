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
import numpy as np
from tkinter import ttk
from PIL import ImageTk
import PySimpleGUI as sg

class windowPage4(tk.Frame):
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
        channelBox = Frame(master = midFrame, width = 250, height = 100, background=grisclaro_linea)
        channelBox.grid(row=1,column=0,padx = 0, pady = 10)


        #style1 = ttk.Style(channelBox)
        #style1.configure('One.TNotebook.Tab',tabposition = 'n', padding = 1, font=('Calibri',8))

        #my_notebook1 = ttk.Notebook(channelBox,style='One.TNotebook')
        my_notebook1 = ttk.Notebook(channelBox)
        my_notebook1.grid(row=0, column=0)

        window1 = ttk.Frame(my_notebook1)
        window2 = ttk.Frame(my_notebook1)
        window3 = ttk.Frame(my_notebook1)
        window4 = ttk.Frame(my_notebook1)
        window5 = ttk.Frame(my_notebook1)
        window6 = ttk.Frame(my_notebook1)
        window7 = ttk.Frame(my_notebook1)
        window8 = ttk.Frame(my_notebook1)

        my_notebook1.add(window1, text="    CH1   ")
        my_notebook1.add(window2, text="    CH2   ")
        my_notebook1.add(window3, text="    CH3   ")
        my_notebook1.add(window4, text="    CH4   ")
        my_notebook1.add(window5, text="    CH5   ")
        my_notebook1.add(window6, text="    CH6   ")
        my_notebook1.add(window7, text="    CH7   ")
        my_notebook1.add(window8, text="    CH8   ")

        input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]

        ttk.Label(window1, text ="Tabla de tiempos y corrientes con 2 columnas y varias filas").grid(column = 0,  row = 0, padx = 130, pady = 45)


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

        plt.style.use('ggplot')

        x = np.linspace(0, 2 * np.pi, 400)
        y = np.sin(x ** 2)

        fig = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        #gs = fig.add_gridspec(4, 2, hspace=0, wspace=0)
        #(ax1, ax2), (ax3, ax4),(ax5, ax6), (ax7, ax8) = gs.subplots(sharex='col', sharey='row')
        gs = fig.add_gridspec(2, 1, hspace=0, wspace=0)
        (ax1), (ax5) = gs.subplots(sharex='col', sharey='row')
        ax1.plot(x, y)
        ax5.plot(x, y**2, 'tab:orange')
    

        #for ax in axs.flat:
        #    ax.label_outer()

        #fig1, axis = plt.subplots(4, 2)


        canvas1 = FigureCanvasTkAgg(fig, master = GraphFrame)
        canvas1.get_tk_widget().grid(row=0,column=0)

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
