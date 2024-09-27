from .GraphicsWidget import GraphicsWidget
from _typeshed import Incomplete
from .ViewBox import ViewBox
from ..Qt import QtWidgets, QtGui



__all__ = ['GraphicsLayout']

class GraphicsLayout(GraphicsWidget):
    """
    Used for laying out GraphicsWidgets in a grid.
    This is usually created automatically as part of a :class:`GraphicsLayoutWidget <pyqtgraph.GraphicsLayoutWidget>`.
    """
    border: Incomplete
    layout: Incomplete
    items: Incomplete
    rows: Incomplete
    itemBorders: Incomplete
    currentRow: int
    currentCol: int
    def __init__(self, parent: Incomplete | None = None, border: Incomplete | None = None) -> None: ...
    def setBorder(self, *args, **kwds) -> None:
        """
        Set the pen used to draw border between cells.

        See :func:`mkPen <pyqtgraph.mkPen>` for arguments.
        """
    def nextRow(self) -> None:
        """Advance to next row for automatic item placement"""
    def nextColumn(self) -> None:
        """Advance to next available column
        (generally only for internal use--called by addItem)"""
    def nextCol(self, *args, **kargs):
        """Alias of nextColumn"""
    def addPlot(self, row: Incomplete | None = None, col: Incomplete | None = None, rowspan: int = 1, colspan: int = 1, **kargs):
        """
        Create a PlotItem and place it in the next available cell (or in the cell specified)
        All extra keyword arguments are passed to :func:`PlotItem.__init__ <pyqtgraph.PlotItem.__init__>`
        Returns the created item.
        """
    def addViewBox(self, row: int | None = None, col: int | None = None, rowspan: int = 1, colspan: int = 1, **kargs: QtWidgets.QGraphicsWidget | None | QtGui.QPen | float | bool | str ) -> ViewBox:
        """
        Create a ViewBox and place it in the next available cell (or in the cell specified)
        All extra keyword arguments are passed to :func:`ViewBox.__init__ <pyqtgraph.ViewBox.__init__>`
        Returns the created item.
        """
    def addLabel(self, text: str = ' ', row: Incomplete | None = None, col: Incomplete | None = None, rowspan: int = 1, colspan: int = 1, **kargs):
        """
        Create a LabelItem with *text* and place it in the next available cell (or in the cell specified)
        All extra keyword arguments are passed to :func:`LabelItem.__init__ <pyqtgraph.LabelItem.__init__>`
        Returns the created item.

        To create a vertical label, use *angle* = -90.
        """
    def addLayout(self, row: Incomplete | None = None, col: Incomplete | None = None, rowspan: int = 1, colspan: int = 1, **kargs):
        """
        Create an empty GraphicsLayout and place it in the next available cell (or in the cell specified)
        All extra keyword arguments are passed to :func:`GraphicsLayout.__init__ <pyqtgraph.GraphicsLayout.__init__>`
        Returns the created item.
        """
    def addItem(self, item, row: Incomplete | None = None, col: Incomplete | None = None, rowspan: int = 1, colspan: int = 1) -> None:
        """
        Add an item to the layout and place it in the next available cell (or in the cell specified).
        The item must be an instance of a QGraphicsWidget subclass.
        """
    def getItem(self, row, col):
        """Return the item in (*row*, *col*). If the cell is empty, return None."""
    def boundingRect(self): ...
    def itemIndex(self, item):
        """Return the numerical index of GraphicsItem object passed in

        Parameters
        ----------
        item : QGraphicsLayoutItem
            Item to query the index position of

        Returns
        -------
        int
            Index of the item within the graphics layout

        Raises
        ------
        ValueError
            Raised if item could not be found inside the GraphicsLayout instance.
        """
    def removeItem(self, item) -> None:
        """Remove *item* from the layout."""
    def clear(self) -> None:
        """Remove all items from the layout and set the current row and column to 0
        """
    def setContentsMargins(self, *args) -> None: ...
    def setSpacing(self, *args) -> None: ...
