import serial

arduino_port = "COM6" #serial port of Arduino
baud = 9600 #arduino uno runs at 9600 baud
fileName="analog-data1.csv" #name of the CSV file generated
samples = 10
print_labels = False

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
file = open(fileName, "a")
print("Created file")

line = 0

while line <= samples:
    if print_labels:
        if line == 0:
            print("Headers, Headhers1")
        else:
            print ("Line " + str(line)+ ": writing")

    #display the data to the terminal
    getData=str(ser.readline())
    data=getData[0:][:-2]
    print(data)

    #add the data to the file
    file = open(fileName, "a") #append the data to the file
    file.write(data + "\n") #write data with a newline
    line = line +1
    

#close out the file
file.close()
