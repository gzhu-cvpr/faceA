# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dia_PBar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dia_PBar(object):
    def setupUi(self, Dia_PBar):
        Dia_PBar.setObjectName("Dia_PBar")
        Dia_PBar.resize(391, 181)
        self.progressBar = QtWidgets.QProgressBar(Dia_PBar)
        self.progressBar.setGeometry(QtCore.QRect(70, 60, 261, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Dia_PBar)
        self.label.setGeometry(QtCore.QRect(120, 100, 181, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dia_PBar)
        self.pushButton.setGeometry(QtCore.QRect(160, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dia_PBar)
        QtCore.QMetaObject.connectSlotsByName(Dia_PBar)

    def retranslateUi(self, Dia_PBar):
        _translate = QtCore.QCoreApplication.translate
        Dia_PBar.setWindowTitle(_translate("Dia_PBar", "Dialog"))
        self.pushButton.setText(_translate("Dia_PBar", "确定"))

