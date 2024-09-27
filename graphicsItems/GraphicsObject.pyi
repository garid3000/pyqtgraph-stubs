from ..Qt import QtWidgets
from .GraphicsItem import GraphicsItem

__all__ = ['GraphicsObject']

class GraphicsObject(GraphicsItem, QtWidgets.QGraphicsObject):
    """
    **Bases:** :class:`GraphicsItem <pyqtgraph.GraphicsItem>`, :class:`QtWidgets.QGraphicsObject`

    Extension of QGraphicsObject with some useful methods (provided by :class:`GraphicsItem <pyqtgraph.GraphicsItem>`)
    """
    def __init__(self, *args) -> None: ...
    def itemChange(self, change, value): ...
