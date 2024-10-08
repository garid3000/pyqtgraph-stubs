from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['ColorMapButton']

class ColorMapDisplayMixin:
    horizontal: Incomplete
    def __init__(self, *, orientation) -> None: ...
    def setMaximumThickness(self, val) -> None: ...
    def setColorMap(self, cmap) -> None: ...
    def colorMap(self): ...
    def getImage(self): ...
    def getMenu(self): ...
    def paintColorMap(self, painter, rect) -> None: ...

class ColorMapButton(ColorMapDisplayMixin, QtWidgets.QWidget):
    sigColorMapChanged: Incomplete
    def __init__(self) -> None: ...
    def colorMapChanged(self) -> None: ...
    def paintEvent(self, evt) -> None: ...
    def mouseReleaseEvent(self, evt) -> None: ...
