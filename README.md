## Description：
这是一个基于pyqt的gui客户端程序，主要用来展示人脸属性识别的结果。目前调用了face++旷视公司的接口，此后会改造成，调用自己队伍训练结果的接口。

## Project structure:
``` proj structure
│  AUTHORS  
│  CONTRIBUTING.md  
│  LICENSE  
│  Makefile  
│  README.md  
│  requirements.txt  
│  setup.py  
│  todolist  
├─dist                  放置发行版  
├─docs                  放置说明文档   
├─examples              放置样例，放置运行结果的picture  
├─extras                放置额外文件，在此项目无实际作用  
├─faceA  
│  │  main.py  
│  │  MyException.py  
│  │  MyUtils.py  
│  ├─logs              放置log文件  
│  ├─resource  
│  │  ├─pic_havedone  
│  │  ├─pic_undo  
│  │  └─usr_save  
│  └─ui  ui模块  
│      ├─ui_base       放置 qt designer的布局文件  
│      ├─ui_source     放置qtuic自动生成的文件  
│      │  │  Dia_alter.py  
│      │  │  Dia_PBar.py  
│      │  │  Form_main.py  
│
├─scripts               放置可执行文件  
└─tests                 放置测试样例  

```

  为了避免项目更加复杂，减去了一些目录模板，但是为了以后的项目架构，做出说明（这个项目README简直就是给我以后自己看的，逃）

## 目录额外说明：
不需要network目录 因为没有复杂的网络操作  
不需要dba目录，因为没有数据库。  
不需要examples。因为这里不是库，本身具有程序实现，不需要例子   
dist是发行版的文件夹  


## The Docs Link:
[TODOLIST](https://github.com/ThomasRaymond/faceA/blob/master/docs/todolist)

## Installation：
### Requirrments
* python 3.0+
* requests (>2.13.0)
* PyQt5(>5.8.0)

### install and run
```bash
pip install -r requirements.txt
cd  faceA/faceA
python main.py  
```

## How to use：
You can upload your pic which you want to get the information about.   
And then the program will show you the result after click the button.    
The result will just like  
[Example:Lenna.png](https://github.com/ThomasRaymond/faceA/blob/master/examples/testpic.png)

<p align='center'>
<img src='examples/testpic.png' title='Face Attributes Recognition example' style='max-width:600px'></img>
</p>

