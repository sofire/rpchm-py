# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rpchm_dialog.ui'
#
# Created: Tue Mar 05 21:42:15 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RpChmDialog(object):
    def setupUi(self, RpChmDialog):
        RpChmDialog.setObjectName(_fromUtf8("RpChmDialog"))
        RpChmDialog.resize(484, 430)
        RpChmDialog.setWindowTitle(_fromUtf8(""))
        self.verticalLayout_2 = QtGui.QVBoxLayout(RpChmDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(RpChmDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.workPathLabel = QtGui.QLabel(RpChmDialog)
        self.workPathLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.workPathLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.workPathLabel.setText(_fromUtf8(""))
        self.workPathLabel.setObjectName(_fromUtf8("workPathLabel"))
        self.horizontalLayout.addWidget(self.workPathLabel)
        self.workPathButton = QtGui.QPushButton(RpChmDialog)
        self.workPathButton.setObjectName(_fromUtf8("workPathButton"))
        self.horizontalLayout.addWidget(self.workPathButton)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textDescLabel = QtGui.QLabel(RpChmDialog)
        self.textDescLabel.setFrameShape(QtGui.QFrame.Panel)
        self.textDescLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.textDescLabel.setText(_fromUtf8(""))
        self.textDescLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textDescLabel.setObjectName(_fromUtf8("textDescLabel"))
        self.verticalLayout.addWidget(self.textDescLabel)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.buildButton = QtGui.QPushButton(RpChmDialog)
        self.buildButton.setObjectName(_fromUtf8("buildButton"))
        self.horizontalLayout_4.addWidget(self.buildButton)
        self.exitButton = QtGui.QPushButton(RpChmDialog)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.horizontalLayout_4.addWidget(self.exitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(RpChmDialog)
        QtCore.QMetaObject.connectSlotsByName(RpChmDialog)

    def retranslateUi(self, RpChmDialog):
        self.label_2.setText(_translate("RpChmDialog", "工作目录：", None))
        self.workPathButton.setText(_translate("RpChmDialog", "选择目录", None))
        self.buildButton.setText(_translate("RpChmDialog", "编译", None))
        self.exitButton.setText(_translate("RpChmDialog", "退出", None))

