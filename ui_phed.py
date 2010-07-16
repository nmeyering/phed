# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phed.ui'
#
# Created: Fri Jul 16 17:02:40 2010
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_EditWindow(object):
    def setupUi(self, EditWindow):
        EditWindow.setObjectName("EditWindow")
        EditWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(EditWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.graphicsView.setObjectName("graphicsView")
        EditWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(EditWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        EditWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(EditWindow)
        self.statusbar.setObjectName("statusbar")
        EditWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(EditWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(EditWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(EditWindow)
        QtCore.QMetaObject.connectSlotsByName(EditWindow)

    def retranslateUi(self, EditWindow):
        EditWindow.setWindowTitle(QtGui.QApplication.translate("EditWindow", "phed", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("EditWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("EditWindow", "Open …", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("EditWindow", "Save …", None, QtGui.QApplication.UnicodeUTF8))

