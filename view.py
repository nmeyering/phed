from PyQt4.QtGui import QGraphicsView
from scene import Scene

class View( QGraphicsView ):
	def __init__( self, parent = None, scene = None ):
		QGraphicsView.__init__( self, parent )

		scene = Scene()
		self.setScene( scene )

		self.setDragMode( QGraphicsView.ScrollHandDrag )
	
	def mousePressEvent( self, event ):
		self.scene().drawPoint(event.x(), event.y())