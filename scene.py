import sys, random
from PyQt4.QtGui import QGraphicsScene, QPen, QColor, QBrush
from PyQt4.QtCore import Qt

class Scene( QGraphicsScene ):
	def __init__( self ):
		QGraphicsScene.__init__( self )

		self.setSceneRect( 0, 0, 640, 480 )
		#self.setBackgroundBrush( QBrush( QColor( "black" ) ) )

		self.addText( "Hello, World!" )

		pen = QPen( QColor( 255, 0, 0 ) )
		self.addLine( 0, 0, 100, 30,
			pen )


		print( len( self.items() ) )
