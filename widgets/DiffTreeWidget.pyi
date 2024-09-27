from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['DiffTreeWidget']

class DiffTreeWidget(QtWidgets.QWidget):
    """
    Widget for displaying differences between hierarchical python data structures
    (eg, nested dicts, lists, and arrays)
    """
    layout: Incomplete
    trees: Incomplete
    def __init__(self, parent: Incomplete | None = None, a: Incomplete | None = None, b: Incomplete | None = None) -> None: ...
    data: Incomplete
    def setData(self, a, b):
        """
        Set the data to be compared in this widget.
        """
    def compare(self, a, b, path=()) -> None:
        """
        Compare data structure *a* to structure *b*. 
        
        Return True if the objects match completely. 
        Otherwise, return a structure that describes the differences:
        
            { 'type': bool
              'len': bool,
              'str': bool,
              'shape': bool,
              'dtype': bool,
              'mask': array,
              }
        
                
        """
    def compareArrays(self, a, b): ...
    def setColor(self, path, column, color, tree: Incomplete | None = None) -> None: ...
