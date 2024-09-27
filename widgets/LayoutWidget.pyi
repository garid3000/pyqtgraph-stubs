from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['LayoutWidget']

class LayoutWidget(QtWidgets.QWidget):
    """
    Convenience class used for laying out QWidgets in a grid.
    (It's just a little less effort to use than QGridLayout)
    """
    layout: Incomplete
    items: Incomplete
    rows: Incomplete
    currentRow: int
    currentCol: int
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def nextRow(self) -> None:
        """Advance to next row for automatic widget placement"""
    def nextColumn(self, colspan: int = 1):
        """Advance to next column, while returning the current column number 
        (generally only for internal use--called by addWidget)"""
    def nextCol(self, *args, **kargs):
        """Alias of nextColumn"""
    def addLabel(self, text: str = ' ', row: Incomplete | None = None, col: Incomplete | None = None, rowspan: int = 1, colspan: int = 1, **kargs):
        """
        Create a QLabel with *text* and place it in the next available cell (or in the cell specified)
        All extra keyword arguments are passed to QLabel().
        Returns the created widget.
        """
    def addLayout(self, row: Incomplete | None = None, col: Incomplete | None = None, rowspan: int = 1, colspan: int = 1, **kargs):
        """
        Create an empty LayoutWidget and place it in the next available cell (or in the cell specified)
        All extra keyword arguments are passed to :func:`LayoutWidget.__init__ <pyqtgraph.LayoutWidget.__init__>`
        Returns the created widget.
        """
    def addWidget(self, item, row: Incomplete | None = None, col: Incomplete | None = None, rowspan: int = 1, colspan: int = 1) -> None:
        """
        Add a widget to the layout and place it in the next available cell (or in the cell specified).
        """
    def getWidget(self, row, col):
        """Return the widget in (*row*, *col*)"""
