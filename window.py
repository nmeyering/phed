import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow
from ui_phed import Ui_EditWindow
from scene import Scene

class Window( QMainWindow ):

	def __init__( self ):
		QMainWindow.__init__( self )
		
		self.ui = Ui_EditWindow()
		self.ui.setupUi( self )

		view = self.ui.phedView
		scene = view.scene()
		
		button = self.ui.pushButton
		button.clicked.connect( scene.lotsoflines )

