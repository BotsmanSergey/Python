#for win
import serial
s = serial.Serial('COM7')
res = s.read()
print(res)

#
#pip install pyserial

import serial
import time

serialPort = serial.Serial(
    port="COM4", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)
serialString = ""  # Used to hold data coming over UART
while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        try:
            print(serialString.decode("Ascii"))
        except:
            pass

#for linux
my_serial = serial.Serial('/dev/ttyS1', 115200)
my_serial.write(b'command_1')
my_serial.close()