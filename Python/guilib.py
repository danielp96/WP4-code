

def refreshPortList():
    portList = device.getPortList()

    if (len(portList) == 0):
        portList = [""]

    return portList


def buttonStartFunction():

    if (dev.port() == "none"):
        return

    current = ch1CurrentEntry.get()

    time = ch1TimeEntry.get()

    dev.setChannel(1, current, time)
    dev.start()


def buttonStopFunction():

    if (dev.port() == "none"):
        return

    dev.stop()


def buttonRefreshPortFunction():
    portList = refreshPortList()

    portMenuValue.set('')
    portMenu['menu'].delete(0, 'end')

    for port in portList:
        portMenu['menu'].add_command(label=port, command=tk._setit(portMenuValue, port))

    portMenuValue.set(portList[0]) # default value


def buttonConnectFunction():
    dev.port(portMenuValue.get())

    if (dev.ping()):
        # set some indicator of connected
        pass
    else:
        # set some indicator of not connected
        pass