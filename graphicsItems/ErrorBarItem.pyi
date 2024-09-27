from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['ErrorBarItem']

class ErrorBarItem(GraphicsObject):
    opts: Incomplete
    def __init__(self, **opts) -> None:
        """
        All keyword arguments are passed to setData().
        """
    path: Incomplete
    def setData(self, **opts) -> None:
        """
        Update the data in the item. All arguments are optional.
        
        Valid keyword options are:
        x, y, height, width, top, bottom, left, right, beam, pen
        
          * x and y must be numpy arrays specifying the coordinates of data points.
          * height, width, top, bottom, left, right, and beam may be numpy arrays,
            single values, or None to disable. All values should be positive.
          * top, bottom, left, and right specify the lengths of bars extending
            in each direction.
          * If height is specified, it overrides top and bottom.
          * If width is specified, it overrides left and right.
          * beam specifies the width of the beam at the end of each bar.
          * pen may be any single argument accepted by pg.mkPen().
        
        This method was added in version 0.9.9. For prior versions, use setOpts.
        """
    def setOpts(self, **opts) -> None: ...
    def drawPath(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...
