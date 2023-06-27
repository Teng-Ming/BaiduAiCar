#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
import struct
from serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class InfraredSensor:
    '''
    红外传感器
    '''
    def __init__(self, port):
        port_str = '{:02x}'.format(port)
        self.cmd_data = bytes.fromhex('77 68 04 00 01 D4 {} 0A'.format(port_str))

    def read(self):
        serial.write(self.cmd_data)
        return_data = serial.read()
        if return_data[2] != 0x04:
            return None
        if return_data[3] == 0x0a:
            return None
        return_data_infrared = return_data[3:7]
        print(return_data_infrared)
        infrared_sensor = struct.unpack('<i', struct.pack('4B', *(return_data_infrared)))[0]
        return infrared_sensor