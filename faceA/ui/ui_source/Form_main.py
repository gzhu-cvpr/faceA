# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_main(object):
    def setupUi(self, Form_main):
        Form_main.setObjectName("Form_main")
        Form_main.resize(919, 468)
        self.label = QtWidgets.QLabel(Form_main)
        self.label.setGeometry(QtCore.QRect(240, 60, 271, 351))
        self.label.setStyleSheet("background-color:White")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Form_main)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 160, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form_main)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 210, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(Form_main)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 320, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(Form_main)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(Form_main)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 260, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(Form_main)
        self.pushButton.setGeometry(QtCore.QRect(40, 60, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form_main)
        self.label_2.setGeometry(QtCore.QRect(600, 70, 221, 331))
        self.label_2.setStyleSheet("background-color:White")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form_main)
        self.label_3.setGeometry(QtCore.QRect(560, 60, 281, 351))
        self.label_3.setStyleSheet("background-color:White")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form_main)
        self.label_4.setGeometry(QtCore.QRect(440, 20, 311, 21))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton_7 = QtWidgets.QPushButton(Form_main)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 370, 121, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_6.raise_()
        self.pushButton_2.raise_()
        self.pushButton_5.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.pushButton_7.raise_()

        self.retranslateUi(Form_main)
        QtCore.QMetaObject.connectSlotsByName(Form_main)

    def retranslateUi(self, Form_main):
        _translate = QtCore.QCoreApplication.translate
        Form_main.setWindowTitle(_translate("Form_main", "Form"))
        self.pushButton_3.setText(_translate("Form_main", "打开待识别文件夹"))
        self.pushButton_4.setText(_translate("Form_main", "打开识别结果文件夹"))
        self.pushButton_6.setText(_translate("Form_main", "展示识别结果"))
        self.pushButton_2.setText(_translate("Form_main", "识别当前图片"))
        self.pushButton_5.setText(_translate("Form_main", "处理所有待识别图片"))
        self.pushButton.setText(_translate("Form_main", "选择要识别的图片"))
        self.pushButton_7.setText(_translate("Form_main", "结束展示"))

