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

        global y, t1, t2, t3, t4, t5, t6, t7, t8
        global i1, i2, i3, i4, i5, i6, i7, i8, sum
        y = 0
        t1 = 0
        t2 = 0
        t3 = 0
        t4 = 0
        t5 = 0
        t6 = 0
        t7 = 0
        t8 = 0
        sum = 0




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





        def buttonAllFunction():

            if (ch1MasterEnableCheckVal.get()):
                for child in ch1Frame.winfo_children():
                    child.configure(state='normal')
                for child in ch2Frame.winfo_children():
                    child.configure(state='normal')
                for child in ch3Frame.winfo_children():
                    child.configure(state='normal')
                for child in ch4Frame.winfo_children():
                    child.configure(state='normal')
                for child in ch5Frame.winfo_children():
                    child.configure(state='normal')
                for child in ch6Frame.winfo_children():
                    child.configure(state='normal')
                for child in ch7Frame.winfo_children():
                    child.configure(state='normal')
                for child in ch8Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch1Frame.winfo_children():
                    child.configure(state='disable')
                for child in ch2Frame.winfo_children():
                    child.configure(state='disable')
                for child in ch3Frame.winfo_children():
                    child.configure(state='disable')
                for child in ch4Frame.winfo_children():
                    child.configure(state='disable')
                for child in ch5Frame.winfo_children():
                    child.configure(state='disable')
                for child in ch6Frame.winfo_children():
                    child.configure(state='disable')
                for child in ch7Frame.winfo_children():
                    child.configure(state='disable')
                for child in ch8Frame.winfo_children():
                    child.configure(state='disable')

            ch1EnableCheck.configure(state='normal')
            ch2EnableCheck.configure(state='normal')
            ch3EnableCheck.configure(state='normal')
            ch4EnableCheck.configure(state='normal')
            ch5EnableCheck.configure(state='normal')
            ch6EnableCheck.configure(state='normal')
            ch7EnableCheck.configure(state='normal')
            ch8EnableCheck.configure(state='normal')




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
        buttonStart = Button(controlFrame, text="   Start  ", image = self.original_play, compound = "left", width = 90, height = 50, command = buttonStartFunction,background = grisclaro_boton)
        buttonStart.grid(row=0,column=0,padx = 1,pady = 1)

        self.stop = PhotoImage(file="stop.png")
        self.original_stop = self.stop.subsample(15,15) # resize image using subsample
        buttonStop = Button(controlFrame, text="    Stop  ", image = self.original_stop, compound = "left", width = 90, height = 50,background = grisclaro_boton)
        buttonStop.grid(row=0,column=1,padx = 1,pady = 1)


# TODO: create the 8 channels with loop ----------------------------------------
        channelBox = Frame(master = midFrame, width = 10, height = 10, background=grisclaro_linea)
        channelBox.grid(row=1,column=0,padx = 20, pady = 20)

        channelsFrameBox =Frame(channelBox, width = 250, height = 100, background=grisclaro_linea)
        channelsFrameBox.grid(row=1,column=1,padx = 1,pady = 1)

        channelsFrame1 =Frame(channelsFrameBox, width = 250, height = 100, background=grisclaro_linea)
        channelsFrame1.grid(row=1,column=1,padx = 1,pady = 1)

        def cal_sum():
            i1=int(ch1CurrentEntry.get())
            i2=int(ch2CurrentEntry.get())
            i3=int(ch3CurrentEntry.get())
            i4=int(ch4CurrentEntry.get())
            i5=int(ch5CurrentEntry.get())
            i6=int(ch6CurrentEntry.get())
            i7=int(ch7CurrentEntry.get())
            i8=int(ch8CurrentEntry.get())

            t1=int(ch1TimeEntry.get())
            t2=int(ch2TimeEntry.get())
            t3=int(ch3TimeEntry.get())
            t4=int(ch4TimeEntry.get())
            t5=int(ch5TimeEntry.get())
            t6=int(ch6TimeEntry.get())
            t7=int(ch7TimeEntry.get())
            t8=int(ch8TimeEntry.get())
            sum=t1+t2+t2+t5+t5+t6+t7+t8

            print(i1)
            print(type(i1))

            return i1, i2, i3, i4, i5, i6, i7, i8, t1, t2, t3, t4, t5, t6, t7, t8, sum





