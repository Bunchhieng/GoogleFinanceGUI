__author__ = 'Bunchhieng'

import sys
from PyQt4 import QtGui, QtCore
from UI_parser import Ui_GoogleFinance

class MyApp(QtGui.QMainWindow, Ui_GoogleFinance):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_GoogleFinance.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())