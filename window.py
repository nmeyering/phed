import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QColorDialog
from ui_phed import Ui_EditWindow
from scene import Scene

class Window( QMainWindow ):

	def __init__( self ):
		QMainWindow.__init__( self )
		
		self.ui = Ui_EditWindow()
		self.ui.setupUi( self )

		self.edit = self.ui.edit
		self.scene = self.edit.scene()

		button = self.ui.pushButton
		clearbutton = self.ui.clearButton
		spinBox = self.ui.spinBox

		button.clicked.connect( self.edit.chooseColor )
		clearbutton.clicked.connect( self.edit.cleanup )
		spinBox.valueChanged.connect( (lambda : self.edit.setWidth(
			spinBox.value() ) ) )

		self.ui.actionOpen.triggered.connect( self.edit.openFile )
		self.ui.actionSave.triggered.connect( self.edit.saveFile )
