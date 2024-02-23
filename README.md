# pdu-control

> The APC PDU control tool with GUI interface based on PySide6 and pyserial.

## 介绍

通过串口控制PDU设备，对PDU电源输出端口自定义通断电时间及循环次数，以满足CPE设备的电源上下电可靠性测试要求。

### Developer

[FanHao](http://alanfanh.github)

### 项目结构

````text
pdu-control
|
|--common
|  |
|  |---pdu.py         # 控制pdu类源码
|  |---gui_ui.py      # 界面源码
|  |---gui.ui         # ui原型文件
|
|--main.py            # 程序入口，界面主线程,工作子线程处理逻辑
|
````

## 环境

> python3.9.2 64bit

### 依赖

> 可将如下文本保存至requirements.txt文件中，然后使用"pip install -r requirements.txt"一键安装所有依赖项

````text
pyside6==6.2.3
pyserial==3.5
````