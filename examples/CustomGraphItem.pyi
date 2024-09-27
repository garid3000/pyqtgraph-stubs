import pyqtgraph as pg
from _typeshed import Incomplete
from pyqtgraph.Qt import QtCore as QtCore

w: Incomplete
v: Incomplete

class Graph(pg.GraphItem):
    dragPoint: Incomplete
    dragOffset: Incomplete
    textItems: Incomplete
    def __init__(self) -> None: ...
    text: Incomplete
    data: Incomplete
    def setData(self, **kwds) -> None: ...
    def setTexts(self, text) -> None: ...
    def updateGraph(self) -> None: ...
    def mouseDragEvent(self, ev) -> None: ...
    def clicked(self, pts) -> None: ...

g: Incomplete
pos: Incomplete
adj: Incomplete
symbols: Incomplete
lines: Incomplete
texts: Incomplete
