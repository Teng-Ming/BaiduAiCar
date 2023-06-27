#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
import struct
from serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class MatrixButton:
    def __init__(self, port, buttonstr):
        self.state = False
        self.port = port
        self.buttonstr = buttonstr
        port_str = '{:02x}'.format(port)
        self.cmd_data = bytes.fromhex('77 68 05 00 01 E1 {} 01 0A'.format(port_str))

    def clicked(self):
        serial.write(self.cmd_data)
        response = serial.read()
        buttonclick="no"
        if len(response) == 9 and  response[5]==0xE1 and response[6] == self.port:
            button_byte = response[3:5] + bytes.fromhex('00 00')
            button_value=struct.unpack('<i', struct.pack('4B', *(button_byte)))[0]
            if button_value>=0x1f1 and button_value<=0x20f:
                buttonclick="U"
            elif button_value>=0x330 and button_value<=0x33f:
                buttonclick = "L"
            elif button_value>=0x2f1 and button_value<=0x30f:
                buttonclick = "D"
            elif button_value>=0x2a0 and button_value<=0x2af:
                buttonclick = "R"
            else:
                buttonclick
        return self.buttonstr == buttonclick