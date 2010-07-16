#!/usr/bin/python3
import sys, os, random
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QFileDialog, QMainWindow, QGraphicsView, QPen, QColor, QBrush
from PyQt4.QtCore import Qt
from ui_phed import Ui_EditWindow
from scene import Scene

class Window( QMainWindow ):

	def __init__( self ):
		QMainWindow.__init__( self )
		
		self.ui = Ui_EditWindow()
		self.ui.setupUi( self )
		
		button = self.ui.pushButton

		button.clicked.connect( self.foo )

		self.view = self.ui.graphicsView
		self.scene = Scene()
		self.view.setScene( self.scene )
		self.view.setDragMode( QGraphicsView.ScrollHandDrag )

	def foo( self ):
		pen = QPen( QBrush( QColor( 0, 0, 150, 50 ) ),
			15.0,
			Qt.SolidLine,
			Qt.RoundCap,
			Qt.BevelJoin
		)

		w = self.scene.width()
		h = self.scene.height()

		for i in range( 5 ):
			x1 = random.randint(1, int(w - 1))
			y1 = random.randint(1, int(h - 1))
			x2 = random.randint(1, int(w - 1))
			y2 = random.randint(1, int(h - 1))
			self.scene.addLine(x1, y1, x2, y2, pen)

app = QApplication( sys.argv )
window = Window()
window.show()
sys.exit(app.exec_())
