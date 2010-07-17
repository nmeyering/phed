#!/usr/bin/python
import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from window import Window
	
app = QApplication( sys.argv )
window = Window()
window.show()
sys.exit(app.exec_())
