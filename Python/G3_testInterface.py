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

class windowPage3(tk.Frame):
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
        buttonStart = Button(controlFrame, text="   Start ", image = self.original_play, compound = "left", width = 90, height = 50, command = buttonStartFunction,background = grisclaro_boton)
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







#Data Graph box ---- -----------------------------------------------------------
        box_graphs = Frame(midFrame, width = 400, height = 300, background=grismedio)
        box_graphs.grid(row=2, column=0, padx=19, pady=1)

        style = ttk.Style(channelBox)
        style.configure('Two.TNotebook',tabposition = 'en', padding = [1,1], font=('Calibri',12))
        current_theme =style.theme_use()
        style.theme_settings(current_theme, {"TNotebook.Tab": {"configure": {"padding": [14, 8]}}})

        my_notebook2 = ttk.Notebook(box_graphs,style='Two.TNotebook')
        #my_notebook2 = ttk.Notebook(box_graphs)
        my_notebook2.grid(row=0, column=0)

        window1  = ttk.Frame(my_notebook2)
        window2  = ttk.Frame(my_notebook2)
        window3  = ttk.Frame(my_notebook2)
        window4  = ttk.Frame(my_notebook2)
        window14 = ttk.Frame(my_notebook2)
        window5  = ttk.Frame(my_notebook2)
        window6  = ttk.Frame(my_notebook2)
        window7  = ttk.Frame(my_notebook2)
        window8  = ttk.Frame(my_notebook2)
        window58 = ttk.Frame(my_notebook2)

        my_notebook2.add(window1, text="    CH1   ")
        my_notebook2.add(window2, text="    CH2   ")
        my_notebook2.add(window3, text="    CH3   ")
        my_notebook2.add(window4, text="    CH4   ")
        my_notebook2.add(window14,text="     1-4    ")
        my_notebook2.add(window5, text="    CH5   ")
        my_notebook2.add(window6, text="    CH6   ")
        my_notebook2.add(window7, text="    CH7   ")
        my_notebook2.add(window8, text="    CH8   ")
        my_notebook2.add(window58,text="     5-8    ")


        #grismedio_boton = "#f0f0f0"

#Graph Example -----------------------------------------------------------------
        # the figure that will contain the plot

        #plt.style.use('ggplot')
        x = np.linspace(0, 2 * np.pi, 400)
        y1 = np.exp(x)
        y2 = 150*x
        y3 = -1*np.log(x)
        y4 = -1*x
        y5 = np.log(x)
        y6 = x
        y7 = np.exp(x)
        y8 = -50*x+500
        #y2 = np.random(x ** 2)

        fig14 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig14.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs14 = fig14.add_gridspec(2, 2, hspace=0, wspace=0)
        (ax1, ax2), (ax3, ax4) = gs14.subplots(sharex='col', sharey='row')
        ax1.plot(x, y1)
        ax2.plot(x, y2, 'tab:orange')
        ax3.plot(x ,y3, 'tab:green')
        ax4.plot(x ,y4, 'tab:red')

        fig58 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig58.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs58 = fig58.add_gridspec(2, 2, hspace=0, wspace=0)
        (ax5, ax6), (ax7, ax8) = gs58.subplots(sharex='col', sharey='row')
        ax5.plot(x, y5)
        ax6.plot(x, y6, 'tab:orange')
        ax7.plot(x ,y7, 'tab:green')
        ax8.plot(x ,y8, 'tab:red')

        fig1 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig1.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs1 = fig1.add_gridspec(1, 1, hspace=0, wspace=0)
        (ax1) = gs1.subplots(sharex='col', sharey='row')
        ax1.plot(x, y1)

        fig2 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig2.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs2 = fig2.add_gridspec(1, 1, hspace=0, wspace=0)
        (ax2) = gs2.subplots(sharex='col', sharey='row')
        ax2.plot(x, y2, 'tab:orange')

        fig3 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig3.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs3 = fig3.add_gridspec(1, 1, hspace=0, wspace=0)
        (ax3) = gs3.subplots(sharex='col', sharey='row')
        ax3.plot(x, y3, 'tab:green')

        fig4 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig4.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs4 = fig4.add_gridspec(1, 1, hspace=0, wspace=0)
        (ax4) = gs4.subplots(sharex='col', sharey='row')
        ax4.plot(x, y4, 'tab:red')

        fig5 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig5.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs5 = fig5.add_gridspec(1, 1, hspace=0, wspace=0)
        (ax5) = gs5.subplots(sharex='col', sharey='row')
        ax5.plot(x, y5)

        fig6 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig6.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs6 = fig6.add_gridspec(1, 1, hspace=0, wspace=0)
        (ax6) = gs6.subplots(sharex='col', sharey='row')
        ax6.plot(x, y6, 'tab:orange')

        fig7 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig7.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs7 = fig7.add_gridspec(1, 1, hspace=0, wspace=0)
        (ax7) = gs7.subplots(sharex='col', sharey='row')
        ax7.plot(x, y7, 'tab:green')

        fig8 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig8.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs8 = fig8.add_gridspec(1, 1, hspace=0, wspace=0)
        (ax8) = gs8.subplots(sharex='col', sharey='row')
        ax8.plot(x, y8, 'tab:red')

        canvas1 = FigureCanvasTkAgg(fig1, master = window1)
        canvas1.get_tk_widget().grid(row=0,column=0)

        canvas2 = FigureCanvasTkAgg(fig2, master = window2)
        canvas2.get_tk_widget().grid(row=0,column=0)

        canvas3 = FigureCanvasTkAgg(fig3, master = window3)
        canvas3.get_tk_widget().grid(row=0,column=0)

        canvas4 = FigureCanvasTkAgg(fig4, master = window4)
        canvas4.get_tk_widget().grid(row=0,column=0)

        canvas5 = FigureCanvasTkAgg(fig5, master = window5)
        canvas5.get_tk_widget().grid(row=0,column=0)

        canvas6 = FigureCanvasTkAgg(fig6, master = window6)
        canvas6.get_tk_widget().grid(row=0,column=0)

        canvas7 = FigureCanvasTkAgg(fig7, master = window7)
        canvas7.get_tk_widget().grid(row=0,column=0)

        canvas8 = FigureCanvasTkAgg(fig8, master = window8)
        canvas8.get_tk_widget().grid(row=0,column=0)

        canvas14 = FigureCanvasTkAgg(fig14, master = window14)
        canvas14.get_tk_widget().grid(row=0,column=0)

        canvas58 = FigureCanvasTkAgg(fig58, master = window58)
        canvas58.get_tk_widget().grid(row=0,column=0)

        #gs = fig.add_gridspec(4, 2, hspace=0, wspace=0)
        #(ax1, ax2), (ax3, ax4),(ax5, ax6), (ax7, ax8) = gs.subplots(sharex='col', sharey='row')
        #for ax in axs.flat:
        #    ax.label_outer()

        #fig1, axis = plt.subplots(4, 2)




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
