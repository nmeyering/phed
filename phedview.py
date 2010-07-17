from PyQt4.QtGui import QGraphicsView
from scene import Scene

class PhedView( QGraphicsView ):
	def __init__( self, parent = None ):
		QGraphicsView.__init__( self, parent )

		self.setDragMode( QGraphicsView.ScrollHandDrag )

