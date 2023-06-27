#!/usr/bin/python3
# -*- coding: utf-8 -*-
import struct
import sys
sys.path.append("../")
from serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class Ultrasonic():
    '''
    超声波传感器
    '''
    def __init__(self, port):
        self.port = port
        port_str = '{:02x}'.format(port)
        self.cmd_data = bytes.fromhex('77 68 04 00 01 D1 {} 0A'.format(port_str))

    def read(self):
        serial.write(self.cmd_data)
        return_data = serial.read()
        if len(return_data) < 11 or return_data[7] != 0xD1 or return_data[8] != self.port:
            return None
        return_data_ultrasonic = return_data[3:7]
        ultrasonic_sensor = struct.unpack('<f', struct.pack('4B', *(return_data_ultrasonic)))[0]
        return int(ultrasonic_sensor)