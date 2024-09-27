from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['ColorButton']

class ColorButton(QtWidgets.QPushButton):
    """
    **Bases:** QtWidgets.QPushButton
    
    Button displaying a color and allowing the user to select a new color.
    
    ====================== ============================================================
    **Signals:**
    sigColorChanging(self) emitted whenever a new color is picked in the color dialog
    sigColorChanged(self)  emitted when the selected color is accepted (user clicks OK)
    ====================== ============================================================
    """
    sigColorChanging: Incomplete
    sigColorChanged: Incomplete
    padding: Incomplete
    colorDialog: Incomplete
    def __init__(self, parent: Incomplete | None = None, color=(128, 128, 128), padding: int = 6) -> None: ...
    def paintEvent(self, ev) -> None: ...
    def setColor(self, color, finished: bool = True) -> None:
        """Sets the button's color and emits both sigColorChanged and sigColorChanging."""
    origColor: Incomplete
    def selectColor(self) -> None: ...
    def dialogColorChanged(self, color) -> None: ...
    def colorRejected(self) -> None: ...
    def colorSelected(self, color) -> None: ...
    def saveState(self): ...
    def restoreState(self, state) -> None: ...
    def color(self, mode: str = 'qcolor'): ...
    def widgetGroupInterface(self): ...
