
# IMPORTANT
# TODO: add error checking if port can't be opened

import serial
import time
import datetime


def getPortList():

    import serial.tools.list_ports

    return [comport.device for comport in serial.tools.list_ports.comports()]


class Device:
    
    def __init__(self, baudrate=9600, port="none", logfile="", logEnabled=True):
        self.serial = serial.Serial()
        self.serial.baudrate = baudrate
        self.serial.port = port
        self.serial.timeout = 5
        self.logEnabled = logEnabled

        if (logfile == ""):
            self.logfile = '{:%Y-%m-%d}.log'.format(datetime.datetime.now())
        else:
            self.logfile = logfile

    def log(self, msg):

        if (self.logEnabled):
            file = open(self.logfile, 'a')
            file.write('{:%Y-%m-%d_%H:%M:%S}: '.format(datetime.datetime.now()) + msg + "\n")
            file.close()

    def detect(self):

        device_port = ""

        port_list = getPortList()

        self.log("Ports detected: " + str(port_list))

        # if no ports available
        if (len(port_list) == 0):
            return "none"

        for p in port_list:

            self.log("Checking port " + p)

            self.port(p)

            self.open()


            self.write("$PING:0")
            line = self.read()
        
            # arduino sends newlines as CRLF
            # include them when compring strings
            if (line == "PONG:0\r\n"):
                device_port = self.port()
                break
            else:
                device_port = "none"

            self.close()

        self.port(device_port)

        return device_port

    def port(self, port=""):

        if (port != ""):
            self.log("Port configured to " + port)
            self.serial.port = port

        return self.serial.port

    def write(self, msg):

        if (not self.serial.is_open):
            self.serial.open()
            time.sleep(2)

        self.serial.write(bytes(msg, 'utf-8'))

        self.log("Sent " + msg)


    def read(self):

        if (not self.serial.is_open):
            self.serial.open()
            time.sleep(2)

        line = self.serial.readline()

        self.log("Read " + str(line))

        line = line.decode("utf-8")


        return line;

    def close(self):
        self.serial.close()

    def open(self):
        self.serial.open()
        time.sleep(2) # wait requiered while port opens

    def start(self):
        self.write("$START:")
        ack = self.read()

        if (ack == "STARTED\x0D\x0A"):
            return True
        else:
            return False


    def stop(self):
        self.write("$STOP:")
        ack = self.read()

        if (ack == "STOPPED\x0D\x0A"):
            return True
        else:
            return False

    def setAllChannels(self, current, time):
        msg = "$SET_ALL:" + str(current) + "," + str(time) + ";"
        self.write(msg)
        ack = self.read()

        if (ack == "DONE, SET_ALL\x0D\x0A"):
            return True
        else:
            return False

    def setChannel(self, channel, current, time):
        msg = "$SET_ONE:" + str(channel) + "," + str(current) + "," + str(time) + ";"
        self.write(msg)
        ack = self.read()

        if (ack == "DONE, SET_ONE\x0D\x0A"):
            return True
        else:
            return False


    def setEachChannel(self, data):

        if (len(data) != 8):
            return False

        msg = "$SET_EACH:"
        for ch in data:
            # [enable, current, time]
            msg += str(ch[0]) + "," + str(ch[1]) + "," + str(ch[2]) + ";"

        self.write(msg)
        ack = self.read()

        if (ack == "DONE, SET_EACH\x0D\x0A"):
            return True
        else:
            return False

    # resets channel config
    def reset(self):
        self.write("$RESET:")
        ack = self.read()

        if (ack == "RESETED\x0D\x0A"):
            return True
        else:
            return False

    def getData(self):
        self.write("$DATA:")
        return self.read()

    def getChannelConfig(self):
        msg = "$PRINT_CONFIG:"
        self.write(msg)
        data = self.read()[14:]

        data = data.split(';')[:8]

        channel_config = {}

        for i in range(8):
            temp = data[i].split(',')

            channel_config["CH" + str(i)] = {"Enabled": temp[0], "TimerEnabled": temp[1],
                                             "Current": temp[2], "Time": temp[3]}

        return channel_config

