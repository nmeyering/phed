import sys, random
from PyQt4.QtGui import QGraphicsScene, QPen, QColor, QBrush
from PyQt4.QtCore import Qt, QPoint, QPointF, QLineF
from tux import Tux

class Scene( QGraphicsScene ):
	def __init__( self ):
		QGraphicsScene.__init__( self )

		self.setSceneRect( 0, 0, 1024, 768 )

		self.pen = QPen( QBrush( QColor( 0, 0, 150, 255 ) ),
			5.0,
			Qt.SolidLine,
			Qt.RoundCap,
			Qt.BevelJoin
		)


	def lotsoflines( self ):
		w = self.width()
		h = self.height()

		for i in range( 5 ):
			x1 = random.randint(1, int(w - 1))
			y1 = random.randint(1, int(h - 1))
			x2 = random.randint(1, int(w - 1))
			y2 = random.randint(1, int(h - 1))
			self.addLine(x1, y1, x2, y2, self.pen)

	def drawPoint( self, point ):
		point2 = QPointF( point.x() + 1, point.y() + 1 )

		self.addLine( 
			QLineF( 
				point, point2 ),
			self.pen )

	def drawLine( self, line ):
		self.addLine( line, self.pen )
	
	def drawTux( self, point ):
		tux = Tux()
		tux.setPos( point - QPointF( 128.0, 128.0 ) )
		self.addItem( tux )

	def setColor( self, color ):
		self.pen.setColor( color )
	
	def setWidth( self, width ):
		self.pen.setWidth( width )
	
	def cleanup( self ):
		print('Cleared {c} items.'.format(
			c = len( self.items() ) ) )
		self.clear()
