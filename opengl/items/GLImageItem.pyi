from OpenGL.GL import *
from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLImageItem']

class GLImageItem(GLGraphicsItem):
    """
    **Bases:** :class:`GLGraphicsItem <pyqtgraph.opengl.GLGraphicsItem.GLGraphicsItem>`
    
    Displays image data as a textured quad.
    """
    smooth: Incomplete
    texture: Incomplete
    def __init__(self, data, smooth: bool = False, glOptions: str = 'translucent', parentItem: Incomplete | None = None) -> None:
        """
        
        ==============  =======================================================================================
        **Arguments:**
        data            Volume data to be rendered. *Must* be 3D numpy array (x, y, RGBA) with dtype=ubyte.
                        (See functions.makeRGBA)
        smooth          (bool) If True, the volume slices are rendered with linear interpolation 
        ==============  =======================================================================================
        """
    def initializeGL(self) -> None: ...
    data: Incomplete
    def setData(self, data) -> None: ...
    def paint(self) -> None: ...
