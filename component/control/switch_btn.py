#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("../")
from serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL


class SwitchButton:
    def __init__(self, port):
        self.state = False
        self.port = port
        self.state = True
        port_str = '{:02x}'.format(port)
        self.cmd_data = bytes.fromhex('77 68 04 00 01 DD {} 0A'.format(port_str))

    def clicked(self):
        serial.write(self.cmd_data)
        response = serial.read()  # 77 68 01 00 0D 0A
        if len(response) < 8 or response[4] != 0xDD or response[5] != self.port \
                or response[2] != 0x01:
            return False
        state = response[3] == 0x01
        clicked = False
        if state == True and self.state == True and clicked == False:
            clicked = True
        if state == False and self.state == True and clicked == True:
            clicked = False
        return clicked
