from OpenGL.GL import *
from ..GLGraphicsItem import GLGraphicsItem
from _typeshed import Incomplete

__all__ = ['GLTextItem']

class GLTextItem(GLGraphicsItem):
    """Draws text in 3D."""
    pos: Incomplete
    color: Incomplete
    text: str
    font: Incomplete
    def __init__(self, parentItem: Incomplete | None = None, **kwds) -> None:
        """All keyword arguments are passed to setData()"""
    def setData(self, **kwds) -> None:
        """
        Update the data displayed by this item. All arguments are optional;
        for example it is allowed to update text while leaving colors unchanged, etc.

        ====================  ==================================================
        **Arguments:**
        ------------------------------------------------------------------------
        pos                   (3,) array of floats specifying text location.
        color                 QColor or array of ints [R,G,B] or [R,G,B,A]. (Default: Qt.white)
        text                  String to display.
        font                  QFont (Default: QFont('Helvetica', 16))
        ====================  ==================================================
        """
    def paint(self) -> None: ...
