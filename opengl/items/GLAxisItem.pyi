from OpenGL.GL import *
from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLAxisItem']

class GLAxisItem(GLGraphicsItem):
    """
    **Bases:** :class:`GLGraphicsItem <pyqtgraph.opengl.GLGraphicsItem.GLGraphicsItem>`
    
    Displays three lines indicating origin and orientation of local coordinate system. 
    
    """
    antialias: Incomplete
    def __init__(self, size: Incomplete | None = None, antialias: bool = True, glOptions: str = 'translucent', parentItem: Incomplete | None = None) -> None: ...
    def setSize(self, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, size: Incomplete | None = None) -> None:
        """
        Set the size of the axes (in its local coordinate system; this does not affect the transform)
        Arguments can be x,y,z or size=QVector3D().
        """
    def size(self): ...
    def paint(self) -> None: ...
