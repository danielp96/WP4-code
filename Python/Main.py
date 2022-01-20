import tkinter as tk
from tkinter import *
from tkinter import ttk
import device
from G1_testInterface import windowPage1
from G2_testInterface import windowPage2
from G3_testInterface import windowPage3
#from page2 import Page2

class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        dev = device.Device()

        root.title("DC STIMULATOR")
        root.geometry("884x700")
        color_grisclaro = "#f5f4f6"
        color_azul = "#004080"
        root.configure(background=color_grisclaro)

        back_color = Frame(root, width = 30, height = 696, background = color_azul)
        back_color.grid(row=0, column=0, padx = 3, pady = 1)

        style = ttk.Style(root)
        style.configure('One.TNotebook.Tab',tabposition = 'n', padding = 18, font=('Calibri',12))

        my_notebook = ttk.Notebook(root,style='One.TNotebook')
        my_notebook.grid(row=0, column=1)

        window1 = windowPage1(my_notebook, dev)
        window2 = windowPage2(my_notebook, dev)
        window3 = windowPage3(my_notebook, dev)
        window4 = Frame(my_notebook, width = 710, height = 600)

        window1.test= "hola"

        my_notebook.add(window1, text="         Test Interface       ")
        my_notebook.add(window2, text="           Calibration        ")
        my_notebook.add(window3, text="       Simple Stimulation     ")
        my_notebook.add(window4, text="   Programmable Stimulation   ")

if __name__ == "__main__":
    root = tk.Tk()
    Main(root).grid(row=0, column=0)
    root.mainloop()
