import device

print("Detecting device, please wait...")
print("Device detected on port: " + device.detect())

print("")
print("TEST: Sending START command...")
device.Start()
print("TEST: Received: " + device.Read())

print("")
print("TEST: Sending STOP command...")
device.Stop()
print("TEST: Received: " + device.Read())

device.Close()