#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading
from plugins import log
from widgets import *
#巡航处理 - 控制巡线
class CruiseHandler:
    '''
    Class: 巡航处理器
    [单例模式] 巡航只允许有一个实例
    '''
    # 巡航任务动作
    def cruise_action(params = None):
        pass

    # [腾蛟起凤] 特殊任务动作
    def task_action():
        pass

# 任务
class TaskScheduler(threading.Thread):
    '''
    任务调度器 [任务线程]
    '''
    number = 0
    # 激流勇进 | 登高作赋 | 登高作赋 | 渔舟唱晚 | 物换星移 | 登高作赋 | 回船转舵
    points = [
        "JLYJ", "DGZF", "DGZF", "YZWC", "WHXY", "TJQF", "DGZF", "HCZD"
    ]

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        log.info("TaskScheduler Run")
        side_camera.start()
        TaskScheduler.number += 1

if __name__ == '__main__':
    front_camera.start()
    # 基准速度与转弯系数
    driver.set_speed(20)
    driver.set_kx(1)

    # 蜂鸣器 声鸣
    buzzer.rings()
    while True:
        CruiseHandler.cruise_action()
    Log.time()
    Log.info("==========[END]==========")