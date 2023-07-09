#!/usr/bin/python3
# -*- coding: utf-8 -*
from component.camera import Camera
from component.driver import Driver
from component.control.buzzer import Buzzer
from component.control.sb_servo import SBServo
from component.control.pwm_servo import PWMServo
from component.control.rgb_lamp import RGBLamp
from component.control.switch_btn import SwitchButton

from detector.detectors import Cruiser, TaskDetector, SignDetector

front_camera = Camera(0)
side_camera = Camera(1)

driver = Driver()

boot_btn = SwitchButton(1)

rgb_lamp = RGBLamp(1)
sicv_servo = SBServo(1)
flag_servo = PWMServo(6)

buzzer = Buzzer()

cruiser = Cruiser()
sign_detector = SignDetector()


if __name__ == "__main__":
    print("ok")
    pass
