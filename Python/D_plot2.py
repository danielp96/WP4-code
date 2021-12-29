import serial
import matplotlib.pyplot as plt
import numpy as np

connected = False

comPort = 'COM6'        

ser = serial.Serial(comPort, 9600)    # Sets up serial connection (make sure baud rate is correct - matches Arduino)

while not connected:
    serin = ser.read()
    connected = True

plt.ion()                               # Sets plot to animation mode


fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
fig4 = plt.figure()
fig5 = plt.figure()
fig6 = plt.figure()
fig7 = plt.figure()
fig8 = plt.figure()

ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)
ax3 = fig3.add_subplot(111)
ax4 = fig4.add_subplot(111)
ax5 = fig5.add_subplot(111)
ax6 = fig6.add_subplot(111)
ax7 = fig7.add_subplot(111)
ax8 = fig8.add_subplot(111)

length = 500                             # Determines length of data taking session (in data points); length/10 = seconds

w = [0]*length                          # Create empty variable of length of test
x = [0]*length               
y = [0]*length
z = [0]*length
a = [0]*length                          # Create empty variable of length of test
b = [0]*length               
c = [0]*length
d = [0]*length

wline, = ax1.plot(w)                    # Sets up future lines to be modified
xline, = ax2.plot(x)                    
yline, = ax3.plot(y)
zline, = ax4.plot(z)
aline, = ax1.plot(w)                    # Sets up future lines to be modified
bline, = ax2.plot(x)                    
cline, = ax3.plot(y)
dline, = ax4.plot(z)



plt.ylim(0,255)                       # Sets the y axis limits - 16 bits resolution

for i in range(length):                 # While you are taking data
    data = ser.readline()               # Reads until it gets a carriage return (/n).
    sep = data.split()                  # Splits string into a list at the tabs

    w.append(int(sep[0]))               # Add new values as int to current list
    x.append(int(sep[1]))   
    y.append(int(sep[2]))
    z.append(int(sep[3]))
    a.append(int(sep[4]))               # Add new values as int to current list
    b.append(int(sep[5]))   
    c.append(int(sep[6]))
    d.append(int(sep[7]))

    del w[0]
    del x[0]
    del y[0]
    del z[0]
    del a[0]
    del b[0]
    del c[0]
    del d[0]

    wline.set_xdata(np.arange(len(w)))  # Sets wdata to new list length  
    xline.set_xdata(np.arange(len(x)))  
    yline.set_xdata(np.arange(len(y)))  
    zline.set_xdata(np.arange(len(z)))
    aline.set_xdata(np.arange(len(a)))  # Sets wdata to new list length  
    bline.set_xdata(np.arange(len(b)))  
    cline.set_xdata(np.arange(len(c)))  
    dline.set_xdata(np.arange(len(d)))  

    wline.set_ydata(w)                  # Sets ydata to new lists 
    xline.set_ydata(x)                 
    yline.set_ydata(y)
    zline.set_ydata(z)
    aline.set_ydata(a)                  # Sets ydata to new lists 
    bline.set_ydata(b)                 
    cline.set_ydata(c)
    dline.set_ydata(d)

    print (i)
    print (sep)


    plt.pause(0.001)                   
    ax1.grid(True)
    fig1.canvas.draw()                         # Draws new plot


    plt.pause(0.001)                   
    ax2.grid(True)
    fig2.canvas.draw()                         # Draws new plot


    plt.pause(0.001)                   
    ax3.grid(True)
    fig3.canvas.draw()                         # Draws new plot


    plt.pause(0.001)                   
    ax4.grid(True)
    fig4.canvas.draw()                         # Draws new plot

    plt.pause(0.001)                   
    ax5.grid(True)
    fig5.canvas.draw()                         # Draws new plot


    plt.pause(0.001)                   
    ax6.grid(True)
    fig6.canvas.draw()                         # Draws new plot


    plt.pause(0.001)                   
    ax7.grid(True)
    fig7.canvas.draw()                         # Draws new plot


    plt.pause(0.001)                   
    ax8.grid(True)
    fig8.canvas.draw()                         # Draws new plot

    

plt.show()
