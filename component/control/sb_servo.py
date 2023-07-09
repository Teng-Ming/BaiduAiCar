
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
from component.serial_channel import SERIAL_CHANNEL

serial = SERIAL_CHANNEL

class SBServo:
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
    print("ok")
    import time
    servo_2 = SBServo(1)
    servo_2.control(142, 60)
    time.sleep(1)
    servo_2.control(-36, 60)
    time.sleep(1)

