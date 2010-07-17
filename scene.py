import sys, random
from PyQt4.QtGui import QGraphicsScene, QPen, QColor, QBrush
from PyQt4.QtCore import Qt

class Scene( QGraphicsScene ):
	def __init__( self ):

		QGraphicsScene.__init__( self )

		self.setSceneRect( 0, 0, 1024, 768 )

	def lotsoflines( self ):
		pen = QPen( QBrush( QColor( 0, 0, 150, 50 ) ),
			15.0,
			Qt.SolidLine,
			Qt.RoundCap,
			Qt.BevelJoin
		)

		w = self.width()
		h = self.height()

		for i in range( 5 ):
			x1 = random.randint(1, int(w - 1))
			y1 = random.randint(1, int(h - 1))
			x2 = random.randint(1, int(w - 1))
			y2 = random.randint(1, int(h - 1))
			self.addLine(x1, y1, x2, y2, pen)

	def drawPoint( self, x, y ):
		pen = QPen( QBrush( QColor( 0, 0, 150, 50 ) ),
			15.0,
			Qt.SolidLine,
			Qt.RoundCap,
			Qt.BevelJoin
		)

		print([x,y])
		self.addLine( x, y, x+1, y+1, pen )
