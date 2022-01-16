import device
import time

dev = device.Device()

#dev.port("/dev/ttyACM0")
#print(dev.port())

print("Detecting device, please wait...")
print("Device detected on port: " + str(dev.detect()))

print(dev.dataBuffer)

print("")
print("Sending START command.")
dev.start()


print("")
print("Testing STOP command: " + str(dev.stop()))

print(dev.dataBuffer)


# print("")
# print("Testing SET_ONE command: " + str(dev.setChannel(1, 5, 10)))

# print(dev.getChannelConfig())

# data = [ [1,1,1], [0,2,2], [1,3,3], [0,4,4], [1,5,5], [0,6,6], [1,7,7], [0,8,8]]
# print("")
# print("Testing SET_ALL command: " + str(dev.setEachChannel(data)))

# print(dev.getChannelConfig())

# print("")
# print("Testing RESET command: " + str(dev.reset()))

# print(dev.getChannelConfig())

dev.close()


