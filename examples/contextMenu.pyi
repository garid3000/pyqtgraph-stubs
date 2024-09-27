import pyqtgraph as pg
from _typeshed import Incomplete
from pyqtgraph.Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets

win: Incomplete
view: Incomplete
zoom1: Incomplete
zoom2: Incomplete

def zoomTo1() -> None: ...
def zoomTo2() -> None: ...

class MenuBox(pg.GraphicsObject):
    """
    This class draws a rectangular area. Right-clicking inside the area will
    raise a custom context menu which also includes the context menus of
    its parents.    
    """
    name: Incomplete
    pen: Incomplete
    menu: Incomplete
    def __init__(self, name) -> None: ...
    def boundingRect(self): ...
    def paint(self, p, *args) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def raiseContextMenu(self, ev): ...
    def getContextMenus(self, event: Incomplete | None = None): ...
    def setGreen(self) -> None: ...
    def setBlue(self) -> None: ...
    def setAlpha(self, a) -> None: ...

box1: Incomplete
box2: Incomplete