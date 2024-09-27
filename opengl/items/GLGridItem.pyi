from OpenGL.GL import *
from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLGridItem']

class GLGridItem(GLGraphicsItem):
    """
    **Bases:** :class:`GLGraphicsItem <pyqtgraph.opengl.GLGraphicsItem.GLGraphicsItem>`
    
    Displays a wire-frame grid. 
    """
    antialias: Incomplete
    def __init__(self, size: Incomplete | None = None, color=(255, 255, 255, 76.5), antialias: bool = True, glOptions: str = 'translucent', parentItem: Incomplete | None = None) -> None: ...
    def setSize(self, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, size: Incomplete | None = None) -> None:
        """
        Set the size of the axes (in its local coordinate system; this does not affect the transform)
        Arguments can be x,y,z or size=QVector3D().
        """
    def size(self): ...
    def setSpacing(self, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, spacing: Incomplete | None = None) -> None:
        """
        Set the spacing between grid lines.
        Arguments can be x,y,z or spacing=QVector3D().
        """
    def spacing(self): ...
    def setColor(self, color) -> None:
        """Set the color of the grid. Arguments are the same as those accepted by functions.mkColor()"""
    def color(self): ...
    def paint(self) -> None: ...
