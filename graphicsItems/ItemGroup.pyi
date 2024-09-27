from .GraphicsObject import GraphicsObject

__all__ = ['ItemGroup']

class ItemGroup(GraphicsObject):
    """
    Replacement for QGraphicsItemGroup
    """
    def __init__(self, *args) -> None: ...
    def boundingRect(self): ...
    def paint(self, *args) -> None: ...
    def addItem(self, item) -> None: ...