#!/usr/bin/python3
import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QFileDialog, QMainWindow
from ui_phed import Ui_EditWindow
from scene import Scene

class Window( QMainWindow ):

	def __init__( self ):
		QMainWindow.__init__( self )
		
		self.ui = Ui_EditWindow()
		self.ui.setupUi( self )

		self.ui.graphicsView.setScene( Scene() )


app = QApplication( sys.argv )
window = Window()
window.show()
sys.exit(app.exec_())
