# -*- coding:utf-8 -*-
from faceA import MyUtils

if __name__ == '__main__':
    MyUtils.geLogger("main").debug("debug1")
    MyUtils.geLogger("utils").debug("debug2")
    MyUtils.geLogger("exception").debug("debug3")
    # MyUtils.geLogger("main").error("error1")
    # MyUtils.geLogger("utils").error("error2")
    # MyUtils.geLogger("exception").error("error3")
    MyUtils.geLogger("main").info("info1")
    MyUtils.geLogger("utils").info("info2")
    MyUtils.geLogger("exception").info("info3")

"""
@author:raymond
@file:testlog.py
@time:2018/1/1916:38
"""