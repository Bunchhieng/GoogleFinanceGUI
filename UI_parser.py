# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Untitled.ui'
#
# Created: Thu Apr 30 00:24:46 2015
# by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import csv
from PyQt4 import QtCore, QtGui
from DirDialog import DirDialog
from Parser import DataParser

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_GoogleFinance(object):
    SYMBOL = None
    MARKET = None

    def __init__(self):
        super(Ui_GoogleFinance, self).__init__()
        self.setupUi(self)

    def setupUi(self, GoogleFinance):
        GoogleFinance.setObjectName(_fromUtf8("GoogleFinance"))
        GoogleFinance.resize(364, 195)
        self.btn_open_dir = QtGui.QPushButton(GoogleFinance)
        self.btn_open_dir.setGeometry(QtCore.QRect(10, 111, 121, 41))
        self.btn_open_dir.setObjectName(_fromUtf8("btn_open_dir"))
        self.btn_open_dir.clicked.connect(self.open_dir)
        # parsing button
        self.btn_parse = QtGui.QPushButton(GoogleFinance)
        self.btn_parse.setGeometry(QtCore.QRect(130, 151, 110, 41))
        self.btn_parse.setObjectName(_fromUtf8("btn_parse"))
        self.btn_parse.clicked.connect(self.OnClicked)
        # Group of radio button
        self.groupBox = QtGui.QGroupBox(GoogleFinance)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 111, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.nyse = QtGui.QRadioButton(self.groupBox)
        self.nyse.setGeometry(QtCore.QRect(10, 30, 97, 18))
        self.nyse.setObjectName(_fromUtf8("nyse"))
        self.nasdaq = QtGui.QRadioButton(self.groupBox)
        self.nasdaq.setGeometry(QtCore.QRect(10, 60, 97, 18))
        self.nasdaq.setObjectName(_fromUtf8("nasdaq"))
        self.csv_check = QtGui.QCheckBox(GoogleFinance)
        self.csv_check.setGeometry(QtCore.QRect(180, 70, 121, 18))
        self.csv_check.setObjectName(_fromUtf8("csv_check"))
        self.csv_check.setChecked(True);
        # required symbol to parse
        self.symbol = QtGui.QComboBox(GoogleFinance)
        self.symbol.setGeometry(QtCore.QRect(150, 40, 200, 21))
        self.symbol.setObjectName(_fromUtf8("symbol"))
        with open("symbols.csv", "rU") as sym:
            reader = csv.reader(sym, dialect='excel')
            for row in reader:
                self.symbol.addItem(row[0] + " - " + row[1])

        self.label = QtGui.QLabel(GoogleFinance)
        self.label.setGeometry(QtCore.QRect(160, 22, 56, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.output_dir = QtGui.QLineEdit(GoogleFinance)
        self.output_dir.setGeometry(QtCore.QRect(130, 120, 211, 21))
        self.output_dir.setObjectName(_fromUtf8("output_dir"))
        self.label_2 = QtGui.QLabel(GoogleFinance)
        self.label_2.setGeometry(QtCore.QRect(140, 200, 56, 13))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        # Error output
        self.error = QtGui.QLabel("", self)
        self.error.move(200, 90)
        self.error.setStyleSheet('color: red')
        self.retranslateUi(GoogleFinance)
        QtCore.QMetaObject.connectSlotsByName(GoogleFinance)

    """
    OnClicked event when the parse button is clicked
    :return csv file with the specified directory
    """

    def OnClicked(self):
        self.error.clear()
        if self.nyse.isChecked():
            self.MARKET = str(self.nyse.objectName())
        elif self.nasdaq.isChecked():
            self.MARKET = str(self.nasdaq.objectName())
        else:
            self.error.setText("Fill in the box!")

        if self.csv_check.isChecked():
            pass
        else:
            self.error.setText("Fill in the box!")
        self.dash = str(self.symbol.currentText()).find('-')
        self.text = self.symbol.currentText()[:self.dash]
        self.SYMBOL = str(self.text)
        print self.MARKET, self.SYMBOL
        dp = DataParser(self.MARKET, self.SYMBOL)
        print dp.GOOGLE_FINANCE_URL
    """
    Open "~" aka home directory when user click
    then set dir name to line edit.
    """

    def open_dir(self):
        dir = DirDialog()
        self.output_dir.setText(dir.foldername)

    def retranslateUi(self, GoogleFinance):
        GoogleFinance.setWindowTitle(_translate("GoogleFinance", "Google Finance Parser", None))
        self.btn_open_dir.setText(_translate("GoogleFinance", "Output Directory", None))
        self.btn_parse.setText(_translate("GoogleFinance", "Parsing", None))
        self.groupBox.setTitle(_translate("GoogleFinance", "Stock Exchange", None))
        self.nyse.setText(_translate("GoogleFinance", "NYSE", None))
        self.nasdaq.setText(_translate("GoogleFinance", "NASDAQ", None))
        self.csv_check.setText(_translate("GoogleFinance", "Save as csv file", None))
        self.label.setText(_translate("GoogleFinance", "Symbol :", None))

