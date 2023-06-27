#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
from serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class RGBLamp:
    def __init__(self, port):
        self.port = port
        self.port_str = '{:02x}'.format(port)

    def on(self, which = 0, Red = 255, Green = 0, Blue = 0):  #@which 0代表全亮，其他值对应灯珠亮，1~4
        which_str = '{:02x}'.format(which)
        Red_str = '{:02x}'.format(Red)
        Green_str = '{:02x}'.format(Green)
        Blue_str = '{:02x}'.format(Blue)
        cmd_servo_data = bytes.fromhex('77 68 08 00 02 3B {} {} {} {} {} 0A'.format(self.port_str, which_str, Red_str \
                                                                                    , Green_str, Blue_str))
        serial.write(cmd_servo_data)

    def off(self):
        cmd_servo_data1 = bytes.fromhex('77 68 08 00 02 3B 02 00 00 00 00 0A')
        cmd_servo_data2 = bytes.fromhex('77 68 08 00 02 3B 03 00 00 00 00 0A')
        cmd_servo_data = cmd_servo_data1 + cmd_servo_data2
        serial.write(cmd_servo_data)

if __name__ == "__main__":
    import time
    rgb_lamp = RGBLamp(2)
    rgb_lamp.on()
    time.sleep(0.5)
    rgb_lamp.off()
    time.sleep(0.5)
    rgb_lamp.on()
    time.sleep(0.5)
    rgb_lamp.off()