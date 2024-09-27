from .UIGraphicsItem import UIGraphicsItem
from _typeshed import Incomplete

__all__ = ['GridItem']

class GridItem(UIGraphicsItem):
    """
    **Bases:** :class:`UIGraphicsItem <pyqtgraph.UIGraphicsItem>`
    
    Displays a rectangular grid of lines indicating major divisions within a coordinate system.
    Automatically determines what divisions to use.
    """
    opts: Incomplete
    def __init__(self, pen: str = 'default', textPen: str = 'default') -> None: ...
    picture: Incomplete
    def setPen(self, *args, **kwargs) -> None:
        """Set the pen used to draw the grid."""
    def setTextPen(self, *args, **kwargs) -> None:
        """Set the pen used to draw the texts."""
    grid_depth: Incomplete
    def setTickSpacing(self, x: Incomplete | None = None, y: Incomplete | None = None) -> None:
        """
        Set the grid tick spacing to use.

        Tick spacing for each axis shall be specified as an array of
        descending values, one for each tick scale. When the value
        is set to None, grid line distance is chosen automatically
        for this particular level.

        Example:
            Default setting of 3 scales for each axis:
            setTickSpacing(x=[None, None, None], y=[None, None, None])

            Single scale with distance of 1.0 for X axis, Two automatic
            scales for Y axis:
            setTickSpacing(x=[1.0], y=[None, None])

            Single scale with distance of 1.0 for X axis, Two scales
            for Y axis, one with spacing of 1.0, other one automatic:
            setTickSpacing(x=[1.0], y=[1.0, None])
        """
    def viewRangeChanged(self) -> None: ...
    def paint(self, p, opt, widget) -> None: ...
    def generatePicture(self) -> None: ...
