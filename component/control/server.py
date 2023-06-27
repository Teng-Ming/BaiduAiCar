#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
from serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class Servo:
    def __init__(self, ID):
        self.ID = ID
        self.ID_str = '{:02x}'.format(ID)

    def control(self, angle, speed):
        angle = int(angle)
        cmd_servo_data = bytes.fromhex('77 68 08 00 02 36 {}'.format(self.ID_str)) + speed.to_bytes(
            1, byteorder='big', signed=True) + (angle).to_bytes(3, byteorder='little', signed=True
        ) + bytes.fromhex('0A')
        serial.write(cmd_servo_data)

if __name__ == "__main__":
    import time
    servo_2 = Servo(0)
    servo_2.ontrol(-40, 60)
    time.sleep(4)
    #servo_2.servo_control(-120, 60)
    #time.sleep(4)
    #servo_2.servo_control(120, 60)
    #time.sleep(4)
