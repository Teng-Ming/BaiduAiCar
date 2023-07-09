#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
from component.serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class RGBLamp:
    def __init__(self, port):
        self.port = port
        self.port_str = '{:02x}'.format(port)

    def on(self, which = 0, Red = 0, Green = 0, Blue = 0):  #@which 0代表全亮，其他值对应灯珠亮，1~4
        which_str = '{:02x}'.format(which)
        Red_str = '{:02x}'.format(Red)
        Green_str = '{:02x}'.format(Green)
        Blue_str = '{:02x}'.format(Blue)
        cmd_servo_data = bytes.fromhex('77 68 08 00 02 3B {} {} {} {} {} 0A'.format(
            self.port_str, which_str, Red_str, Green_str, Blue_str)
        )
        serial.write(cmd_servo_data)

    def quick_on(self, cmd):
        if cmd == "R":
            self.on(0, 255, 0, 0)
        elif cmd == "G":
            self.on(0, 0, 255, 0)
        elif cmd == "B":
            self.on(0, 0, 0, 255)
        else:
            self.on(0, 0, 0, 0)

    def quick_off(self):
        self.on(0, 0, 0, 0)

    def off(self):
        cmd_servo_data1 = bytes.fromhex('77 68 08 00 02 3B 02 00 00 00 00 0A')
        cmd_servo_data2 = bytes.fromhex('77 68 08 00 02 3B 03 00 00 00 00 0A')
        cmd_servo_data = cmd_servo_data1 + cmd_servo_data2
        serial.write(cmd_servo_data)

if __name__ == "__main__":
    import time
    rgb_lamp = RGBLamp(1)
    time.sleep(1)
    rgb_lamp.on(0, 0, 255, 0)
    time.sleep(0.6)
    rgb_lamp.on(0, 0, 0, 0)
    time.sleep(0.6)
    rgb_lamp.on(0, 0, 255, 0)
    time.sleep(0.6)
    rgb_lamp.on(0, 0, 0, 0)
    time.sleep(0.6)
    rgb_lamp.on(0, 0, 255, 0)
    time.sleep(0.6)
    rgb_lamp.on(0, 0, 0, 0)
    print("end")