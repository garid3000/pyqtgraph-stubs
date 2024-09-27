from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['CurvePoint', 'CurveArrow']

class CurvePoint(GraphicsObject):
    """A GraphicsItem that sets its location to a point on a PlotCurveItem.
    Also rotates to be tangent to the curve.
    The position along the curve is a Qt property, and thus can be easily animated.
    
    Note: This class does not display anything; see CurveArrow for an applied example
    """
    curve: Incomplete
    def __init__(self, curve, index: int = 0, pos: Incomplete | None = None, rotate: bool = True) -> None:
        """Position can be set either as an index referring to the sample number or
        the position 0.0 - 1.0
        If *rotate* is True, then the item rotates to match the tangent of the curve.
        """
    def setPos(self, pos) -> None: ...
    def setIndex(self, index) -> None: ...
    def event(self, ev): ...
    def boundingRect(self): ...
    def paint(self, *args) -> None: ...
    def makeAnimation(self, prop: str = 'position', start: float = 0.0, end: float = 1.0, duration: int = 10000, loop: int = 1): ...

class CurveArrow(CurvePoint):
    """Provides an arrow that points to any specific sample on a PlotCurveItem.
    Provides properties that can be animated."""
    arrow: Incomplete
    def __init__(self, curve, index: int = 0, pos: Incomplete | None = None, **opts) -> None: ...
    def setStyle(self, **opts): ...
