from .UIGraphicsItem import UIGraphicsItem
from _typeshed import Incomplete

__all__ = ['VTickGroup']

class VTickGroup(UIGraphicsItem):
    """
    **Bases:** :class:`UIGraphicsItem <pyqtgraph.UIGraphicsItem>`
    
    Draws a set of tick marks which always occupy the same vertical range of the view,
    but have x coordinates relative to the data within the view.
    
    """
    path: Incomplete
    ticks: Incomplete
    xvals: Incomplete
    yrange: Incomplete
    def __init__(self, xvals: Incomplete | None = None, yrange: Incomplete | None = None, pen: Incomplete | None = None) -> None:
        """
        ==============  ===================================================================
        **Arguments:**
        xvals           A list of x values (in data coordinates) at which to draw ticks.
        yrange          A list of [low, high] limits for the tick. 0 is the bottom of
                        the view, 1 is the top. [0.8, 1] would draw ticks in the top
                        fifth of the view.
        pen             The pen to use for drawing ticks. Default is grey. Can be specified
                        as any argument valid for :func:`mkPen<pyqtgraph.mkPen>`
        ==============  ===================================================================
        """
    pen: Incomplete
    def setPen(self, *args, **kwargs) -> None:
        """Set the pen to use for drawing ticks. Can be specified as any arguments valid
        for :func:`mkPen<pyqtgraph.mkPen>`"""
    def setXVals(self, vals) -> None:
        """Set the x values for the ticks. 
        
        ==============   =====================================================================
        **Arguments:**
        vals             A list of x values (in data/plot coordinates) at which to draw ticks.
        ==============   =====================================================================
        """
    def setYRange(self, vals) -> None:
        """Set the y range [low, high] that the ticks are drawn on. 0 is the bottom of 
        the view, 1 is the top."""
    def dataBounds(self, *args, **kargs) -> None: ...
    def yRange(self): ...
    def rebuildTicks(self) -> None: ...
    def paint(self, p, *args) -> None: ...
