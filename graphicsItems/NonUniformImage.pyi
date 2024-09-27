from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['NonUniformImage']

class NonUniformImage(GraphicsObject):
    """
    **Bases:** :class:`GraphicsObject <pyqtgraph.GraphicsObject>`

    GraphicsObject displaying an image with non-uniform sample points. It's
    commonly used to display 2-d or slices of higher dimensional data that
    have a regular but non-uniform grid e.g. measurements or simulation results.
    """
    cmap: Incomplete
    lut: Incomplete
    data: Incomplete
    levels: Incomplete
    border: Incomplete
    picture: Incomplete
    def __init__(self, x, y, z, border: Incomplete | None = None) -> None: ...
    def setLookupTable(self, lut, update: bool = True, **kwargs) -> None: ...
    def setColorMap(self, cmap) -> None: ...
    def getHistogram(self, **kwds):
        """Returns x and y arrays containing the histogram values for the current image.
        For an explanation of the return format, see numpy.histogram().
        """
    def setLevels(self, levels) -> None: ...
    def getLevels(self): ...
    def generatePicture(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...
