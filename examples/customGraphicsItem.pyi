import pyqtgraph as pg
from _typeshed import Incomplete
from pyqtgraph import QtCore as QtCore, QtGui as QtGui

class CandlestickItem(pg.GraphicsObject):
    data: Incomplete
    def __init__(self, data) -> None: ...
    picture: Incomplete
    def generatePicture(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...

data: Incomplete
item: Incomplete
plt: Incomplete
