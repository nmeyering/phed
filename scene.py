from PyQt4.QtGui import QGraphicsScene
class Scene( QGraphicsScene ):
	def __init__( self ):
		QGraphicsScene.__init__( self )

		self.addText( "Hello, World!" )
