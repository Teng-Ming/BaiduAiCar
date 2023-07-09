#!/usr/bin/python3
# -*- coding: utf-8 -*
from component.camera import Camera
from component.driver import Driver
from component.control.buzzer import Buzzer

front_camera = Camera(0)
side_camera = Camera(1)

driver = Driver()
buzzer = Buzzer()

