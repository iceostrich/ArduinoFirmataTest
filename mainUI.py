# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 54, 12))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 70, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(220, 70, 113, 20))
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(220, 290, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 290, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 290, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 120, 113, 20))
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 54, 12))
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 120, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(100, 430, 601, 71))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.comboBox_2.raise_()
        self.label_2.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.comboBox_3.raise_()
        self.lcdNumber.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuBegain = QtWidgets.QMenu(self.menubar)
        self.menuBegain.setObjectName("menuBegain")
        self.menuPort = QtWidgets.QMenu(self.menuBegain)
        self.menuPort.setObjectName("menuPort")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCOM1 = QtWidgets.QAction(MainWindow)
        self.actionCOM1.setObjectName("actionCOM1")
        self.actionCOM2 = QtWidgets.QAction(MainWindow)
        self.actionCOM2.setObjectName("actionCOM2")
        self.actionBoard = QtWidgets.QAction(MainWindow)
        self.actionBoard.setObjectName("actionBoard")
        self.actionUser_guide = QtWidgets.QAction(MainWindow)
        self.actionUser_guide.setObjectName("actionUser_guide")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuPort.addAction(self.actionCOM1)
        self.menuPort.addAction(self.actionCOM2)
        self.menuBegain.addAction(self.menuPort.menuAction())
        self.menuBegain.addAction(self.actionBoard)
        self.menuBegain.addSeparator()
        self.menuBegain.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionUser_guide)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuBegain.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.lineEdit.hide)
        self.comboBox.activated['QString'].connect(self.lineEdit.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arduino PyFirmata Demo"))
        self.label.setText(_translate("MainWindow", "Pin 1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Input"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Output"))
        self.comboBox.setItemText(2, _translate("MainWindow", "PWM"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Servo"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Analog"))
        self.lineEdit.setText(_translate("MainWindow", "LOW"))
        self.pushButton.setText(_translate("MainWindow", "HIGH"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Input"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Output"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "PWM"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Servo"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Analog"))
        self.label_2.setText(_translate("MainWindow", "Pin 10"))
        self.lineEdit_2.setText(_translate("MainWindow", "LOW"))
        self.pushButton_2.setText(_translate("MainWindow", "HIGH"))
        self.label_3.setText(_translate("MainWindow", "Pin 1"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Input"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Output"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "PWM"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Servo"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Analog"))
        self.menuBegain.setTitle(_translate("MainWindow", "Begain"))
        self.menuPort.setTitle(_translate("MainWindow", "Port"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCOM1.setText(_translate("MainWindow", "COM1"))
        self.actionCOM2.setText(_translate("MainWindow", "COM2"))
        self.actionBoard.setText(_translate("MainWindow", "Board"))
        self.actionUser_guide.setText(_translate("MainWindow", "User guide"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

