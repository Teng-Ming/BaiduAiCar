#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
from serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

#蜂鸣器
class Buzzer:
    def __init__(self, data = '77 68 06 00 02 3D 03 02 0A'):
        self.cmd_data = bytes.fromhex(data)

    def rings(self):
        serial.write(self.cmd_data)

if __name__ == "__main__":
    buzzer = Buzzer()
    #
    buzzer.rings()
    #
    buzzer.rings()