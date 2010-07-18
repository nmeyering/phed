from PyQt4.QtGui import QGraphicsView
from PyQt4.QtCore import QPoint, QPointF, QLineF, Qt
from scene import Scene

class View( QGraphicsView ):
	def __init__( self, parent = None, scene = None ):
		QGraphicsView.__init__( self, parent )

		scene = Scene()
		self.setScene( scene )
		self.lastPoint = QPointF()

		self.setDragMode( QGraphicsView.NoDrag )

		self.scribbling = False
	
	def mousePressEvent( self, event ):
		if event.button() == Qt.RightButton:
			point = self.mapToScene( event.pos() )
			self.lastPoint = point
			self.scribbling = True
		else:
			point = self.mapToScene( event.pos() )
			self.scene().drawTux( point )
	
	def mouseMoveEvent( self, event ):
		if ( event.buttons() & Qt.RightButton ) and self.scribbling:
			point = self.mapToScene( event.pos() )
			self.scene().drawLine( QLineF(
				self.lastPoint,
				point ) )
			self.lastPoint = point

	def mouseReleasedEvent( self, event ):
		if self.scribbling and event.button() == Qt.RightButton:
			point = self.mapToScene( event.pos() )
			self.scene().drawLine( QLineF(
				self.lastPoint,
				point ) )
			self.scribbling = false
	
	def rotate1( self ):
		self.rotate( 360/150 )
