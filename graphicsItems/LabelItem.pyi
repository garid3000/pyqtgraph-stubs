from .GraphicsWidget import GraphicsWidget
from .GraphicsWidgetAnchor import GraphicsWidgetAnchor
from _typeshed import Incomplete

__all__ = ['LabelItem']

class LabelItem(GraphicsWidgetAnchor, GraphicsWidget):
    """
    GraphicsWidget displaying text.
    Used mainly as axis labels, titles, etc.
    
    Note: To display text inside a scaled view (ViewBox, PlotWidget, etc) use TextItem
    """
    item: Incomplete
    opts: Incomplete
    def __init__(self, text: str = ' ', parent: Incomplete | None = None, angle: int = 0, **args) -> None: ...
    def setAttr(self, attr, value) -> None:
        """Set default text properties. See setText() for accepted parameters."""
    text: Incomplete
    def setText(self, text, **args) -> None:
        """Set the text and text properties in the label. Accepts optional arguments for auto-generating
        a CSS style string:

        ==================== ==============================
        **Style Arguments:**
        family               (str) example: 'Cantarell'
        color                (str) example: '#CCFF00'
        size                 (str) example: '8pt'
        bold                 (bool)
        italic               (bool)
        ==================== ==============================
        """
    def resizeEvent(self, ev) -> None: ...
    angle: Incomplete
    def setAngle(self, angle) -> None: ...
    def updateMin(self) -> None: ...
    def sizeHint(self, hint, constraint): ...
    def itemRect(self): ...
