from PyQt4.QtGui import QGraphicsScene

class Scene( QGraphicsScene ):
	def __init__( self ):
		QGraphicsScene.__init__( self )

		self.setSceneRect( 0, 0, 1024, 768 )

