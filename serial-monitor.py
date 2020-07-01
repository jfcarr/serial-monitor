#!/usr/bin/python3

import argparse
import serial
from time import sleep
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-b", "--baud", type=int, default=9600, help="Baud rate.  Defaults to 9600")
parser.add_argument("-p", "--port", type=str, default="/dev/ttyACM0", help="Port to monitor.  Examples: 'COM3' (Windows), '/dev/ttyACM0' (Linux). Defaults to '/dev/ttyACM0'")
parser.add_argument("-m", "--monitor", help="Monitor and display port traffic?", action="store_true")
args = parser.parse_args()

COM = args.port
BAUD = args.baud

try:
	ser = serial.Serial(COM, BAUD, timeout = .1)
except Exception as ex:
	print(ex)
	sys.exit(-1)

try:
	print('Waiting for device')
	sleep(2)
	print(ser.name)
	print('(Ctrl-C to stop)')
except Exception as ex:
	print(ex)
	sys.exit(-1)

while True:
	val = str(ser.readline().decode().strip('\r\n'))
	if (args.monitor and val != ''):
		print(val, flush=True)
