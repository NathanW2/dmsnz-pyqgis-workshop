# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_templatedock.ui'
#
# Created: Fri Sep 18 15:25:40 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(309, 309)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.dockWidgetContents)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_2 = QtGui.QGridLayout(self.page)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton = QtGui.QPushButton(self.page)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.page)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.templatesList = QtGui.QListWidget(self.page)
        self.templatesList.setObjectName(_fromUtf8("templatesList"))
        self.gridLayout_2.addWidget(self.templatesList, 1, 0, 1, 2)
        self.applyButton = QtGui.QPushButton(self.page)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.gridLayout_2.addWidget(self.applyButton, 2, 0, 1, 2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "DockWidget", None))
        self.pushButton.setText(_translate("DockWidget", "Define New", None))
        self.pushButton_2.setText(_translate("DockWidget", "Delete", None))
        self.applyButton.setText(_translate("DockWidget", "Apply", None))