#begin CH1 ---------------------------------------------------------------------

        def ch1EnableCheckFunction():

            if (ch1EnableCheckVal.get()):
                for child in ch1Frame.winfo_children():
                    child.configure(state='normal')
            else:
                for child in ch1Frame.winfo_children():
                    child.configure(state='disable')

            ch1EnableCheck.configure(state='normal')

        ch1Frame = Frame(channelsFrame1,background=grismedio)
        ch1Frame.grid(row=0,column=0,padx = 1,pady = 1)
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

        ch2Frame = Frame(channelsFrame1,background=grismedio)
        ch2Frame.grid(row=1,column=0,padx = 1,pady = 1)
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

        ch3Frame = Frame(channelsFrame1,background=grismedio)
        ch3Frame.grid(row=2,column=0,padx = 1,pady = 1)
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

        ch4Frame = Frame(channelsFrame1,background=grismedio)
        ch4Frame.grid(row=3,column=0,padx = 1,pady = 1)
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

        ch5Frame = Frame(channelsFrame1,background=grismedio)
        ch5Frame.grid(row=0,column=1,padx = 1,pady = 1)
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

        ch6Frame = Frame(channelsFrame1,background=grismedio)
        ch6Frame.grid(row=1,column=1,padx = 1,pady = 1)
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

        ch7Frame = Frame(channelsFrame1,background=grismedio)
        ch7Frame.grid(row=2,column=1,padx = 1,pady = 1)
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

        ch8Frame = Frame(channelsFrame1,background=grismedio)
        ch8Frame.grid(row=3,column=1,padx = 1,pady = 1)
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

        ch1MasterEnableCheckVal = BooleanVar(value=True)
        ch1MasterEnableCheck = Checkbutton(channelsFrameBox, text="Enable CH1", variable=ch1MasterEnableCheckVal ,background=grismedio, command=buttonAllFunction)
        ch1MasterEnableCheck.grid(row=1,column=2,padx = 1,pady = 1)





#ch1CurrentEntry
#ch1TimeEntry

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
        x = np.linspace(1, 2 * np.pi, 400)
        y1_amp = 0.7*x-4 #Channel0Array
        y2_amp = np.log(x)
        y3_amp = -1*np.log(x)-2
        y4_amp = -1*x
        y5_amp = 0.7*x-4
        y6_amp = np.log(x)
        y7_amp = -1*np.log(x)-2
        y8_amp = -1*x

        y1_vol = np.log(x)
        y2_vol = x
        y3_vol = np.exp(x)/500
        y4_vol = -0.9*x+0.9
        y5_vol = np.log(x)
        y6_vol = x
        y7_vol = np.exp(x)/500
        y8_vol = -0.9*x+0.9


        fig1 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig1.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs1 = fig1.add_gridspec(2, 1, hspace=0, wspace=0)
        (ax1), (ax2) = gs1.subplots(sharex='col', sharey='row')
        ax1.plot(x, y1_amp)
        ax2.plot(x, y1_vol, 'tab:red')

        fig2 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig2.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs2 = fig2.add_gridspec(2, 1, hspace=0, wspace=0)
        (ax1), (ax2) = gs2.subplots(sharex='col', sharey='row')
        ax1.plot(x, y2_amp)
        ax2.plot(x, y2_vol, 'tab:red')

        fig3 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig3.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs3 = fig3.add_gridspec(2, 1, hspace=0, wspace=0)
        (ax1), (ax2) = gs3.subplots(sharex='col', sharey='row')
        ax1.plot(x, y3_amp)
        ax2.plot(x, y3_vol, 'tab:red')

        fig4 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig4.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs4 = fig4.add_gridspec(2, 1, hspace=0, wspace=0)
        (ax1), (ax2) = gs4.subplots(sharex='col', sharey='row')
        ax1.plot(x, y4_amp)
        ax2.plot(x, y4_vol, 'tab:red')

        fig5 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig5.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs5 = fig5.add_gridspec(2, 1, hspace=0, wspace=0)
        (ax1), (ax2) = gs5.subplots(sharex='col', sharey='row')
        ax1.plot(x, y5_amp)
        ax2.plot(x, y5_vol, 'tab:red')

        fig6 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig6.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs6 = fig6.add_gridspec(2, 1, hspace=0, wspace=0)
        (ax1), (ax2) = gs6.subplots(sharex='col', sharey='row')
        ax1.plot(x, y6_amp)
        ax2.plot(x, y6_vol, 'tab:red')

        fig7 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig7.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs7 = fig7.add_gridspec(2, 1, hspace=0, wspace=0)
        (ax1), (ax2) = gs7.subplots(sharex='col', sharey='row')
        ax1.plot(x, y7_amp)
        ax2.plot(x, y7_vol, 'tab:red')

        fig8 = plt.figure(figsize = (7, 5.3), dpi = 70)
        fig8.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs8 = fig8.add_gridspec(2, 1, hspace=0, wspace=0)
        (ax1), (ax2) = gs8.subplots(sharex='col', sharey='row')
        ax1.plot(x, y8_amp)
        ax2.plot(x, y8_vol, 'tab:red')


        #fig14 = plt.figure(figsize = (7, 5.3), dpi = 70)
        #fig14.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        #gs14 = fig14.add_gridspec(2, 2, hspace=0, wspace=0)
        #(ax1, ax2), (ax3, ax4) = gs14.subplots(sharex='col', sharey='row')
        #ax1.plot(x, y1_amp)
        #ax1.plot(x, y1_vol, 'tab:red')

        #ax2.plot(x, y2_amp)
        #ax2.plot(x, y2_vol, 'tab:red')

        #ax3.plot(x, y3_amp)
        #ax3.plot(x, y3_vol, 'tab:red')

        #ax4.plot(x, y4_amp)
        #ax4.plot(x, y4_vol, 'tab:red')

        #fig58 = plt.figure(figsize = (7, 5.3), dpi = 70)
        #fig58.subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        #gs58 = fig58.add_gridspec(2, 2, hspace=0, wspace=0)
        #(ax5, ax6), (ax7, ax8) = gs58.subplots(sharex='col', sharey='row')
        #ax5.plot(x, y5_amp)
        #ax5.plot(x, y5_vol, 'tab:red')

        #ax6.plot(x, y6_amp)
        #ax6.plot(x, y6_vol, 'tab:red')

        #ax7.plot(x, y7_amp)
        #ax7.plot(x, y7_vol, 'tab:red')

        #ax8.plot(x, y8_amp)
        #ax8.plot(x, y8_vol, 'tab:red')


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

        #canvas14 = FigureCanvasTkAgg(fig14, master = window14)
        #canvas14.get_tk_widget().grid(row=0,column=0)

        #canvas58 = FigureCanvasTkAgg(fig58, master = window58)
        #canvas58.get_tk_widget().grid(row=0,column=0)

