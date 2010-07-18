from PyQt4.QtGui import QGraphicsView
from PyQt4.QtCore import QPoint, QPointF, QLineF
from scene import Scene

class View( QGraphicsView ):
	def __init__( self, parent = None, scene = None ):
		QGraphicsView.__init__( self, parent )

		scene = Scene()
		self.setScene( scene )
		self.lastPoint = QPointF()

		self.setDragMode( QGraphicsView.ScrollHandDrag )
	
	def mousePressEvent( self, event ):
		point = self.mapToScene(
			QPoint( event.x(), event.y() ) )
		self.scene().drawPoint( point )
		self.lastPoint = point
	
	def mouseMoveEvent( self, event ):
		point = self.mapToScene(
			QPoint( event.x(), event.y() ) )
		self.scene().drawLine( QLineF(
			self.lastPoint,
			point ) )
		self.lastPoint = point
