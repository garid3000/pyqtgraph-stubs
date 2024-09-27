from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['LinearRegionItem']

class LinearRegionItem(GraphicsObject):
    """
    **Bases:** :class:`GraphicsObject <pyqtgraph.GraphicsObject>`
    
    Used for marking a horizontal or vertical region in plots.
    The region can be dragged and is bounded by lines which can be dragged individually.
    
    ===============================  =============================================================================
    **Signals:**
    sigRegionChangeFinished(self)    Emitted when the user has finished dragging the region (or one of its lines)
                                     and when the region is changed programatically.
    sigRegionChanged(self)           Emitted while the user is dragging the region (or one of its lines)
                                     and when the region is changed programatically.
    ===============================  =============================================================================
    """
    sigRegionChangeFinished: Incomplete
    sigRegionChanged: Incomplete
    Vertical: int
    Horizontal: int
    orientation: Incomplete
    blockLineSignal: bool
    moving: bool
    mouseHovering: bool
    span: Incomplete
    swapMode: Incomplete
    clipItem: Incomplete
    lines: Incomplete
    def __init__(self, values=(0, 1), orientation: str = 'vertical', brush: Incomplete | None = None, pen: Incomplete | None = None, hoverBrush: Incomplete | None = None, hoverPen: Incomplete | None = None, movable: bool = True, bounds: Incomplete | None = None, span=(0, 1), swapMode: str = 'sort', clipItem: Incomplete | None = None) -> None:
        '''Create a new LinearRegionItem.
        
        ==============  =====================================================================
        **Arguments:**
        values          A list of the positions of the lines in the region. These are not
                        limits; limits can be set by specifying bounds.
        orientation     Options are \'vertical\' or \'horizontal\'
                        The default is \'vertical\', indicating that the region is bounded
                        by vertical lines.
        brush           Defines the brush that fills the region. Can be any arguments that
                        are valid for :func:`mkBrush <pyqtgraph.mkBrush>`. Default is
                        transparent blue.
        pen             The pen to use when drawing the lines that bound the region.
        hoverBrush      The brush to use when the mouse is hovering over the region.
        hoverPen        The pen to use when the mouse is hovering over the region.
        movable         If True, the region and individual lines are movable by the user; if
                        False, they are static.
        bounds          Optional [min, max] bounding values for the region
        span            Optional [min, max] giving the range over the view to draw
                        the region. For example, with a vertical line, use
                        ``span=(0.5, 1)`` to draw only on the top half of the
                        view.
        swapMode        Sets the behavior of the region when the lines are moved such that
                        their order reverses:

                          * "block" means the user cannot drag one line past the other
                          * "push" causes both lines to be moved if one would cross the other
                          * "sort" means that lines may trade places, but the output of
                            getRegion always gives the line positions in ascending order.
                          * None means that no attempt is made to handle swapped line
                            positions.

                        The default is "sort".
        clipItem        An item whose bounds will be used to limit the region bounds.
                        This is useful when a LinearRegionItem is added on top of an
                        :class:`~pyqtgraph.ImageItem` or
                        :class:`~pyqtgraph.PlotDataItem` and the visual region should
                        not extend beyond its range. This overrides ``bounds``.
        ==============  =====================================================================
        '''
    def getRegion(self):
        """Return the values at the edges of the region."""
    def setRegion(self, rgn) -> None:
        """Set the values for the edges of the region.
        
        ==============   ==============================================
        **Arguments:**
        rgn              A list or tuple of the lower and upper values.
        ==============   ==============================================
        """
    brush: Incomplete
    currentBrush: Incomplete
    def setBrush(self, *br, **kargs) -> None:
        """Set the brush that fills the region. Can have any arguments that are valid
        for :func:`mkBrush <pyqtgraph.mkBrush>`.
        """
    hoverBrush: Incomplete
    def setHoverBrush(self, *br, **kargs) -> None:
        """Set the brush that fills the region when the mouse is hovering over.
        Can have any arguments that are valid
        for :func:`mkBrush <pyqtgraph.mkBrush>`.
        """
    def setBounds(self, bounds) -> None:
        """Set ``(min, max)`` bounding values for the region.

        The current position is only affected it is outside the new bounds. See
        :func:`~pyqtgraph.LinearRegionItem.setRegion` to set the position of the region.

        Use ``(None, None)`` to disable bounds.
        """
    movable: Incomplete
    def setMovable(self, m: bool = True) -> None:
        """Set lines to be movable by the user, or not. If lines are movable, they will 
        also accept HoverEvents."""
    def setSpan(self, mn, mx) -> None: ...
    def setClipItem(self, item: Incomplete | None = None) -> None:
        """Set an item to which the region is bounded.

        If ``None``, bounds are disabled.
        """
    def boundingRect(self): ...
    def paint(self, p, *args) -> None: ...
    def dataBounds(self, axis, frac: float = 1.0, orthoRange: Incomplete | None = None): ...
    def lineMoved(self, i) -> None: ...
    def lineMoveFinished(self) -> None: ...
    cursorOffsets: Incomplete
    startPositions: Incomplete
    def mouseDragEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def setMouseHover(self, hover) -> None: ...
