# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 390)
        MainWindow.setMinimumSize(QSize(350, 390))
        MainWindow.setMaximumSize(QSize(350, 390))
        self.actionTips = QAction(MainWindow)
        self.actionTips.setObjectName(u"actionTips")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 331, 111))
        self.frame.setStyleSheet(u"#frame{border:1px solid rgb(0,0,0)}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 81, 20))
        self.selectCom = QComboBox(self.frame)
        self.selectCom.setObjectName(u"selectCom")
        self.selectCom.setGeometry(QRect(90, 10, 91, 22))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 10, 61, 20))
        self.baudrate = QLineEdit(self.frame)
        self.baudrate.setObjectName(u"baudrate")
        self.baudrate.setGeometry(QRect(262, 10, 61, 21))
        self.groupCheck = QGroupBox(self.frame)
        self.groupCheck.setObjectName(u"groupCheck")
        self.groupCheck.setGeometry(QRect(10, 40, 311, 61))
        self.port1 = QCheckBox(self.groupCheck)
        self.port1.setObjectName(u"port1")
        self.port1.setGeometry(QRect(80, 10, 31, 21))
        self.port1.setTristate(False)
        self.port2 = QCheckBox(self.groupCheck)
        self.port2.setObjectName(u"port2")
        self.port2.setGeometry(QRect(130, 10, 31, 21))
        self.port2.setChecked(False)
        self.port3 = QCheckBox(self.groupCheck)
        self.port3.setObjectName(u"port3")
        self.port3.setGeometry(QRect(180, 10, 31, 21))
        self.port3.setChecked(False)
        self.port4 = QCheckBox(self.groupCheck)
        self.port4.setObjectName(u"port4")
        self.port4.setGeometry(QRect(230, 10, 31, 21))
        self.port4.setChecked(False)
        self.port5 = QCheckBox(self.groupCheck)
        self.port5.setObjectName(u"port5")
        self.port5.setGeometry(QRect(80, 40, 31, 16))
        self.port6 = QCheckBox(self.groupCheck)
        self.port6.setObjectName(u"port6")
        self.port6.setGeometry(QRect(130, 40, 31, 16))
        self.port7 = QCheckBox(self.groupCheck)
        self.port7.setObjectName(u"port7")
        self.port7.setGeometry(QRect(180, 40, 31, 16))
        self.port8 = QCheckBox(self.groupCheck)
        self.port8.setObjectName(u"port8")
        self.port8.setGeometry(QRect(230, 40, 31, 16))
        self.groupCheck.raise_()
        self.label.raise_()
        self.selectCom.raise_()
        self.label_2.raise_()
        self.baudrate.raise_()
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(140, 320, 75, 24))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 120, 331, 141))
        self.frame_2.setStyleSheet(u"#frame_2{border:1px solid rgb(0,0,0)}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.config = QTextEdit(self.frame_2)
        self.config.setObjectName(u"config")
        self.config.setGeometry(QRect(180, 70, 141, 61))
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 50, 101, 20))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 50, 51, 21))
        self.times = QLineEdit(self.frame_2)
        self.times.setObjectName(u"times")
        self.times.setGeometry(QRect(10, 70, 111, 20))
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 331, 41))
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(True)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 290, 301, 23))
        self.progressBar.setValue(24)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 270, 53, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 350, 22))
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuhelp.addAction(self.actionTips)
        self.menuhelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"APC PDU\u63a7\u5236\u7a0b\u5e8f", None))
        self.actionTips.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u63d0\u793a", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PDU\u63a7\u5236\u4e32\u53e3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\u8bbe\u7f6e", None))
        self.baudrate.setText(QCoreApplication.translate("MainWindow", u"9600", None))
        self.groupCheck.setTitle(QCoreApplication.translate("MainWindow", u"PDU\u7aef\u53e3\u53f7", None))
        self.port1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.port2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.port3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.port4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.port5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.port6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.port7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.port8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.config.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1,1,2,3</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e0b\u7535\u65f6\u95f4\u914d\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5faa\u73af\u6b21\u6570", None))
        self.times.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e0b\u7535\u65f6\u95f4\u9700\u8981\u4f20\u5165\u5076\u6570\u5bf9\u503c\u59821,1,2,3  \u5373\u8868\u793a\u4e0a\u75351s\uff0c\u4e0b\u75351s\uff0c\u4e0a\u75352s\uff0c\u4e0b\u75353s\u4e3a\u4e00\u4e2a\u5faa\u73af\u3002", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u8fdb\u5ea6", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi

