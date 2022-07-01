import tkinter as tk
from tkinter import *
from tkinter import ttk
import device
from guilib import *
from G1_testInterface import windowPage1
from G2_testInterface import windowPage2
from G3_testInterface import windowPage3
from G4_testInterface import windowPage4
#from page2 import Page2

class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

# Tkinter things ------- --------------------------
        root.title("DC STIMULATOR")
        root.geometry("953x740")
        color_grisclaro = "#f5f4f6"
        color_azul = "#004080"
        top_color = "#f0f0f0"
        root.configure(background=color_grisclaro)
        grismedio = "#61697c"
        letter_color = "white"
        height_buttom = 3  # no image button size
        width_buttom = 12  # no image button size
        connectFrame = Frame(root, width = 1,height = 1, background=grismedio)
        connectFrame.grid(row=0,column=0,padx = 1,pady = 1)

# Device import  ------- --------------------------
        self.dev = device.Device()
        portList = refreshPortList()
        self.dev.detect()

# refresh port  ----------------------------------------------------------------
        def buttonRefreshPortFunction():
            portList = refreshPortList()
            portMenuValue.set('')
            portMenu['menu'].delete(0, 'end')
            for port in portList:
                portMenu['menu'].add_command(label=port, command=tk._setit(portMenuValue, port))

            portMenuValue.set(portList[0]) # default value

# Begin port connection frame -------------------------------------------------
        portFrame = Frame(connectFrame, width = 1, height = 1, background=grismedio)
        portFrame.grid(row=0,column=0,padx = 1, pady = 1)
        space = Frame(connectFrame, width = 1, height = 500, background=grismedio)
        space.grid(row=1,column=0,padx = 1, pady = 1)

        portMenuValue = StringVar()
        portMenuValue.set(portList[0]) # default value, background=color
        portMenu = OptionMenu(portFrame, portMenuValue, *portList)
        portMenu.config(background = grismedio, borderwidth = 1,fg = letter_color,height = height_buttom,width=8)
        portMenu.grid(row=0,column=0,padx = 1, pady = 1)

        def buttonConnectFunction():
            self.dev.port(portMenuValue.get())
            if (self.dev.ping()):
                #set some indicator
                pass
            else:
                pass

        buttonRefreshPort = Button(portFrame, text="Refresh", command=buttonRefreshPortFunction, height = height_buttom, width = width_buttom,background = grismedio, fg = letter_color)
        buttonRefreshPort.grid(row=1,column=0,padx = 0, pady = 0)
        buttonDetectPort = Button(portFrame, text="Auto Detect",height = height_buttom, width = width_buttom,background = grismedio, command=self.dev.detect, fg = letter_color)
        buttonDetectPort.grid(row=2,column=0,padx = 0, pady = 0)
        buttonConnectPort = Button(portFrame, text="Connect", height = height_buttom, width = width_buttom,background = grismedio, command = buttonConnectFunction, fg = letter_color)
        buttonConnectPort.grid(row=3,column=0,padx = 0, pady = 0)
        spacePortFrame = LabelFrame(connectFrame, text="     ").grid(row=0,column=1,padx = 1,pady = 1) # blank space between frames

        style = ttk.Style(root)
        style.configure('One.TNotebook.Tab',tabposition = 'n', padding = 18, font=('Calibri',12))

        my_notebook = ttk.Notebook(root,style='One.TNotebook')
        my_notebook.grid(row=0, column=1)

        window1 = windowPage1(my_notebook, self.dev)
        window2 = windowPage2(my_notebook, self.dev)
        window3 = windowPage3(my_notebook, self.dev)
        window4 = windowPage4(my_notebook, self.dev)

        my_notebook.add(window1, text="         Test Interface       ")
        my_notebook.add(window2, text="           Calibration        ")
        my_notebook.add(window3, text="       Simple Stimulation     ")
        my_notebook.add(window4, text="   Programmable Stimulation   ")

if __name__ == "__main__":
    root = tk.Tk()
    Main(root).grid(row=0, column=0)
    root.mainloop()
