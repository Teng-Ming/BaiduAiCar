#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
from serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class Servo_pwm:
    def __init__(self, ID):
        self.ID = ID
        self.ID_str = '{:02x}'.format(ID)

    def control(self, angle, speed):
        angle = int(angle)
        cmd_servo_data = bytes.fromhex('77 68 06 00 02 0B') + bytes.fromhex(self.ID_str) + speed.to_bytes(
            1, byteorder='big', signed=True) + angle.to_bytes(1, byteorder='big', signed=False
        ) + bytes.fromhex('0A')
        serial.write(cmd_servo_data)

if __name__ == "__main__":
    import time
    servo_2 = Servo_pwm(0)
    servo_2.control(-40, 60)
    time.sleep(4)
    #servo_2.servo_control(-120, 60)
    #time.sleep(4)
    #servo_2.servo_control(120, 60)
    #time.sleep(4)
