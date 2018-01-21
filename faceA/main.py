# -*- coding:utf-8 -*-

import os, _thread, sys, json

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import pyqtSignal, QThread

from faceA import MyUtils
from faceA.ui.ui_source.Form_main import Ui_Form_main
from faceA.ui.Dia_alter import Alter_Dialog
from faceA.ui.Dia_doAllFile import DoAllFile_Dialog


class mainD(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_main()
        self.ui.setupUi(self)
        self.setWindowTitle("人脸属性识别系统")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # 禁止用户改变窗口大小

        # 定义几个按钮的槽连接
        self.ui.pushButton.clicked.connect(self.openfile_button_connect)
        self.ui.pushButton_2.clicked.connect(self.analysisCurPic_button_connect)
        self.ui.pushButton_3.clicked.connect(self.openUnProcesssedFile_button_connect)
        self.ui.pushButton_4.clicked.connect(self.openHaveDonedFile_button_connect)
        self.ui.pushButton_5.clicked.connect(self.doAllFile_button_connect)
        self.ui.pushButton_6.clicked.connect(self.showAllResults_button_connect)
        self.ui.pushButton_7.clicked.connect(self.stopShowResult_button_connect)

        # 初始化一些要用到的变量
        self.picpath = ''
        self.result = ''
        self.picnum_toshow=0
        self.picnum_haveshow=0
        self.undoPath = r'.\resource\pic_undo'
        self.havedonedPath = r'.\resource\pic_havedone'
        self.doallfilethread = None

    def showAllResults_button_connect(self):
        if not self.doallfilethread == None:
            if self.doallfilethread.thread_status == 1:
                self.doallfilethread.thread_status = 0
                self.ui.pushButton_6.setText("继续展示")
                return
            elif self.doallfilethread.thread_status == 0:
                self.doallfilethread.thread_status = 1
                self.ui.pushButton_6.setText("暂停展示")
                return

        self.picnum_haveshow=0
        self.picnum_toshow=int(len(os.listdir(self.havedonedPath))/2)
        self.ui.label_4.setText(str(self.picnum_haveshow)+"/"+str(self.picnum_toshow))

        self.doallfilethread = showFileThread()

        self.ui.pushButton_6.setText("暂停展示")
        self.doallfilethread.shownew_signal.connect(self.showPicAndResult_connect)
        self.doallfilethread.setPath(self.havedonedPath)
        self.doallfilethread.setPicSize(self.ui.label.width(), self.ui.label.height())
        self.doallfilethread.start()

    def stopShowResult_button_connect(self):
        if not self.doallfilethread == None:
            self.ui.pushButton_6.setText("展示识别结果")
            self.picnum_haveshow = 0
            self.ui.label_4.setText(str(self.picnum_haveshow) + "/" + str(self.picnum_toshow))
            self.doallfilethread.thread_status = -1

    def openfile_button_connect(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', './')
        self.picpath = fname[0]

        if not (self.picpath[-4:] == '.png' or self.picpath[-4:] == '.jpg'):
            Alter_Dialog("警报", "请选择jpg或者png文件").exec_()
            return

        png = QPixmap(self.picpath)

        if png.isNull():
            Alter_Dialog("警报", "图片转换出现错误").exec_()
            return

        # 按与控件的比例，对图像进行缩放
        if png.width() / png.height() > self.ui.label.width() / self.ui.label.height():
            png = png.scaled(self.ui.label.width(), png.height() * self.ui.label.width() / png.width())
        else:
            png = png.scaledToHeight(png.width() * self.ui.label.height() / png.height(), self.ui.label.height())
        # 把图像放到控件中显示
        self.ui.label.setPixmap(png)

    def analysisCurPic_button_connect(self):
        if not (self.picpath[-4:] == '.png' or self.picpath[-4:] == '.jpg'):
            Alter_Dialog("警报", "请选择jpg或者png文件").exec_()
        else:
            try:
                self.showResult(MyUtils.getPicAnalysisResult(self.picpath))
            except Exception as e:
                Alter_Dialog(e.__str__()).exec()

    def openUnProcesssedFile_button_connect(self):
        os.system("explorer.exe %s" % self.undoPath)

    def openHaveDonedFile_button_connect(self):
        os.system("explorer.exe %s" % self.havedonedPath)

    def doAllFile_button_connect(self):
        dfb = DoAllFile_Dialog("图片识别中……")
        dfb.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinimizeButtonHint)
        _thread.start_new_thread(self.doAllFileinThread_threadfunction, (dfb, self.havedonedPath, self.undoPath))
        dfb.exec_()

    def showPicAndResult_connect(self, pic, result, picpath):
        self.ui.label.setPixmap(pic)
        self.picpath = picpath
        self.showResult(result)
        self.picnum_haveshow+=1
        self.ui.label_4.setText(str(self.picnum_haveshow)+"/"+str(self.picnum_toshow))
        if(self.picnum_haveshow==self.picnum_toshow):
            self.ui.pushButton_6.setText("展示识别结果")

    def doAllFileinThread_threadfunction(self, dfb, havedonedPath, undoPath):
        i = (int)(len(os.listdir(havedonedPath)) / 2)
        j = i
        num_undo = len(os.listdir(undoPath))
        if num_undo == 0:
            dfb.ui.progressBar.hide()
            dfb.ui.label.setText("没有文件待处理")
            dfb.ui.pushButton.show()
            return

        for root, dirs, files in os.walk(self.undoPath):
            for file in files:
                filepath = os.path.join(root, file)
                MyUtils.getLogger(__name__).info("读取 " + filepath)
                # 判断用户选择的文件是否符合要求，这里只支持png和jpg
                if len(filepath) < 4 or (not (filepath[-4:] == '.png' or filepath[-4:] == '.jpg')):
                    MyUtils.getLogger(__name__).warn(file + "不是jpg或者png文件")
                else:
                    result = ""
                    try:
                        result = MyUtils.getPicAnalysisResult(filepath)
                    except Exception as e:
                        MyUtils.getLogger(__name__).error(e.__str__())

                    os.rename(filepath, os.path.join(self.havedonedPath, str(i)) + filepath[-4:])
                    try:
                        fjson = open(os.path.join(self.havedonedPath, str(i)) + ".json", 'w')
                        fjson.write(result)
                        i += 1
                        fjson.close()
                    except Exception as e:
                        MyUtils.getLogger(__name__).error(e.__str__() + " open " + self.havedonedPath + " failed")

                dfb.ui.progressBar.setValue(100 * (i - j) / num_undo)
        dfb.ui.progressBar.setValue(100)
        dfb.ui.label.setText("识别已经完成")
        dfb.ui.pushButton.show()

    # 这个函数被两个内部函数用到了,在这里写重试申请
    def showResult(self, result):

        resultobj = None
        try:
            resultobj = json.JSONDecoder().decode(result)
        except Exception as e:
            MyUtils.getLogger(__name__).error(e.__str__())
        if (resultobj == None or 'error_message' in resultobj):
            try:
                result = MyUtils.getPicAnalysisResult(self.picpath)
                resultobj = json.JSONDecoder().decode(result)
            except Exception as e:
                MyUtils.getLogger(__name__).error(e.__class__ + e.__str__())

        if (resultobj == None):
            text = '数据请求失败'
            self.ui.label_2.setText(text)
            return
        elif ('error_message' in resultobj):
            text = "error_message:" + resultobj['error_message']['value']
            self.ui.label_2.setText(text)
            return

        text = ''
        j = 0
        try:
            for i in resultobj['faces']:
                text += "人物" + str(j) + ":\n"
                j += 1
                att = i['attributes']
                text += "age: " + str(att['age']['value'])
                text += "\n性别: " + ("女" if att['gender']['value'] == "Female" else "男")
                text += "\n人种: "
                if att['ethnicity']['value'] == 'None':
                    text += "亚洲人"
                elif att['ethnicity']['value'] == 'White':
                    text += "白人"
                else:
                    text += "黑人"

                text += "\n笑容程度: " + str(att['smile']['value']) + "\t阈值：" + str(att['smile']['threshold']) + "\n"
                if att['glass']['value'] == 'None':
                    text += "没有佩戴眼镜"
                elif att['glass']['value'] == 'Dark':
                    text += "佩戴墨镜"
                else:
                    text += "佩戴普通眼镜"
                text += '\n'
        except Exception as e:
            MyUtils.getLogger(__name__).error(e.__class__ + e.__str__())

        self.ui.label_2.setText(text)


class showFileThread(QThread):
    shownew_signal = pyqtSignal(object, str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        # 三种状态 -1 是终止，0是等待，1是运行
        self.thread_status = 1

    def setPath(self, path):
        self.havedonedPath = path

    def setPicSize(self, width, height):
        self.wid = width
        self.he = height

    def run(self):
        for root, dirs, files in os.walk(self.havedonedPath):
            for file in files:
                if self.thread_status == 1:
                    filepath = os.path.join(root, file)
                    if not (filepath[-4:] == '.png' or filepath[-4:] == '.jpg'):
                        pass
                    else:
                        pic = QPixmap(filepath)
                        if pic.isNull():
                            MyUtils.getLogger(__name__).error("警报", "图片转换出现错误")
                        else:
                            # 按与控件的比例，对图像进行缩放
                            if pic.width() / pic.height() > self.wid / self.he:
                                pic = pic.scaled(self.wid, pic.height() * self.wid / pic.width())
                            else:
                                pic = pic.scaledToHeight(pic.width() * self.he / pic.height(), self.he)
                        try:
                            file = open(filepath[:-4] + '.json')
                            result = file.read()
                            file.close()
                            self.shownew_signal.emit(pic, result, filepath)
                        except Exception as e:
                            MyUtils.getLogger(__name__).error(e.__str__() + " open " + self.havedonedPath + " failed")

                        self.sleep(3)
                elif self.thread_status == -1:
                    return
                else:
                    while self.thread_status == 0:
                        self.sleep(5)
        self.thread_status = -1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = mainD()
    ex.show()
    sys.exit(app.exec_())

"""
@author:raymond
@file:main.py
@time:2018/1/1611:45
"""
