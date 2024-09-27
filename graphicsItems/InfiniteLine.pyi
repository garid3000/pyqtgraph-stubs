from ..Qt import QtCore, QtGui #<D-i> , QtGui, QtWidgets, isQObjectAlive, QT_LIB
from .GraphicsObject import GraphicsObject
from .TextItem import TextItem
from _typeshed import Incomplete

__all__ = ['InfiniteLine', 'InfLineLabel']

class InfiniteLine(GraphicsObject):
    """
    **Bases:** :class:`GraphicsObject <pyqtgraph.GraphicsObject>`

    Displays a line of infinite length.
    This line may be dragged to indicate a position in data coordinates.

    =============================== ===================================================
    **Signals:**
    sigDragged(self)
    sigPositionChangeFinished(self)
    sigPositionChanged(self)
    sigClicked(self, ev)
    =============================== ===================================================
    """
    sigDragged: Incomplete
    sigPositionChangeFinished: Incomplete
    sigPositionChanged: Incomplete
    sigClicked: Incomplete
    maxRange: Incomplete
    moving: bool
    mouseHovering: bool
    p: Incomplete
    span: Incomplete
    currentPen: Incomplete
    markers: Incomplete
    label: Incomplete
    def __init__(self, pos: QtCore.QPointF | float | None = None, angle: int = 90, pen: QtGui.QPen | None = None, movable: bool = False, bounds: tuple[float,float] | list[float] | None = None, hoverPen: QtGui.QPen | None = None, label: str | None = None, labelOpts: dict[str,str|tuple[int, int, int]|float|tuple[int,int,int,int]|bool] | None = None, span:tuple[float,float]=(0, 1), markers: list[tuple[str, float, float]] | None = None, name: str | None = None) -> None:
        """
        =============== ==================================================================
        **Arguments:**
        pos             Position of the line. This can be a QPointF or a single value for
                        vertical/horizontal lines.
        angle           Angle of line in degrees. 0 is horizontal, 90 is vertical.
        pen             Pen to use when drawing line. Can be any arguments that are valid
                        for :func:`mkPen <pyqtgraph.mkPen>`. Default pen is transparent
                        yellow.
        hoverPen        Pen to use when the mouse cursor hovers over the line.
                        Only used when movable=True.
        movable         If True, the line can be dragged to a new position by the user.
        bounds          Optional [min, max] bounding values. Bounds are only valid if the
                        line is vertical or horizontal.
        hoverPen        Pen to use when drawing line when hovering over it. Can be any
                        arguments that are valid for :func:`mkPen <pyqtgraph.mkPen>`.
                        Default pen is red.
        label           Text to be displayed in a label attached to the line, or
                        None to show no label (default is None). May optionally
                        include formatting strings to display the line value.
        labelOpts       A dict of keyword arguments to use when constructing the
                        text label. See :class:`InfLineLabel <pyqtgraph.graphicsItems.InfiniteLine.InfLineLabel>`.
        span            Optional tuple (min, max) giving the range over the view to draw
                        the line. For example, with a vertical line, use span=(0.5, 1)
                        to draw only on the top half of the view.
        markers         List of (marker, position, size) tuples, one per marker to display
                        on the line. See the addMarker method.
        name            Name of the item
        =============== ==================================================================
        """
    movable: Incomplete
    def setMovable(self, m) -> None:
        """Set whether the line is movable by the user."""
    def setBounds(self, bounds) -> None:
        """Set the (minimum, maximum) allowable values when dragging."""
    def bounds(self):
        """Return the (minimum, maximum) values allowed when dragging.
        """
    pen: Incomplete
    def setPen(self, *args, **kwargs) -> None:
        """Set the pen for drawing the line. Allowable arguments are any that are valid
        for :func:`mkPen <pyqtgraph.mkPen>`."""
    hoverPen: Incomplete
    def setHoverPen(self, *args, **kwargs) -> None:
        """Set the pen for drawing the line while the mouse hovers over it.
        Allowable arguments are any that are valid
        for :func:`mkPen <pyqtgraph.mkPen>`.

        If the line is not movable, then hovering is also disabled.

        Added in version 0.9.9."""
    def addMarker(self, marker, position: float = 0.5, size: float = 10.0) -> None:
        """Add a marker to be displayed on the line.

        ============= =========================================================
        **Arguments**
        marker        String indicating the style of marker to add:
                      ``'<|'``, ``'|>'``, ``'>|'``, ``'|<'``, ``'<|>'``,
                      ``'>|<'``, ``'^'``, ``'v'``, ``'o'``
        position      Position (0.0-1.0) along the visible extent of the line
                      to place the marker. Default is 0.5.
        size          Size of the marker in pixels. Default is 10.0.
        ============= =========================================================
        """
    def clearMarkers(self) -> None:
        """ Remove all markers from this line.
        """
    angle: Incomplete
    def setAngle(self, angle) -> None:
        """
        Takes angle argument in degrees.
        0 is horizontal; 90 is vertical.

        Note that the use of value() and setValue() changes if the line is
        not vertical or horizontal.
        """
    def setPos(self, pos: float) -> None: ...
    def getXPos(self): ...
    def getYPos(self): ...
    def getPos(self): ...
    def value(self):
        """Return the value of the line. Will be a single number for horizontal and
        vertical lines, and a list of [x,y] values for diagonal lines."""
    def setValue(self, v) -> None:
        """Set the position of the line. If line is horizontal or vertical, v can be
        a single value. Otherwise, a 2D coordinate must be specified (list, tuple and
        QPointF are all acceptable)."""
    def setSpan(self, mn, mx) -> None: ...
    def boundingRect(self): ...
    def paint(self, p, *args) -> None: ...
    def dataBounds(self, axis, frac: float = 1.0, orthoRange: Incomplete | None = None): ...
    cursorOffset: Incomplete
    startPosition: Incomplete
    def mouseDragEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def setMouseHover(self, hover) -> None: ...
    def viewTransformChanged(self) -> None:
        """
        Called whenever the transformation matrix of the view has changed.
        (eg, the view range has changed or the view was resized)
        """
    def setName(self, name) -> None: ...
    def name(self): ...

