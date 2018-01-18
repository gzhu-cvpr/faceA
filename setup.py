# -*- coding:utf-8 -*-
#用来生成发行包的
#当所写程序是一个库的时候，此配置生成的文件 用来把库导入到用户环境中
#当所写程序是一个可执行程序时候，此用来为可执行程序搭建环境，或者生成打包后的可执行文件
#目前此文件 是 为了打包成exe ，工作TODO中

import sys
from cx_Freeze import setup,Executable

build_exe_options = {'packages': [], 'excludes': []}

setup(
      name='faceA',
      version='1.0',
      description='无',
      option={'build_exe':build_exe_options},
      executables=[Executable(r'.\faceA\main.py',targetName='faceA.exe')]
      )


"""
@author:raymond

@file:setup.py
@time:2018/1/1613:17
"""