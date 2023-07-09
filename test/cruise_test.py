#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import sys
sys.path.append("../")
sys.path.append("../component")
import setpath
from component.driver import Driver
from detector.detectors import Cruiser
from widgets import boot_btn, front_camera


driver = Driver()
cruiser = Cruiser()

RUNFLAG = 1

if __name__ == '__main__':
    front_camera.start()
    driver.set_speed(20)
    driver.set_kx(1)
    # 延时
    time.sleep(0.5)
    print("==========RUN==========")
    while True:
        front_image = front_camera.read()
        angle = cruiser.infer_cnn(front_image)
        driver.steer(angle)
        if boot_btn.clicked():
            driver.stop()
            print("End of program!")
            break
    front_camera.stop()