class InfLineLabel(TextItem):
    """
    A TextItem that attaches itself to an InfiniteLine.

    This class extends TextItem with the following features:

      * Automatically positions adjacent to the line at a fixed position along
        the line and within the view box.
      * Automatically reformats text when the line value has changed.
      * Can optionally be dragged to change its location along the line.
      * Optionally aligns to its parent line.

    =============== ==================================================================
    **Arguments:**
    line            The InfiniteLine to which this label will be attached.
    text            String to display in the label. May contain a {value} formatting
                    string to display the current value of the line.
    movable         Bool; if True, then the label can be dragged along the line.
    position        Relative position (0.0-1.0) within the view to position the label
                    along the line.
    anchors         List of (x,y) pairs giving the text anchor positions that should
                    be used when the line is moved to one side of the view or the
                    other. This allows text to switch to the opposite side of the line
                    as it approaches the edge of the view. These are automatically
                    selected for some common cases, but may be specified if the
                    default values give unexpected results.
    =============== ==================================================================

    All extra keyword arguments are passed to TextItem. A particularly useful
    option here is to use `rotateAxis=(1, 0)`, which will cause the text to
    be automatically rotated parallel to the line.
    """
    line: Incomplete
    movable: Incomplete
    moving: bool
    orthoPos: Incomplete
    format: Incomplete
    anchors: Incomplete
    def __init__(self, line, text: str = '', movable: bool = False, position: float = 0.5, anchors: Incomplete | None = None, **kwds) -> None: ...
    def valueChanged(self) -> None: ...
    def getEndpoints(self): ...
    def updatePosition(self) -> None: ...
    def setVisible(self, v) -> None: ...
    def setMovable(self, m) -> None:
        """Set whether this label is movable by dragging along the line.
        """
    def setPosition(self, p) -> None:
        """Set the relative position (0.0-1.0) of this label within the view box
        and along the line.

        For horizontal (angle=0) and vertical (angle=90) lines, a value of 0.0
        places the text at the bottom or left of the view, respectively.
        """
    def setFormat(self, text) -> None:
        '''Set the text format string for this label.

        May optionally contain "{value}" to include the lines current value
        (the text will be reformatted whenever the line is moved).
        '''
    def mouseDragEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def viewTransformChanged(self) -> None: ...
