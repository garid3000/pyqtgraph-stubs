from ..Qt import QtWidgets as QtWidgets
from .Container import Container as Container, HContainer as HContainer, TContainer as TContainer, VContainer as VContainer
from .Dock import Dock as Dock
from .DockDrop import DockDrop as DockDrop
from _typeshed import Incomplete

class DockArea(Container, QtWidgets.QWidget):
    dockdrop: Incomplete
    layout: Incomplete
    docks: Incomplete
    topContainer: Incomplete
    temporary: Incomplete
    tempAreas: Incomplete
    home: Incomplete
    def __init__(self, parent: Incomplete | None = None, temporary: bool = False, home: Incomplete | None = None) -> None: ...
    def type(self): ...
    def addDock(self, dock: Incomplete | None = None, position: str = 'bottom', relativeTo: Incomplete | None = None, **kwds):
        """Adds a dock to this area.
        
        ============== =================================================================
        **Arguments:**
        dock           The new Dock object to add. If None, then a new Dock will be 
                       created.
        position       'bottom', 'top', 'left', 'right', 'above', or 'below'
        relativeTo     If relativeTo is None, then the new Dock is added to fill an 
                       entire edge of the window. If relativeTo is another Dock, then 
                       the new Dock is placed adjacent to it (or in a tabbed 
                       configuration for 'above' and 'below'). 
        ============== =================================================================
        
        All extra keyword arguments are passed to Dock.__init__() if *dock* is
        None.        
        """
    def moveDock(self, dock, position, neighbor) -> None:
        """
        Move an existing Dock to a new location. 
        """
    def getContainer(self, obj): ...
    def makeContainer(self, typ): ...
    def addContainer(self, typ, obj):
        """Add a new container around obj"""
    def insert(self, new, pos: Incomplete | None = None, neighbor: Incomplete | None = None) -> None: ...
    def count(self): ...
    def resizeEvent(self, ev) -> None: ...
    def addTempArea(self): ...
    def floatDock(self, dock) -> None:
        """Removes *dock* from this DockArea and places it in a new window."""
    def removeTempArea(self, area) -> None: ...
    def saveState(self):
        """
        Return a serialized (storable) representation of the state of
        all Docks in this DockArea."""
    def childState(self, obj): ...
    def restoreState(self, state, missing: str = 'error', extra: str = 'bottom') -> None:
        """
        Restore Dock configuration as generated by saveState.
        
        This function does not create any Docks--it will only 
        restore the arrangement of an existing set of Docks.
        
        By default, docks that are described in *state* but do not exist
        in the dock area will cause an exception to be raised. This behavior
        can be changed by setting *missing* to 'ignore' or 'create'.
        
        Extra docks that are in the dockarea but that are not mentioned in
        *state* will be added to the bottom of the dockarea, unless otherwise
        specified by the *extra* argument.
        """
    def buildFromState(self, state, docks, root, depth: int = 0, missing: str = 'error') -> None: ...
    def findAll(self, obj: Incomplete | None = None, c: Incomplete | None = None, d: Incomplete | None = None): ...
    def apoptose(self, propagate: bool = True) -> None: ...
    def clear(self) -> None: ...
    def dragEnterEvent(self, *args) -> None: ...
    def dragMoveEvent(self, *args) -> None: ...
    def dragLeaveEvent(self, *args) -> None: ...
    def dropEvent(self, *args) -> None: ...
    def printState(self, state: Incomplete | None = None, name: str = 'Main') -> None: ...

class TempAreaWindow(QtWidgets.QWidget):
    layout: Incomplete
    dockarea: Incomplete
    def __init__(self, area, **kwargs) -> None: ...
    def closeEvent(self, *args) -> None: ...
