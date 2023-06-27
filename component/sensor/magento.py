#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
import struct
from serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class MagnetoSensor:
    '''
    电磁传感器
    '''
    def __init__(self, port):
        self.port = port
        port_str = '{:02x}'.format(self.port)
        self.cmd_data = bytes.fromhex(
            '77 68 04 00 01 CF {} 0A'.format(port_str))

    def read(self):
        serial.write(self.cmd_data)
        return_data = serial.read()
        if len(return_data) < 11 or return_data[7] != 0xCF or return_data[8] != self.port:
            return None
        return_data = return_data[3:7]
        mag_sensor = struct.unpack('<i', struct.pack('4B', *(return_data)))[0]
        return int(mag_sensor)
