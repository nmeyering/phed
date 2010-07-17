#!/usr/bin/python
import sys, os, random
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QFileDialog, QMainWindow, QGraphicsView, QPen, QColor, QBrush, QWidget
from PyQt4.QtCore import Qt
from ui_phed import Ui_EditWindow
from scene import Scene

class Window( QMainWindow ):

	def __init__( self ):
		QMainWindow.__init__( self )
		
		self.ui = Ui_EditWindow()
		self.ui.setupUi( self )

		scene = Scene()
		
		view = self.ui.phedView
		view.setScene( scene )
		
		button = self.ui.pushButton
		button.clicked.connect( scene.lotsoflines )

app = QApplication( sys.argv )
window = Window()
window.show()
sys.exit(app.exec_())
