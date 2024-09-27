import pyqtgraph as pg
from _typeshed import Incomplete
from pyqtgraph.Qt import QtCore as QtCore

class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def mouseDragEvent(self, ev, axis: Incomplete | None = None) -> None: ...

class CustomTickSliderItem(pg.TickSliderItem):
    all_ticks: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def setTicks(self, ticks) -> None: ...
    def updateRange(self, vb, viewRange) -> None: ...

app: Incomplete
axis: Incomplete
vb: Incomplete
pw: Incomplete
dates: Incomplete
tickViewer: Incomplete
r: Incomplete
