#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
from enums import *
from widgets import *
from plugins.log import log
from tasks import TASK_MAP
from component.serial_channel import startmachine

# 激流勇进 | 登高作赋 | 登高作赋 | 渔舟唱晚
# 物换星移 | 登高作赋 | 回船转舵 | 结束

BASE_SPEED = 16
REC_NUM = 3

SIGN_MAPPER = {
    "dgzf": SIGNLable.DGZF,
    "hczd": SIGNLable.HCZD,
    "jlyj": SIGNLable.JLYJ,
    "tjqf": SIGNLable.TJQF,
    "whxy": SIGNLable.WHXY,
    "yzcw": SIGNLable.YZCW
}

TASK_MAPPER = {
    "hhl": TASKLAble.HUANG_HE_LOU,
    "twg": TASKLAble.TENG_WANG_GE,
    "yyl": TASKLAble.YUE_YANG_LOU,
    "cz": TASKLAble.CZ,
    "yu": TASKLAble.YU,
    "lh": TASKLAble.LH,
    "xy": TASKLAble.XY
}

LABLE_CONFIG = {
    "sign": [
        SIGNLable.JLYJ, SIGNLable.DGZF, SIGNLable.DGZF,
        SIGNLable.YZCW, SIGNLable.WHXY, SIGNLable.DGZF,
        SIGNLable.HCZD
    ],
    "flag": [
        CVFlag.RIGHT, CVFlag.RIGHT, CVFlag.LEFT, CVFlag.LEFT,
        CVFlag.LEFT, CVFlag.LEFT, CVFlag.LEFT, CVFlag.LEFT
    ]
}

#巡航处理 - 控制巡线
class CruiseHandler:
    '''
    Class: 巡航处理器
    [单例模式] 巡航只允许有一个实例
    '''
    # 巡航任务动作
    def cruise_action(params = None):
        driver.set_speed(BASE_SPEED)
        driver.set_kx(1)
        sign_list = [0] * 7
        while True:
            front_image = front_camera.read()
            angle = cruiser.infer_cnn(front_image)
            log.info(angle)
            driver.steer(angle)
            res = sign_detector.detect(front_image)
            if len(res) != 0:
                log.info(res)
                for sign in res:
                    if SIGN_MAPPER[sign.index] == LABLE_CONFIG["sign"][TaskScheduler.number]:
                        sign_list[TaskScheduler.number] += 1
                        if sign_list[TaskScheduler.number] > REC_NUM:
                            return TaskScheduler.run()
            else:
                sign_list = [0] * 7

    # [腾蛟起凤] 特殊任务动作
    def task_action():
        pass

# 任务
class TaskScheduler():
    '''
    任务调度器
    '''
    number = 0

    def run(params = None):
        log.info("TaskScheduler Run", LABLE_CONFIG["sign"][TaskScheduler.number])
        driver.stop()
        time.sleep(5)
        TASK_MAP[TaskScheduler.number]() # 执行映射函数
        TaskScheduler.number += 1
        return CruiseHandler.cruise_action()


if __name__ == '__main__':
    log.time()
    log.info("==========[RUN]==========")
    startmachine()
    front_camera.start()
    # 基准速度与转弯系数
    driver.set_speed(20)
    driver.set_kx(1)

    # 蜂鸣器 声鸣
    buzzer.rings()
    while True:
        if boot_btn.clicked():
            log.info("===========[OK]===========")
            break
    while True:
        CruiseHandler.cruise_action()
    log.time()
    log.info("==========[END]==========")
