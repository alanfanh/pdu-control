import sys, time
import serial.tools.list_ports
from common.gui_ui import Ui_MainWindow
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtCore import QThread, SIGNAL, Slot
from common.pdu import Pdu
from datetime import datetime

class WorkThread(QThread):
    # 工作子线程，与GUI界面分离
    singal_str = QtCore.Signal(str)
    singal_int = QtCore.Signal(int)
    finished = QtCore.Signal()
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent

    def start_run(self) -> None:
        self.start()

    def stop_run(self) -> None:
        self.terminate()
        self.wait()

    def run(self) -> None:
        # 控制PDU设备端口通断电的主逻辑
        print(self.parent.rate, self.parent.times_int, self.parent.interval, self.parent.com_port, self.parent.pdu_port)
        rate, times, interval, com, port = self.parent.rate, self.parent.times_int, self.parent.interval, self.parent.com_port, self.parent.pdu_port
        if all([rate, times, interval, com, port]):
            # 将时间配置字符串转成list
            interval_l = list(map(int, interval.split(",")))
            try:
                pdu = Pdu(port=com, user="apc", pwd="apc", baudrate=rate, timeout=1.0)
                if (not pdu.is_login()):
                    pdu.login()
            except Exception as e:
                self.singal_str.emit("无法控制PDU，请检查PDU控制串口是否占用")
                return 0
            time.sleep(1.5)
            if (len(interval_l)%2 == 0):
                for i in range(int(times)):
                    # print("---第%s次循环---" % (i+1))
                    for j in range(len(interval_l)):
                        # print("j=%d" % j)
                        # 上电配置
                        if (j%2 == 0):
                            # 循环依次上电给出的pdu端口
                            for p in port:
                                # print("pdu端口%s" % p)
                                pdu.power_on(p)
                            time.sleep(interval_l[j])
                            # print(datetime.now(), "上电%d秒\r" % interval_l[j])
                        else:
                            for p in port:
                                # print("pdu端口%s" % p)
                                pdu.power_off(p)
                            time.sleep(interval_l[j])
                            # print(datetime.now(),"下电%d秒\r" % interval_l[j])
                    self.singal_int.emit(i+1)
            else:
                self.singal_str.emit("请传入偶数个时间间隔")
            pdu.logout()
            pdu.closed_comport()
        else:
            self.singal_str.emit("配置参数缺失，请检查配置")
        self.finished.emit()


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_com_port()
        self.rate = None
        self.interval = None
        self.times_int = None
        self.com_port = None
        self.pdu_port = None
        self.pv = 0
        # 槽函数
        self.init_pdu_port()
        self.connect(self.startButton, SIGNAL("clicked()"), self.start_run)
        self.connect(self.actionTips, SIGNAL("triggered()"), self.help)
        self.connect(self.actionAbout, SIGNAL("triggered()"), self.about)
        # 子线程
        self.workthread = WorkThread(self)
        self.workthread.singal_str.connect(self.dialog)
        self.workthread.singal_int.connect(self.handle_progess)
        self.workthread.finished.connect(self.thread_finished)
        self.progressBar.setValue(self.pv)
        
    def init_com_port(self):
        port_lists = list(serial.tools.list_ports.comports())
        for com in port_lists:
            self.selectCom.addItem(com.name.strip())
        self.connect(self.selectCom, SIGNAL("currentIndexChanged(int)"), self.select_com_port)

    def select_com_port(self):
        selected_com = self.selectCom.currentText()
        self.com_port = selected_com

    def init_pdu_port(self):
        self.connect(self.port1,SIGNAL("clicked()"),self.select_pdu_port)
        self.connect(self.port2,SIGNAL("clicked()"),self.select_pdu_port)
        self.connect(self.port3,SIGNAL("clicked()"),self.select_pdu_port)
        self.connect(self.port4,SIGNAL("clicked()"),self.select_pdu_port)
        self.connect(self.port5,SIGNAL("clicked()"),self.select_pdu_port)
        self.connect(self.port6,SIGNAL("clicked()"),self.select_pdu_port)
        self.connect(self.port7,SIGNAL("clicked()"),self.select_pdu_port)
        self.connect(self.port8,SIGNAL("clicked()"),self.select_pdu_port)

    def select_pdu_port(self):
        self.pdu_port = []
        if self.port1.isChecked():
            self.pdu_port.append(1)
        if self.port2.isChecked():
            self.pdu_port.append(2)
        if self.port3.isChecked():
            self.pdu_port.append(3)
        if self.port4.isChecked():
            self.pdu_port.append(4)
        if self.port5.isChecked():
            self.pdu_port.append(5)
        if self.port6.isChecked():
            self.pdu_port.append(6)
        if self.port7.isChecked():
            self.pdu_port.append(7)
        if self.port8.isChecked():
            self.pdu_port.append(8)
        # print(self.pdu_port)

    def handle_config(self):
        # 处理UI界面配置的数据
        self.rate = self.baudrate.text()
        self.times_int = self.times.text()
        self.interval = self.config.toPlainText()
        self.com_port = self.selectCom.currentText()
        
    @Slot()
    def start_run(self):
        # 开始按钮槽函数
        if (self.startButton.text() == u"开始"):
            self.handle_config()
            self.workthread.start_run()
            self.progressBar.setMaximum(int(self.times_int))
            self.statusbar.showMessage(u"控制程序正在工作")
            self.startButton.setText("运行中...")
        else:
            self.workthread.stop_run()
            self.startButton.setText(u"开始")

    def thread_finished(self):
        # 槽函数，判断线程是否终止
        self.startButton.setText(u"开始")
        self.statusbar.showMessage("程序未运行")

    def handle_progess(self, v):
        # 槽函数，接收work线程传过来的已完成循环次数
        self.progressBar.setValue(v)

    @Slot()
    def help(self):
        # 槽函数，帮助信息弹窗
        QMessageBox.about(self, u"帮助信息", u"开发者:FanHao\n1.PDU端口存在机械寿命，不需要使用的端口，请勿启用。\n2.上下电时间不建议配置超过180s；PDU控制登录老化时间为180s，等待间隔超过180s，pdu控制连接已退出登录")

    @Slot()
    def about(self):
        # 槽函数，关于弹窗
        QMessageBox.about(self, u"About", u"APC PDU控制程序V1.0\n")

    @Slot()
    def dialog(self, msg):
        # 槽函数，提示弹窗
        QMessageBox.about(self, u"警告", msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec())

