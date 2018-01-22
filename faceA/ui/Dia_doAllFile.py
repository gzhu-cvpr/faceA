# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QDialog

from faceA.ui.ui_base.Dia_PBar import Ui_Dia_PBar

"""
显示处理事件进度的通用Dialog
"""
class DoAllFile_Dialog(QDialog):
    def __init__(self,msg=""):
        super().__init__()
        self.ui = Ui_Dia_PBar()
        self.ui.setupUi(self)
        self.ui.label.setText(msg)
        self.setWindowTitle("稍等")
        self.ui.pushButton.hide()
        self.ui.pushButton.clicked.connect(self.cl)

    def cl(self):
        self.close()





"""
@author:raymond
@file:Dia_doAllFile.py
@time:2018/1/1612:57
"""