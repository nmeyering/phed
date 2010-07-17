from PyQt4.QtGui import QGraphicsView
from PyQt4.QtCore import QPoint, QPointF
from scene import Scene

class View( QGraphicsView ):
	def __init__( self, parent = None, scene = None ):
		QGraphicsView.__init__( self, parent )

		scene = Scene()
		self.setScene( scene )

		self.setDragMode( QGraphicsView.ScrollHandDrag )
	
	def mousePressEvent( self, event ):
		point = self.mapToScene(
			QPoint( event.x(), event.y() ) )
		self.scene().drawPoint( point )
