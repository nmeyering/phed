#!/usr/bin/python
import sys, os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QTimer, QTime
from window import Window

app = QApplication( sys.argv )
#Qt.qsrand( QTime(0,0,0).secsTo( QTime.currentTime() ) )
window = Window()
window.show()

timer = QTimer()
timer.timeout.connect( window.view.rotate1 )
timer.start( 30 )

sys.exit(app.exec_())
