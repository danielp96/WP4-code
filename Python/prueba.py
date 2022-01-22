import tkinter as tk
root = tk.Tk()

Photoshop = tk.Button(root, text = 'Photoshop',
                      fg = 'white',  #color letra
                      bg = '#001d26',# color fondo boton
                      bd = 25,
                      highlightthickness = 1,
                      highlightcolor = 'red',
                      highlightbackground = "red",
                      borderwidth = 1) #borde boton

Photoshop.pack()
root.mainloop()
