from .TextItem import TextItem
from .UIGraphicsItem import UIGraphicsItem
from _typeshed import Incomplete

__all__ = ['TargetItem', 'TargetLabel']

class TargetItem(UIGraphicsItem):
    """Draws a draggable target symbol (circle plus crosshair).

    The size of TargetItem will remain fixed on screen even as the view is zoomed.
    Includes an optional text label.
    """
    sigPositionChanged: Incomplete
    sigPositionChangeFinished: Incomplete
    movable: Incomplete
    moving: bool
    mouseHovering: bool
    currentPen: Incomplete
    currentBrush: Incomplete
    scale: Incomplete
    def __init__(self, pos: Incomplete | None = None, size: int = 10, symbol: str = 'crosshair', pen: Incomplete | None = None, hoverPen: Incomplete | None = None, brush: Incomplete | None = None, hoverBrush: Incomplete | None = None, movable: bool = True, label: Incomplete | None = None, labelOpts: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        pos : list, tuple, QPointF, QPoint, Optional
            Initial position of the symbol.  Default is (0, 0)
        size : int
            Size of the symbol in pixels.  Default is 10.
        pen : QPen, tuple, list or str
            Pen to use when drawing line. Can be any arguments that are valid
            for :func:`~pyqtgraph.mkPen`. Default pen is transparent yellow.
        brush : QBrush, tuple, list, or str
            Defines the brush that fill the symbol. Can be any arguments that
            is valid for :func:`~pyqtgraph.mkBrush`. Default is transparent
            blue.
        movable : bool
            If True, the symbol can be dragged to a new position by the user.
        hoverPen : QPen, tuple, list, or str
            Pen to use when drawing symbol when hovering over it. Can be any
            arguments that are valid for :func:`~pyqtgraph.mkPen`. Default pen
            is red.
        hoverBrush : QBrush, tuple, list or str
            Brush to use to fill the symbol when hovering over it. Can be any
            arguments that is valid for :func:`~pyqtgraph.mkBrush`. Default is
            transparent blue.
        symbol : QPainterPath or str
            QPainterPath to use for drawing the target, should be centered at
            ``(0, 0)`` with ``max(width, height) == 1.0``.  Alternatively a string
            which can be any symbol accepted by
            :func:`~pyqtgraph.ScatterPlotItem.setSymbol`
        label : bool, str or callable, optional
            Text to be displayed in a label attached to the symbol, or None to
            show no label (default is None). May optionally include formatting
            strings to display the symbol value, or a callable that accepts x
            and y as inputs.  If True, the label is ``x = {: >.3n}\\ny = {: >.3n}``
            False or None will result in no text being displayed
        labelOpts : dict
            A dict of keyword arguments to use when constructing the text
            label. See :class:`TargetLabel` and :class:`~pyqtgraph.TextItem`
        """
    def setPos(self, *args) -> None:
        """Method to set the position to ``(x, y)`` within the plot view

        Parameters
        ----------
        args : tuple or list or QtCore.QPointF or QtCore.QPoint or Point or float
            Two float values or a container that specifies ``(x, y)`` position where the
            TargetItem should be placed

        Raises
        ------
        TypeError
            If args cannot be used to instantiate a Point
        """
    brush: Incomplete
    def setBrush(self, *args, **kwargs) -> None:
        """Set the brush that fills the symbol. Allowable arguments are any that
        are valid for :func:`~pyqtgraph.mkBrush`.
        """
    hoverBrush: Incomplete
    def setHoverBrush(self, *args, **kwargs) -> None:
        """Set the brush that fills the symbol when hovering over it. Allowable
        arguments are any that are valid for :func:`~pyqtgraph.mkBrush`.
        """
    pen: Incomplete
    def setPen(self, *args, **kwargs) -> None:
        """Set the pen for drawing the symbol. Allowable arguments are any that
        are valid for :func:`~pyqtgraph.mkPen`."""
    hoverPen: Incomplete
    def setHoverPen(self, *args, **kwargs) -> None:
        """Set the pen for drawing the symbol when hovering over it. Allowable
        arguments are any that are valid for
        :func:`~pyqtgraph.mkPen`."""
    def boundingRect(self): ...
    def paint(self, p, *_) -> None: ...
    def setPath(self, path) -> None: ...
    def shape(self): ...
    def generateShape(self): ...
    symbolOffset: Incomplete
    def mouseDragEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def setMouseHover(self, hover) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def viewTransformChanged(self) -> None: ...
    def pos(self):
        """Provides the current position of the TargetItem

        Returns
        -------
        Point
            pg.Point of the current position of the TargetItem
        """
    def label(self):
        """Provides the TargetLabel if it exists

        Returns
        -------
        TargetLabel or None
            If a TargetLabel exists for this TargetItem, return that, otherwise
            return None
        """
    def setLabel(self, text: Incomplete | None = None, labelOpts: Incomplete | None = None) -> None:
        """Method to call to enable or disable the TargetLabel for displaying text

        Parameters
        ----------
        text : Callable or str, optional
            Details how to format the text, by default None
            If None, do not show any text next to the TargetItem
            If Callable, then the label will display the result of ``text(x, y)``
            If a fromatted string, then the output of ``text.format(x, y)`` will be
            displayed
            If a non-formatted string, then the text label will display ``text``, by
            default None
        labelOpts : dict, optional
            These arguments are passed on to :class:`~pyqtgraph.TextItem`
        """

class TargetLabel(TextItem):
    """A TextItem that attaches itself to a TargetItem.

    This class extends TextItem with the following features :
      * Automatically positions adjacent to the symbol at a fixed position.
      * Automatically reformats text when the symbol location has changed.

    Parameters
    ----------
    target : TargetItem
        The TargetItem to which this label will be attached to.
    text : str or callable, Optional
        Governs the text displayed, can be a fixed string or a format string
        that accepts the x, and y position of the target item; or be a callable
        method that accepts a tuple (x, y) and returns a string to be displayed.
        If None, an empty string is used.  Default is None
    offset : tuple or list or QPointF or QPoint
        Position to set the anchor of the TargetLabel away from the center of
        the target in pixels, by default it is (20, 0).
    anchor : tuple or list or QPointF or QPoint
        Position to rotate the TargetLabel about, and position to set the
        offset value to see :class:`~pyqtgraph.TextItem` for more information.
    kwargs : dict 
        kwargs contains arguments that are passed onto
        :class:`~pyqtgraph.TextItem` constructor, excluding text parameter
    """
    offset: Incomplete
    target: Incomplete
    def __init__(self, target, text: str = '', offset=(20, 0), anchor=(0, 0.5), **kwargs) -> None: ...
    def format(self): ...
    def setFormat(self, text) -> None:
        """Method to set how the TargetLabel should display the text.  This
        method should be called from TargetItem.setLabel directly.

        Parameters
        ----------
        text : Callable or str
            Details how to format the text.
            If Callable, then the label will display the result of ``text(x, y)``
            If a fromatted string, then the output of ``text.format(x, y)`` will be
            displayed
            If a non-formatted string, then the text label will display ``text``
        """
    def valueChanged(self) -> None: ...
    def viewTransformChanged(self): ...
    def mouseClickEvent(self, ev): ...
    def mouseDragEvent(self, ev) -> None: ...
