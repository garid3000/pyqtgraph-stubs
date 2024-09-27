from OpenGL.GL import *
from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLBoxItem']

class GLBoxItem(GLGraphicsItem):
    """
    **Bases:** :class:`GLGraphicsItem <pyqtgraph.opengl.GLGraphicsItem>`
    
    Displays a wire-frame box.
    """
    def __init__(self, size: Incomplete | None = None, color: Incomplete | None = None, glOptions: str = 'translucent', parentItem: Incomplete | None = None) -> None: ...
    def setSize(self, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, size: Incomplete | None = None) -> None:
        """
        Set the size of the box (in its local coordinate system; this does not affect the transform)
        Arguments can be x,y,z or size=QVector3D().
        """
    def size(self): ...
    def setColor(self, *args) -> None:
        """Set the color of the box. Arguments are the same as those accepted by functions.mkColor()"""
    def color(self): ...
    def paint(self) -> None: ...
