#!/usr/bin/python
import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QTimer, QTime
from window import Window

def main():
	app = QApplication( sys.argv )
	window = Window()
	window.show()

	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
