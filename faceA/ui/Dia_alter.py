# -*- coding:utf-8 -*-


from PyQt5.QtWidgets import QDialog

from faceA.ui.ui_base.Dia_alter import Ui_Dia_alter

"""
显示提示信息的通用Dialog
"""
class Alter_Dialog(QDialog):
    def __init__(self,name="",msg=""):
        super().__init__()
        self.ui = Ui_Dia_alter()
        self.ui.setupUi(self)
        self.ui.label.setText(msg)
        self.setWindowTitle(name)
        self.ui.pushButton.clicked.connect(self.close)


    def close(self):
        self.accept()


"""
@author:raymond
@file:Dia_alter.py
@time:2018/1/1612:57
"""