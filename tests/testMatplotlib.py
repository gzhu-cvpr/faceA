# -*- coding:utf-8 -*-
from numpy.ma import array
from pylab import *
from PIL import  Image
import json
import os

filepath=r'D:\work\Github\faceA\tests'
file=open(os.path.join(filepath,'7.json'))
filestr=file.read()

im=array(Image.open(os.path.join(filepath,'7.jpg')))

fileobj=json.JSONDecoder().decode(filestr)

x=[]
y=[]

for i in fileobj['faces'][0]['landmark']:
    x.append(fileobj['faces'][0]['landmark'][i]['x'])
    y.append(fileobj['faces'][0]['landmark'][i]['y'])

imshow(im)
plt.scatter(x, y, s=1, marker='o')
axis('off')

#detection
rect = plt.Rectangle((fileobj['faces'][0]['face_rectangle']['left'], fileobj['faces'][0]['face_rectangle']['top']),
                     fileobj['faces'][0]['face_rectangle']['width'], fileobj['faces'][0]['face_rectangle']['height'],
                     facecolor='none', ec='b')
plt.gca().add_patch(rect)
show()


"""
@author:raymond
@file:testMatplotlib.py
@time:2018/1/2211:09
"""