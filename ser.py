import serial
import time
print "Enter ttyACM number"
x = raw_input()
dev = '/dev/ttyACM'+ str(x[0])
ser = serial.Serial(dev, baudrate = 115200)
count = 0
while 1:
	print "[" + str(int(time.time())) +"] " + ser.readline()
	count = count +1
	if(count%5 == 0):
		ser.write("okay\r\n")
		print "okay"
	