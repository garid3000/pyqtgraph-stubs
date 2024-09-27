from ..Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets, mkQApp as mkQApp
from ..widgets.TreeWidget import TreeWidget as TreeWidget
from .ParameterItem import ParameterItem as ParameterItem
from .parameterTypes import GroupParameterItem as GroupParameterItem
from _typeshed import Incomplete

class ParameterTree(TreeWidget):
    """Widget used to display or control data from a hierarchy of Parameters"""
    paramSet: Incomplete
    lastSel: Incomplete
    def __init__(self, parent: Incomplete | None = None, showHeader: bool = True) -> None:
        """
        ============== ========================================================
        **Arguments:**
        parent         (QWidget) An optional parent widget
        showHeader     (bool) If True, then the QTreeView header is displayed.
        ============== ========================================================
        """
    def setParameters(self, param, showTop: bool = True) -> None:
        """
        Set the top-level :class:`Parameter <pyqtgraph.parametertree.Parameter>`
        to be displayed in this ParameterTree.

        If *showTop* is False, then the top-level parameter is hidden and only 
        its children will be visible. This is a convenience method equivalent 
        to::
        
            tree.clear()
            tree.addParameters(param, showTop)
        """
    def addParameters(self, param, root: Incomplete | None = None, depth: int = 0, showTop: bool = True) -> None:
        """
        Adds one top-level :class:`Parameter <pyqtgraph.parametertree.Parameter>`
        to the view. 
        
        ============== ==========================================================
        **Arguments:** 
        param          The :class:`Parameter <pyqtgraph.parametertree.Parameter>` 
                       to add.
        root           The item within the tree to which *param* should be added.
                       By default, *param* is added as a top-level item.
        showTop        If False, then *param* will be hidden, and only its 
                       children will be visible in the tree.
        ============== ==========================================================
        """
    def clear(self) -> None:
        """
        Remove all parameters from the tree.        
        """
    def focusNext(self, item, forward: bool = True) -> None:
        """Give input focus to the next (or previous) item after *item*
        """
    def focusPrevious(self, item) -> None: ...
    def nextFocusableChild(self, root, startItem: Incomplete | None = None, forward: bool = True): ...
    def contextMenuEvent(self, ev) -> None: ...
    def event(self, event: QtCore.QEvent) -> bool: ...
    def itemChangedEvent(self, item, col) -> None: ...
    def itemExpandedEvent(self, item) -> None: ...
    def itemCollapsedEvent(self, item) -> None: ...
    def selectionChanged(self, *args): ...
    def sizeHint(self): ...
