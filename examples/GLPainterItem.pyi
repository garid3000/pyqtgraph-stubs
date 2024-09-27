from _typeshed import Incomplete
from pyqtgraph.Qt import QtCore as QtCore, QtGui as QtGui
from pyqtgraph.opengl import GLAxisItem as GLAxisItem, GLGraphicsItem as GLGraphicsItem, GLGridItem as GLGridItem, GLViewWidget as GLViewWidget

SIZE: int

class GLPainterItem(GLGraphicsItem.GLGraphicsItem):
    def __init__(self, **kwds) -> None: ...
    def compute_projection(self): ...
    def paint(self) -> None: ...
    def draw(self, painter) -> None: ...

glv: Incomplete
griditem: Incomplete
axisitem: Incomplete
paintitem: Incomplete
