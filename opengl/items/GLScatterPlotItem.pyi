import numpy as np
from OpenGL.GL import *
from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLScatterPlotItem']

class GLScatterPlotItem(GLGraphicsItem):
    """Draws points at a list of 3D positions."""
    pos: Incomplete
    size: int
    color: Incomplete
    pxMode: bool
    shader: Incomplete
    def __init__(self, parentItem: Incomplete | None = None, **kwds) -> None: ...
    def setData(self, **kwds: np.ndarray[tuple[int,int], np.dtype[np.uint8| np.float64]] | list[float| int] | bool | float) -> None:
        """
        Update the data displayed by this item. All arguments are optional; 
        for example it is allowed to update spot positions while leaving 
        colors unchanged, etc.
        
        ====================  ==================================================
        **Arguments:**
        pos                   (N,3) array of floats specifying point locations.
        color                 (N,4) array of floats (0.0-1.0) specifying
                              spot colors OR 4a tuple of floats specifying
                              a single color for all spots.
        size                  (N,) array of floats specifying spot sizes or 
                              a single value to apply to all spots.
        pxMode                If True, spot sizes are expressed in pixels. 
                              Otherwise, they are expressed in item coordinates.
        ====================  ==================================================
        """
    pointTexture: Incomplete
    def initializeGL(self): ...
    def paint(self) -> None: ...