#Export Excel & JPG -- ---------------------------------------------------------
        exportExcel = Frame(midFrame, width = 62, height = 50, background=grismedio)
        exportExcel.grid(row=2,column=1,padx = 1,pady = 1)

        def write_Excel():
            file = filedialog.asksaveasfile(defaultextension='.xls',filetypes=[("Excel file",".xls"),("CSV file",".csv")])
            filetext = str("hola")
            file.write(filetext)
            file.close()

        def write_graph():
            cal_sum()
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

        # graphImage







        x_show = np.linspace(1, 5, sum)
        y_show = 0.7*x_show-4

        fig_show = plt.figure(figsize = (9, 5.1), dpi = 70)
        fig_show .subplots_adjust(left=0.05, bottom=0.0, right=0.995, top=0.995, wspace=1, hspace=1)
        gs_show = fig_show.add_gridspec(1, 1, hspace=0, wspace=0)
        (ax_show) = gs_show.subplots(sharex='col', sharey='row')
        ax_show.plot(x_show, y_show)


        def show_graph():

            i1=float(ch1CurrentEntry.get())
            i2=float(ch2CurrentEntry.get())
            i3=float(ch3CurrentEntry.get())
            i4=float(ch4CurrentEntry.get())
            i5=float(ch5CurrentEntry.get())
            i6=float(ch6CurrentEntry.get())
            i7=float(ch7CurrentEntry.get())
            i8=float(ch8CurrentEntry.get())

            t1=float(ch1TimeEntry.get())
            t2=float(ch2TimeEntry.get())
            t3=float(ch3TimeEntry.get())
            t4=float(ch4TimeEntry.get())
            t5=float(ch5TimeEntry.get())
            t6=float(ch6TimeEntry.get())
            t7=float(ch7TimeEntry.get())
            t8=float(ch8TimeEntry.get())

            t1 = t1
            t2 = t2 + t1
            t3 = t3 + t2
            t4 = t4 + t3
            t5 = t5 + t4
            t6 = t6 + t5
            t7 = t7 + t6
            t8 = t8 + t7

            def f1(x):
                if x < t1:
                    return i1
                if (x >= t1 and x < t2):
                    return i2
                if (x >= t2 and x < t3):
                    return i3
                if (x >= t3 and x < t4):
                    return i4
                if (x >= t4 and x < t5):
                    return i5
                if (x >= t5 and x < t6):
                    return i6
                if (x >= t6 and x < t7):
                    return i7
                if (x >= t7 and x < t8):
                    return i8

            print(type(t1))
            print(type(i1))
            print(t1)
            print(i1)

            x=np.linspace(0,10,100)

            f2 = np.vectorize(f1)
            y = f2(x)

            plt.close("all")
            plt.figure()
            plt.plot(x, y)
            plt.show()



        self.showChannel= PhotoImage(file="Pika3.png")
        self.original_showChannel = self.showChannel.subsample(10,10) # resize image using subsample
        buttonReExcel = Button(midFrame, text="    Show ", image = self.original_showChannel, compound = tk.LEFT,command=lambda: show_graph(),height = 50, width = 100,background=grismedio)
        buttonReExcel.grid(row=1,column=1,padx = 1, pady = 1)


#Finish ------------------------------------------------------------------------
        return
