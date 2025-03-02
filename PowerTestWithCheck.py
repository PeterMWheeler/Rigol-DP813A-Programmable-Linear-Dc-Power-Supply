# Written by ESE Peter Wheeler. 1/16/24
# Use: The scripts intended use is for power testing on the Rigol DP813A power supply.
# (TCPIP0::192.168.0.136::INSTR) Refers to the IP address of the unit
# To change the validation test, change the IP in the validate_ping call. 

import pyvisa
import time
from pythonping import ping


def validate_ping(target):
    response = ping(target)
    time.sleep(4)
    if response.success() == 0 :
        print(f"Ping to {target} failed. Device is unreachable.")
        print(f" The test ran: {count} times")
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
    

while TheDeviceIsOn:
    count +=1
    
    # set the voltage on Channel 1
    # Starting State (power is off)
    device.write("APPL CH1,0,00")  # Set channel 1 voltage to 0V and 0Amps
    print("Voltage set to 0V on Channel 1 with 0 AMPs.")

    # Optional delay
    timer = 5
    time.sleep(timer)
    print(f"{timer} second delay")

    # set the voltage on Channel 1
    # Start power (Accessory on?)
    device.write("APPL CH1,12.5,10")  # Set channel 1 voltage to 12.5V and 10Amps
    print("Voltage set to 12.5V on Channel 1 with 10 AMPs.")

    # Optional delay
    timer = 2
    time.sleep(timer)
    print(f"{timer} second delay")
    

    # set the voltage on Channel 1
    # Start cranking (Power drops)
    device.write("APPL CH1,10.7,10")  # Set channel 1 voltage to 10.7V and 10Amps
    print("Voltage set to 10V on Channel 1 with 10 AMPs.")

    # Optional delay
    timer = 4
    time.sleep(timer)
    print(f"{timer} second delay")

    # set the voltage on Channel 1
    # Enging started (Power stable)
    device.write("APPL CH1,13.2,10")  # Set channel 1 voltage to 12V and 10Amps
    print("Voltage set to 13.2V on Channel 1 with 10 AMPs.")


    print("startup done")  # set this to how long you would like to wait before testing the device and restarting the loop
    print(f"Test number {count}")
    timer = 300
    time.sleep(timer)
    print(f"{timer} second delay")
    
    #Test If can Ping Device or site. (Set the IP in the call)
    print("testing Device with Ping")
        
    #ping ("192.168.0.1", verbose=True)  #ping with no test
    validate_ping("192.168.0.1")  # call validate_ping


    print("done with Ping Test")
    print("Starting again in 5 seconds")
    time.sleep(5)

