from .GraphicsObject import GraphicsObject
from .GraphicsWidgetAnchor import GraphicsWidgetAnchor
from _typeshed import Incomplete

__all__ = ['ScaleBar']

class ScaleBar(GraphicsWidgetAnchor, GraphicsObject):
    """
    Displays a rectangular bar to indicate the relative scale of objects on the view.
    """
    brush: Incomplete
    pen: Incomplete
    size: Incomplete
    offset: Incomplete
    bar: Incomplete
    text: Incomplete
    def __init__(self, size, width: int = 5, brush: Incomplete | None = None, pen: Incomplete | None = None, suffix: str = 'm', offset: Incomplete | None = None) -> None: ...
    def changeParent(self) -> None: ...
    def updateBar(self) -> None: ...
    def boundingRect(self): ...
    def setParentItem(self, p): ...
