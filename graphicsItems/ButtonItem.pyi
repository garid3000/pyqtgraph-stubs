from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['ButtonItem']

class ButtonItem(GraphicsObject):
    """Button graphicsItem displaying an image."""
    clicked: Incomplete
    enabled: bool
    def __init__(self, imageFile: Incomplete | None = None, width: Incomplete | None = None, parentItem: Incomplete | None = None, pixmap: Incomplete | None = None) -> None: ...
    def setImageFile(self, imageFile) -> None: ...
    pixmap: Incomplete
    def setPixmap(self, pixmap) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def disable(self) -> None: ...
    def enable(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...
