#!/usr/bin/env python
#coding:utf8
from __future__ import division

"""
axure的chm生成工具
dehongliu@gmail.com 2013.03.05

axure rp软件生成chm文件的时候，左侧菜单会是乱码。
原因是微软的chm编译工具hhc.exe文件只能处理ansi格式的，
而rp生成的是utf8格式的，简单改改格式即可正常显示。
"""

"""
v1.0 - 能把axure rp生成的文件编译成chm文件
"""

#todo:

__version__ = "1.0"


from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

from PyQt4.QtGui import QMessageBox, QFileDialog, QDialog
from PyQt4.QtCore import QFile, QSettings, QVariant

import os, platform, stat, sys, time
from os import path
import time

from rpchm_dialog import *
import codecs

TMP_INIFILE_PATH = path.join(path.dirname(sys.argv[0].decode('gbk')), u'rpchm_tmp.ini')


if getattr(sys, 'frozen', None):        #Pyinstaller打包
    BASEDIR = sys._MEIPASS
else:
    BASEDIR = os.path.dirname(sys.argv[0].decode('gbk'))
    if BASEDIR == '':
        BASEDIR = '.'

BASEDIR = os.path.abspath(BASEDIR)
#print BASEDIR

class RpChmForm(QDialog):
    def __init__(self, parent=None):
        super(RpChmForm, self).__init__(parent)

        self.ui = Ui_RpChmDialog()
        self.ui.setupUi(self)
        self.setWindowTitle(u"chm生成工具 v%s" % (__version__))

        self.connect(self.ui.workPathButton, QtCore.SIGNAL('clicked()'), self.setWorkPath)

        self.settings_tmp = QtCore.QSettings(TMP_INIFILE_PATH, QtCore.QSettings.IniFormat)

        outpath = (unicode(self.settings_tmp.value("outPath").toString()) or os.getcwd().decode('gbk'))
        self.ui.workPathLabel.setText(outpath)

        self.connect(self.ui.buildButton, QtCore.SIGNAL("clicked()"), self.build)
        self.connect(self.ui.exitButton, QtCore.SIGNAL("clicked()"), self.close)


    def closeEvent(self, event):
        self.settings_tmp.setValue("outPath", QVariant(self.ui.workPathLabel.text()))
        event.accept()


    def about(self):
        QMessageBox.about(self, u"关于CHM生成工具",
            u"""<p>
            使用说明：<br>
            1. 选择工作目录<br>
            2. 点 "执行" 按钮<br><br>

            注意事项：<br>
            1. <br><br>

            2013.03.05 v%s </p>""" % (
            __version__))


    def setWorkPath(self):
        path = QFileDialog.getExistingDirectory(self,
                u"选择工作目录", self.ui.workPathLabel.text())
        if path:
            self.ui.workPathLabel.setText(unicode(QDir.toNativeSeparators(path)))

   
    #点击执行按钮
    #状态转变：执行 -> 停止 -> 执行 （如果没有完全停止，执行按钮不可用）
    def build(self):
        workpath = unicode(self.ui.workPathLabel.text())
        if not os.path.isdir(workpath):
            self.ui.textDescLabel.setText(u'工作目录不存在')

        hhcfile = None
        hhpfile = None

        os.chdir(workpath)
        ret = []
        files = os.listdir('.')
        for f in files:
            try:
                f =  f if isinstance(f, unicode) else f.decode('gbk')                
            except UnicodeDecodeError, e:
                f =  f if isinstance(f, unicode) else f.decode('utf8')     

            #print f           

            if f.endswith('.hhc'):
                hhcfile = f
            if f.endswith('.hhp'):
                hhpfile = f

        if hhcfile and hhpfile:
            #self.ui.textDescLabel.setText(hhpfile)
            pass
        else:
            self.ui.textDescLabel.setText(u"没有找到.hhc或.hhp文件，请确认是否已经生成。")
            return
            
        #把hhc文件从utf8改成gbk格式
        try:
            fr = codecs.open(hhcfile, 'r', 'utf-8')
            hhc = fr.read()
        except UnicodeDecodeError, e:
            pass
        except StandardError, e:
            self.ui.textDescLabel.setText(u"%s" % e)
            return
        else:
            fw = codecs.open(hhcfile, 'w', 'gbk')
            fw.write(hhc)       
            fw.close()
        finally:
            fr.close()

        #将hhp文件中的0x409(英文),改为0x804(中文)            
        try:
            fr = codecs.open(hhpfile, 'r', 'utf-8')
            hhp = fr.read()
            hhp = hhp.replace('=0x409 English', '=0x804 Chinese')
        except UnicodeDecodeError, e:
            pass
        except StandardError, e:
            self.ui.textDescLabel.setText(u"%s" % e)
            return
        else:
            fw = codecs.open(hhpfile, 'w', 'gbk')
            fw.write(hhp)
            fw.close()
        finally:
            fr.close()

        #用hhc.exe编译
        hhccmd = BASEDIR + '/HTML Help Workshop/hhc.exe'
        if not os.path.exists(hhccmd):
            self.ui.textDescLabel.setText(u"hhc.exe 命令不存在: %s" % hhccmd)

        args = [hhpfile]
        process = QtCore.QProcess()
        process.start(hhccmd, args)
        if process.waitForFinished(2 * 60 * 1000):
            ba = process.readAllStandardOutput()
            self.ui.textDescLabel.setText(unicode(QString(ba), 'gbk'))

        pass

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    APPPATH = unicode(app.applicationDirPath())
    app.setApplicationName(u"chm生成工具")
    form = RpChmForm()
    form.show()
    app.exec_()

