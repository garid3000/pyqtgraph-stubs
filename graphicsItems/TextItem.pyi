from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['TextItem']

class TextItem(GraphicsObject):
    """
    GraphicsItem displaying unscaled text (the text will always appear normal even inside a scaled ViewBox).
    """
    anchor: Incomplete
    rotateAxis: Incomplete
    textItem: Incomplete
    fill: Incomplete
    border: Incomplete
    def __init__(self, text: str = '', color =(200, 200, 200), html: Incomplete | None = None, anchor=(0, 0), border: Incomplete | None = None, fill: tuple[int, int, int, int]  | None = None, angle: int = 0, rotateAxis: Incomplete | None = None, ensureInBounds: bool = False) -> None:
        '''
        ================  =================================================================================
        **Arguments:**
        *text*            The text to display
        *color*           The color of the text (any format accepted by pg.mkColor)
        *html*            If specified, this overrides both *text* and *color*
        *anchor*          A QPointF or (x,y) sequence indicating what region of the text box will
                          be anchored to the item\'s position. A value of (0,0) sets the upper-left corner
                          of the text box to be at the position specified by setPos(), while a value of (1,1)
                          sets the lower-right corner.
        *border*          A pen to use when drawing the border
        *fill*            A brush to use when filling within the border
        *angle*           Angle in degrees to rotate text. Default is 0; text will be displayed upright.
        *rotateAxis*      If None, then a text angle of 0 always points along the +x axis of the scene.
                          If a QPointF or (x,y) sequence is given, then it represents a vector direction
                          in the parent\'s coordinate system that the 0-degree line will be aligned to. This
                          Allows text to follow both the position and orientation of its parent while still
                          discarding any scale and shear factors.
        *ensureInBounds*  Ensures that the entire TextItem will be visible when using autorange, but may
                          produce runaway scaling in certain circumstances (See issue #2642). Setting to
                          "True" retains legacy behavior.
        ================  =================================================================================


        The effects of the `rotateAxis` and `angle` arguments are added independently. So for example:

          * rotateAxis=None, angle=0 -> normal horizontal text
          * rotateAxis=None, angle=90 -> normal vertical text
          * rotateAxis=(1, 0), angle=0 -> text aligned with x axis of its parent
          * rotateAxis=(0, 1), angle=0 -> text aligned with y axis of its parent
          * rotateAxis=(1, 0), angle=90 -> text orthogonal to x axis of its parent
        '''
    def setText(self, text, color: Incomplete | None = None) -> None:
        """
        Set the text of this item.

        This method sets the plain text of the item; see also setHtml().
        """
    def setPlainText(self, text) -> None:
        """
        Set the plain text to be rendered by this item.

        See QtWidgets.QGraphicsTextItem.setPlainText().
        """
    def toPlainText(self): ...
    def setHtml(self, html) -> None:
        """
        Set the HTML code to be rendered by this item.

        See QtWidgets.QGraphicsTextItem.setHtml().
        """
    def toHtml(self): ...
    def setTextWidth(self, *args) -> None:
        """
        Set the width of the text.

        If the text requires more space than the width limit, then it will be
        wrapped into multiple lines.

        See QtWidgets.QGraphicsTextItem.setTextWidth().
        """
    def setFont(self, *args) -> None:
        """
        Set the font for this text.

        See QtWidgets.QGraphicsTextItem.setFont().
        """
    angle: Incomplete
    def setAngle(self, angle) -> None:
        """
        Set the angle of the text in degrees.

        This sets the rotation angle of the text as a whole, measured
        counter-clockwise from the x axis of the parent. Note that this rotation
        angle does not depend on horizontal/vertical scaling of the parent.
        """
    def setAnchor(self, anchor) -> None: ...
    color: Incomplete
    def setColor(self, color) -> None:
        """
        Set the color for this text.

        See QtWidgets.QGraphicsItem.setDefaultTextColor().
        """
    def updateTextPos(self) -> None: ...
    def dataBounds(self, ax, frac: float = 1.0, orthoRange: Incomplete | None = None):
        """
        Returns only the anchor point for when calulating view ranges.

        Sacrifices some visual polish for fixing issue #2642.
        """
    def boundingRect(self): ...
    def viewTransformChanged(self) -> None: ...
    def paint(self, p, *args) -> None: ...
    def setVisible(self, v) -> None: ...
    def updateTransform(self, force: bool = False) -> None: ...
