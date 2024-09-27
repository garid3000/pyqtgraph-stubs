from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete
import numpy as np
from numpy.typing import NDArray

__all__ = ['GraphItem']

class GraphItem(GraphicsObject):
    """A GraphItem displays graph information as
    a set of nodes connected by lines (as in 'graph theory', not 'graphics').
    Useful for drawing networks, trees, etc.
    """
    scatter: Incomplete
    adjacency: Incomplete
    pos: Incomplete
    picture: Incomplete
    pen: str
    def __init__(self, **kwds) -> None: ...
    def setData(self, **kwds: str|NDArray[np.float64]|NDArray[np.int64]|int|bool) -> None:
        """
        Change the data displayed by the graph.

        ==============  =======================================================================
        **Arguments:**
        pos             (N,2) array of the positions of each node in the graph.
        adj             (M,2) array of connection data. Each row contains indexes
                        of two nodes that are connected or None to hide lines
        pen             The pen to use when drawing lines between connected
                        nodes. May be one of:

                          * QPen
                          * a single argument to pass to pg.mkPen
                          * a record array of length M
                            with fields (red, green, blue, alpha, width). Note
                            that using this option may have a significant performance
                            cost.
                          * None (to disable connection drawing)
                          * 'default' to use the default foreground color.

        symbolPen       The pen(s) used for drawing nodes.
        symbolBrush     The brush(es) used for drawing nodes.
        ``**opts``      All other keyword arguments are given to
                        :func:`ScatterPlotItem.setData() <pyqtgraph.ScatterPlotItem.setData>`
                        to affect the appearance of nodes (symbol, size, brush,
                        etc.)
        ==============  =======================================================================
        """
    def setPen(self, *args, **kwargs) -> None:
        """
        Set the pen used to draw graph lines.
        May be:

          * None to disable line drawing
          * Record array with fields (red, green, blue, alpha, width)
          * Any set of arguments and keyword arguments accepted by
            :func:`mkPen <pyqtgraph.mkPen>`.
          * 'default' to use the default foreground color.
        """
    def generatePicture(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...
    def dataBounds(self, *args, **kwds): ...
    def pixelPadding(self): ...
