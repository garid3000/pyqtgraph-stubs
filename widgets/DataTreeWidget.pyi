from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['DataTreeWidget']

class DataTreeWidget(QtWidgets.QTreeWidget):
    """
    Widget for displaying hierarchical python data structures
    (eg, nested dicts, lists, and arrays)
    """
    def __init__(self, parent: Incomplete | None = None, data: Incomplete | None = None) -> None: ...
    widgets: Incomplete
    nodes: Incomplete
    def setData(self, data, hideRoot: bool = False) -> None:
        """data should be a dictionary."""
    def buildTree(self, data, parent, name: str = '', hideRoot: bool = False, path=()) -> None: ...
    def parse(self, data):
        """
        Given any python object, return:
          * type
          * a short string representation
          * a dict of sub-objects to be parsed
          * optional widget to display as sub-node
        """
