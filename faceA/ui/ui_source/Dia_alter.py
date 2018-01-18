# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dia_alter.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dia_alter(object):
    def setupUi(self, Dia_alter):
        Dia_alter.setObjectName("Dia_alter")
        Dia_alter.setWindowModality(QtCore.Qt.NonModal)
        Dia_alter.resize(366, 159)
        self.label = QtWidgets.QLabel(Dia_alter)
        self.label.setGeometry(QtCore.QRect(50, 20, 261, 71))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dia_alter)
        self.pushButton.setGeometry(QtCore.QRect(140, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dia_alter)
        QtCore.QMetaObject.connectSlotsByName(Dia_alter)

    def retranslateUi(self, Dia_alter):
        _translate = QtCore.QCoreApplication.translate
        Dia_alter.setWindowTitle(_translate("Dia_alter", "Dialog"))
        Dia_alter.setToolTip(_translate("Dia_alter", "<html><head/><body><p><br/></p></body></html>"))
        Dia_alter.setWhatsThis(_translate("Dia_alter", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Dia_alter", "确认"))

