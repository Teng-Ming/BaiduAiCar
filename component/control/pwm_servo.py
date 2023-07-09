#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
from component.serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class PWMServo:
    def __init__(self, ID):
        self.ID = ID
        self.ID_str = '{:02x}'.format(ID)

    def control(self, angle, speed):
        angle = int(angle)
        cmd_servo_data = bytes.fromhex('77 68 06 00 02 0B') + bytes.fromhex(self.ID_str) + speed.to_bytes(
            1, byteorder='big', signed=True) + angle.to_bytes(1, byteorder='big', signed=False
        ) + bytes.fromhex('0A')
        serial.write(cmd_servo_data)

# 右60 下120 左180
if __name__ == "__main__":
    import time
    servo_2 = PWMServo(6)
    time_start = time.clock()
    servo_2.control(60, 60)
    time_end = time.clock()  # 记录结束时间
    time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
    print(time_sum)
    time.sleep(0.25)
    servo_2.control(120, 60)
    time.sleep(0.25)
    servo_2.control(180, 60)
    time.sleep(0.25)
    print("end")
