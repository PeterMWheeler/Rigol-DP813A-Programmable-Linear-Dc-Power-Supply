
import pyvisa
import time
from pythonping import ping
import random

def validate_ping(target):
    response = ping(target)
    
    if response is None:
        print(f"Ping to {target} failed. Device is unreachable.")
        quit()

    else:
        print(f"Ping to {target} successful. Response time: {response} ms")



# Setup communication with the Rigol DP813A using its LAN address
rm = pyvisa.ResourceManager()

# Open the resource using the correct address (verify the IP address and port)
device = rm.open_resource('TCPIP0::192.168.0.136::INSTR')
count = 0
TheDeviceIsOn = True
timer =0


# Query the device to ensure it's communicating
try:
    print("Device ID: " + device.query("*IDN?"))
except pyvisa.VisaIOError:
    print("Error: Unable to communicate with the device.")
    print("Please check the device, it may be in an error state")
    print(f"the test was ran: {count} times")
    exit()  
    

    
    # set the voltage on Channel 1
    # Starting State (power is off)
device.write("APPL CH1,12,10")  # Set channel 1 voltage to 0V and 0Amps
print("Voltage set to 12V on Channel 1 with 0 AMPs.")
