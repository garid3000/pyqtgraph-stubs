from ..Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from _typeshed import Incomplete

translate: Incomplete

class ParameterItem(QtWidgets.QTreeWidgetItem):
    """
    Abstract ParameterTree item. 
    Used to represent the state of a Parameter from within a ParameterTree.
    
      - Sets first column of item to name
      - generates context menu if item is renamable or removable
      - handles child added / removed events
      - provides virtual functions for handling changes from parameter
    
    For more ParameterItem types, see ParameterTree.parameterTypes module.
    """
    param: Incomplete
    depth: Incomplete
    ignoreNameColumnChange: bool
    def __init__(self, param, depth: int = 0) -> None: ...
    def updateFlags(self) -> None: ...
    def valueChanged(self, param, val) -> None: ...
    def isFocusable(self):
        """Return True if this item should be included in the tab-focus order"""
    def setFocus(self) -> None:
        """Give input focus to this item.
        Can be reimplemented to display editor widgets, etc.
        """
    def focusNext(self, forward: bool = True) -> None:
        """Give focus to the next (or previous) focusable item in the parameter tree"""
    def treeWidgetChanged(self) -> None:
        """Called when this item is added or removed from a tree.
        Expansion, visibility, and column widgets must all be configured AFTER 
        the item is added to a tree, not during __init__.
        """
    def childAdded(self, param, child, pos) -> None: ...
    def childRemoved(self, param, child) -> None: ...
    def parentChanged(self, param, parent) -> None: ...
    contextMenu: Incomplete
    def contextMenuEvent(self, ev) -> None: ...
    def columnChangedEvent(self, col) -> None:
        """Called when the text in a column has been edited (or otherwise changed).
        By default, we only use changes to column 0 to rename the parameter.
        """
    def expandedChangedEvent(self, expanded) -> None: ...
    def nameChanged(self, param, name) -> None: ...
    def titleChanged(self) -> None: ...
    def limitsChanged(self, param, limits) -> None:
        """Called when the parameter's limits have changed"""
    def defaultChanged(self, param, default) -> None:
        """Called when the parameter's default value has changed"""
    def optsChanged(self, param, opts) -> None:
        """Called when any options are changed that are not
        name, value, default, or limits"""
    def contextMenuTriggered(self, name): ...
    def editName(self) -> None: ...
    def selected(self, sel) -> None:
        """Called when this item has been selected (sel=True) OR deselected (sel=False)"""
    def requestRemove(self) -> None: ...
    def __hash__(self): ...
    def __eq__(self, x): ...
