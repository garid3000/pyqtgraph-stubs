from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['PathButton']

class PathButton(QtWidgets.QPushButton):
    """Simple PushButton extension that paints a QPainterPath centered on its face.
    """
    margin: Incomplete
    path: Incomplete
    def __init__(self, parent: Incomplete | None = None, path: Incomplete | None = None, pen: str = 'default', brush: Incomplete | None = None, size=(30, 30), margin: int = 7) -> None: ...
    brush: Incomplete
    def setBrush(self, brush) -> None: ...
    pen: Incomplete
    def setPen(self, *args, **kwargs) -> None: ...
    def setPath(self, path) -> None: ...
    def paintEvent(self, ev) -> None: ...
