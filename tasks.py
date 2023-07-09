# -*- coding: utf-8 -*
from enums import TASKLAble, SIGNLable
from widgets import *
import time

DGZF_MAPPER = {
    TASKLAble.TENG_WANG_GE: 60,
    TASKLAble.HUANG_HE_LOU: 120,
    TASKLAble.YUE_YANG_LOU: 180
}

def _DGZF_() -> None:
    '''
    flag_servo.control(DGZF_MAPPER[lable], sipeed)
    f = DGZF_MAPPER[lable] * 0.01 #延时
    time.sleep(f)
    for i in range(0, 3):
        rgb_lamp.quick_on("G")
        time.sleep(0.5)
        rgb_lamp.quick_off()
        time.sleep(0.5)
    flag_servo.control(0, sipeed)
    time.sleep(f)
    '''

def _YZCW_(times: float) -> None:
    '''st = time.time()
    while True:
        driver.move([30, 30, 30, 30])
        time.sleep(0.001)
        if(time.time() - st > times):
            driver.stop()
            time.sleep(0.001)
            break
    buzzer.rings()
    time.sleep(0.5)
    buzzer.rings()
    time.sleep(0.5)
    buzzer.rings()
    time.sleep(0.5)
    st = time.time()
    while True:
        driver.move([30, 30, 30, 30])
        time.sleep(0.001)
        if(time.time() - st > times):
            driver.stop()
            time.sleep(0.001)
            break
    '''

def _JLYJ_():
    pass

def _WHXY_():
    pass

def _HCZD_():
    pass

def _TJQF_():
    pass

TASK_MAP = {
    SIGNLable.DGZF: _DGZF_,
    SIGNLable.HCZD: _HCZD_,
    SIGNLable.JLYJ: _JLYJ_,
    SIGNLable.TJQF: _TJQF_,
    SIGNLable.WHXY: _WHXY_,
    SIGNLable.YZCW: _YZCW_,
}

if __name__ == '__main__':
    print("+++++++")
    while True:
        if boot_btn.clicked() or True:
            print("$$$$$$$$$$$$")
            rgb_lamp.quick_on("G")
            time.sleep(0.1)
            rgb_lamp.quick_off()
            #_DGZF_(DGZFLable.TENGWANG)
            _YZCW_(8.0)
            time.sleep(1)
            break