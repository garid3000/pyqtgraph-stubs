from OpenGL.GL import *
from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLLinePlotItem']

class GLLinePlotItem(GLGraphicsItem):
    """Draws line plots in 3D."""
    pos: Incomplete
    mode: str
    width: float
    color: Incomplete
    def __init__(self, parentItem: Incomplete | None = None, **kwds) -> None:
        """All keyword arguments are passed to setData()"""
    antialias: bool
    def setData(self, **kwds) -> None:
        """
        Update the data displayed by this item. All arguments are optional; 
        for example it is allowed to update vertex positions while leaving 
        colors unchanged, etc.
        
        ====================  ==================================================
        **Arguments:**
        ------------------------------------------------------------------------
        pos                   (N,3) array of floats specifying point locations.
        color                 (N,4) array of floats (0.0-1.0) or
                              tuple of floats specifying
                              a single color for the entire item.
        width                 float specifying line width
        antialias             enables smooth line drawing
        mode                  'lines': Each pair of vertexes draws a single line
                                       segment.
                              'line_strip': All vertexes are drawn as a
                                            continuous set of line segments.
        ====================  ==================================================
        """
    def paint(self) -> None: ...
