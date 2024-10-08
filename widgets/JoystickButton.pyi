from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['JoystickButton']

class JoystickButton(QtWidgets.QPushButton):
    sigStateChanged: Incomplete
    radius: int
    state: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    pressPos: Incomplete
    def mousePressEvent(self, ev) -> None: ...
    def mouseMoveEvent(self, ev) -> None: ...
    def mouseReleaseEvent(self, ev) -> None: ...
    def wheelEvent(self, ev) -> None: ...
    def doubleClickEvent(self, ev) -> None: ...
    def getState(self): ...
    spotPos: Incomplete
    def setState(self, *xy) -> None: ...
    def paintEvent(self, ev) -> None: ...
    def resizeEvent(self, ev) -> None: ...
