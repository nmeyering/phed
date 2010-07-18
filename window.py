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

		self.view = self.ui.phedView
		self.scene = self.view.scene()

		button = self.ui.pushButton
		clearbutton = self.ui.clearButton
		spinBox = self.ui.spinBox

		button.clicked.connect( self.chooseColor )
		clearbutton.clicked.connect( self.scene.clear )
		spinBox.valueChanged.connect( self.updateWidth )

	def chooseColor( self ):
		col = QColorDialog( self ).getColor()
		self.scene.setColor( col )

	def updateWidth( self ):
		self.scene.setWidth( self.ui.spinBox.value() )
