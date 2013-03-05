rpchm-py
========

axure rp 生成CHM文件的时候，某些地方会因为编码问题而产生乱码。

解决方法参考这个：
http://www.webppd.com/viewthread.php?tid=5023&highlight=chm

1、把.hhc 和 .hhp 这两个文件改成gbk编码
2、修改.hhp文件的语言设置从 0x409 改成 0x084：
Language=0x804
3、用hhc.exe命令重新生成chm文件

原文用的是vbs，我把它改成了 pyqt的，有个图像界面赶紧更好用些。

2013.03.06 
