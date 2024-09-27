from ..Qt import QtWidgets
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['TableWidget']

class TableWidget(QtWidgets.QTableWidget):
    """Extends QTableWidget with some useful functions for automatic data handling
    and copy / export context menu. Can automatically format and display a variety
    of data types (see :func:`setData() <pyqtgraph.TableWidget.setData>` for more
    information.
    """
    itemClass: Incomplete
    sortModes: Incomplete
    contextMenu: Incomplete
    def __init__(self, *args, **kwds) -> None:
        """
        All positional arguments are passed to QTableWidget.__init__().
        
        ===================== =================================================
        **Keyword Arguments**
        editable              (bool) If True, cells in the table can be edited
                              by the user. Default is False.
        sortable              (bool) If True, the table may be soted by
                              clicking on column headers. Note that this also
                              causes rows to appear initially shuffled until
                              a sort column is selected. Default is True.
                              *(added in version 0.9.9)*
        ===================== =================================================
        """
    verticalHeadersSet: bool
    horizontalHeadersSet: bool
    items: Incomplete
    def clear(self) -> None:
        """Clear all contents from the table."""
    def setData(self, data) -> None:
        """Set the data displayed in the table.
        Allowed formats are:
        
          * numpy arrays
          * numpy record arrays
          * metaarrays
          * list-of-lists  [[1,2,3], [4,5,6]]
          * dict-of-lists  {'x': [1,2,3], 'y': [4,5,6]}
          * list-of-dicts  [{'x': 1, 'y': 4}, {'x': 2, 'y': 5}, ...]
        """
    def appendData(self, data) -> None:
        """
        Add new rows to the table.
        
        See :func:`setData() <pyqtgraph.TableWidget.setData>` for accepted
        data types.
        """
    editable: Incomplete
    def setEditable(self, editable: bool = True) -> None: ...
    def setFormat(self, format, column: Incomplete | None = None) -> None:
        """
        Specify the default text formatting for the entire table, or for a
        single column if *column* is specified.
        
        If a string is specified, it is used as a format string for converting
        float values (and all other types are converted using str). If a 
        function is specified, it will be called with the item as its only
        argument and must return a string. Setting format = None causes the 
        default formatter to be used instead.
        
        Added in version 0.9.9.
        
        """
    def iteratorFn(self, data): ...
    def iterFirstAxis(self, data) -> Generator[Incomplete, None, None]: ...
    def iterate(self, data) -> Generator[Incomplete, None, None]: ...
    def iterateScalar(self, data) -> Generator[Incomplete, None, None]: ...
    def appendRow(self, data) -> None: ...
    def addRow(self, vals) -> None: ...
    def setRow(self, row, vals) -> None: ...
    def setSortMode(self, column, mode) -> None:
        """
        Set the mode used to sort *column*.
        
        ============== ========================================================
        **Sort Modes**
        value          Compares item.value if available; falls back to text
                       comparison.
        text           Compares item.text()
        index          Compares by the order in which items were inserted.
        ============== ========================================================
        
        Added in version 0.9.9
        """
    def sizeHint(self): ...
    def serialize(self, useSelection: bool = False):
        """Convert entire table (or just selected area) into tab-separated text values"""
    def copySel(self) -> None:
        """Copy selected data to clipboard."""
    def copyAll(self) -> None:
        """Copy all data to clipboard."""
    def saveSel(self) -> None:
        """Save selected data to file."""
    def saveAll(self) -> None:
        """Save all data to file."""
    def save(self, data) -> None: ...
    def contextMenuEvent(self, ev) -> None: ...
    def keyPressEvent(self, ev) -> None: ...
    def handleItemChanged(self, item) -> None: ...

class TableWidgetItem(QtWidgets.QTableWidgetItem):
    sortMode: str
    index: Incomplete
    def __init__(self, val, index, format: Incomplete | None = None) -> None: ...
    def setEditable(self, editable) -> None:
        """
        Set whether this item is user-editable.
        """
    def setSortMode(self, mode) -> None:
        """
        Set the mode used to sort this item against others in its column.
        
        ============== ========================================================
        **Sort Modes**
        value          Compares item.value if available; falls back to text
                       comparison.
        text           Compares item.text()
        index          Compares by the order in which items were inserted.
        ============== ========================================================
        """
    def setFormat(self, fmt) -> None:
        """Define the conversion from item value to displayed text. 
        
        If a string is specified, it is used as a format string for converting
        float values (and all other types are converted using str). If a 
        function is specified, it will be called with the item as its only
        argument and must return a string.
        
        Added in version 0.9.9.
        """
    value: Incomplete
    def setValue(self, value) -> None: ...
    def itemChanged(self) -> None:
        """Called when the data of this item has changed."""
    def textChanged(self) -> None:
        """Called when this item's text has changed for any reason."""
    def format(self): ...
    def __lt__(self, other): ...
