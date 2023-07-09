
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import serial
import time
from threading import Lock

class SerialChannel:
    def __init__(self, bps = 380400):
        port_x = "/dev/ttyUSB0"


        self.res = None
        self.serial = serial.Serial(port_x, int(bps), timeout=0.004, parity=serial.PARITY_NONE, stopbits=1)
        time.sleep(1)

    def write(self, data):
        self.res = ''
        self.serial.reset_input_buffer()
        lock = Lock()
        lock.acquire()
        try:
            self.serial.write(data)
            # print(data)
            self.serial.flush()
            self.res = self.serial.readline()
            for i in range(10):
                self.res = self.res + self.serial.readline()
                time.sleep(0.001)
            # print(self.res)
            self.serial.flush()
            
        except ZeroDivisionError as e:
            print('except:', e)
        finally:
            # print("serial.write_finally\n")
            lock.release()
            pass

    def read(self):
        return self.res

SERIAL_CHANNEL = SerialChannel(115200)

# 机器省电关闭
def startmachine():
    cmd_data = bytes.fromhex('77 68 03 00 02 67 0A')
    for i in range(0, 2):
        SERIAL_CHANNEL.write(cmd_data)
        time.sleep(0.2)
