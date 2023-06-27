# 百度智慧交通创意组-"长江之歌"

## 文件目录结构

│
│  boot.py    【主运行文件】
│  README.md
│
├─component   【组件封装文件夹】
│  │  camera.py         【摄像头】
│  │  chassis.py        【底盘驱动】
│  │  driver.py         【底盘高级封装】
│  │  serial_channel.py 【串口信道】
│  │
│  ├─control  【控制模组】
│  │      buzzer.py     【蜂鸣器】
│  │      matrix_btn.py 【矩阵按键】
│  │      rgb_lamp.py   【RGB灯】
│  │      server_pwm.py 【PWM 舵机】
│  │      server.py     【舵机】
│  │      switch_btn.py
│  │
│  └─sensor   【传感模组】
│          Infrared.py  【红外传感器】
│          magento.py   【电磁传感器】
│          ultrasonic.py【超声波感器】
│
├─config 【配置类】
│      board.py  【板载信息】
│      target.py 【目标信息】
│
├─handler 【处理器】
│      model_handler.py 【模型处理器】
│
├─plugins 【小插件】
│      log.py 【日志类】
│
└─res
    │  赛题规则.pdf
    │
    └─model 【模型文件夹】
