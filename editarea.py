import os
from PyQt4.QtGui import QGraphicsView, QPen, QBrush, QColor, QColorDialog, QFileDialog, QPixmap, QPainter
from PyQt4.QtCore import QPoint, QPointF, QLineF, Qt
from scene import Scene

class EditArea( QGraphicsView ):
	def __init__( self, parent = None, scene = None ):
		QGraphicsView.__init__( self, parent )

		scene = Scene()
		self.setScene( scene )
		self.lastPoint = QPointF()

		self.setDragMode( QGraphicsView.NoDrag )

		self.scribbling = False

		self.pen = QPen( QBrush( QColor( 0, 0, 150, 255 ) ),
			5.0,
			Qt.SolidLine,
			Qt.RoundCap,
			Qt.BevelJoin
		)

	def mousePressEvent( self, event ):
		if event.button() == Qt.RightButton:
			point = self.mapToScene( event.pos() )
			self.lastPoint = point
			self.scribbling = True
	
	def mouseMoveEvent( self, event ):
		if ( event.buttons() & Qt.RightButton ) and self.scribbling:
			point = self.mapToScene( event.pos() )
			self.drawLine( QLineF(
				self.lastPoint,
				point ) )
			self.lastPoint = point

	def mouseReleasedEvent( self, event ):
		if self.scribbling and event.button() == Qt.RightButton:
			point = self.mapToScene( event.pos() )
			self.drawLine( QLineF(
				self.lastPoint,
				point ) )
			self.scribbling = false

	def setColor( self, color ):
		self.pen.setColor( color )

	def setWidth( self, width ):
		self.pen.setWidth( width )

	def rotate( angle ):
		self.view.rotate( angle )

	def drawPoint( self, point ):
		point2 = QPointF( point.x() + 1, point.y() + 1 )

		self.scene().addLine( 
			QLineF( 
				point, point2 ),
			self.pen )

	def drawLine( self, line ):
		self.scene().addLine( line, self.pen )

	def cleanup( self ):
		print('Cleared {c} items.'.format(
			c = len( self.scene().items() ) ) )
		self.scene().clear()

	def chooseColor( self ):
		col = QColorDialog( self.parent() ).getColor()
		self.setColor( col )
	
	def openFile( self ):
		file = QFileDialog( self.parent() ).getOpenFileName(
			self,
			"Open Image",
			os.curdir,
			"Image Files (*.png *.jpg *.tga *.bmp);;All Files (*.*)"
		)
		self.scene().addPixmap(
			QPixmap( file )
		)
	def saveFile( self ):
#		dialog = QFileDialog( self.parent() )
#		dialog.setFileMode( QFileDialog.AnyFile )
#		dialog.setNameFilter( "Image Files (*.png *.jpg *.tga *.bmp" )
		file = QFileDialog( self.parent() ).getSaveFileName(
			self,
			"Save Image",
			os.curdir,
			"PNG Files (*.png)"
		)
		image = QPixmap( self.scene().width(), self.scene().height() )
		image.fill()
		painter = QPainter( image )
		self.scene().render( painter )
		image.save( file )
