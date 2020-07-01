#!/usr/bin/python3

import argparse
import serial
from time import sleep
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-b", "--baud", type=int, default=9600, help="Baud rate.  Default is 9600.")
parser.add_argument("-p", "--port", type=str, default="/dev/ttyACM0", help="Port to monitor.  Examples: 'COM3' (Windows), '/dev/ttyACM0' (Linux). Default is '/dev/ttyACM0'.")
parser.add_argument("-m", "--monitor", help="Monitor and display port traffic? If this argument is not supplied, the port will be initialized, but not polled for traffic.", action="store_true")
parser.add_argument("-w", "--wait", type=int, default=1, help="Number of seconds to wait before starting the polling loop. Default is 1.")
args = parser.parse_args()

com_port = args.port
baud_rate = args.baud

try:
	ser = serial.Serial(com_port, baud_rate, timeout = .1)
except Exception as ex:
	print(ex)
	sys.exit(-1)

try:
	print(f'Waiting {args.wait} second(s) for device')
	sleep(args.wait)
	print(f'Polling {ser.name}  (Ctrl-C to stop)')
	#print('(Ctrl-C to stop)')
except Exception as ex:
	print(ex)
	sys.exit(-1)

while True:
	val = str(ser.readline().decode().strip('\r\n'))
	if (args.monitor and val != ''):
		print(val, flush=True)
