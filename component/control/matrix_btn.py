#!/usr/bin/python3
# -*- coding: utf-8 -*-
import struct
import sys
sys.path.append("../")
from component.serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class MatrixButton:
    def __init__(self, port):
        self.state = False
        self.port = port
        port_str = '{:02x}'.format(port)
        self.cmd_data = bytes.fromhex('77 68 05 00 01 E1 {} 01 0A'.format(port_str))

    def clicked(self, key):
        serial.write(self.cmd_data)
        response = serial.read()
        buttonclick=-1
        if len(response) == 9 and  response[5]==0xE1 and response[6] == self.port:
            button_byte = response[3:5] + bytes.fromhex('00 00')
            button_value=struct.unpack('<i', struct.pack('4B', *(button_byte)))[0]
            print(button_value)
            if button_value >= 0x150 and button_value <= 0x15f:
                buttonclick = 1
            elif button_value >= 0x200 and button_value <= 0x20f:
                buttonclick = 2
            elif button_value >= 0x050 and button_value <= 0x05f:
                buttonclick = 3
            elif button_value >= 0x2f0 and button_value <= 0x2ff:
                buttonclick = 4
            else:
                buttonclick = -1
        return buttonclick == key

if __name__ == "__main__":
    print("+++++++++++++++++++++++++++++")
    button = MatrixButton(1)
    while True:
        if button.clicked(1) :
            print("clicked 1")
            break
        if button.clicked(2) :
            print("clicked 2")
            break
        if button.clicked(3) :
            print("clicked 3")
            break
        if button.clicked(4) :
            print("clicked 4")
            break