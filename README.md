# serial-monitor

Serial monitor for Arduino.

## Install Dependencies

Uses Python 3

```
pip3 install argparse

pip3 install pyserial
```

## Usage

```
serial-monitor.py -h
```

### Example

To monitor (with active display) the Arduino device plugged into /dev/ttyACM0, at a baud rate of 9600:

```
serial-monitor.py -b 9600 -p /dev/ttyACM0 -m
```
