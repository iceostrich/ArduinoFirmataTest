import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainUI import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        self.timer = QBasicTimer()
        self.timer.start(1000, self)


    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.lcdNumber.display(time.strftime("%X",time.localtime()))
        else:
            super(WigglyWidget, self).timerEvent(event)

    def slot1(self):
        self.lcdNumber.display(1000)



if __name__ == "__main__":
    import sys
    import pyfirmata

    app = QtWidgets.QApplication(sys.argv)
    MyShow = MyWindow()
    MyShow.show()
    sys.exit(app.exec_())
