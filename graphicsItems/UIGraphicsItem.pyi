from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['UIGraphicsItem']

class UIGraphicsItem(GraphicsObject):
    """
    Base class for graphics items with boundaries relative to a GraphicsView or ViewBox.
    The purpose of this class is to allow the creation of GraphicsItems which live inside 
    a scalable view, but whose boundaries will always stay fixed relative to the view's boundaries.
    For example: GridItem, InfiniteLine
    
    The view can be specified on initialization or it can be automatically detected when the item is painted.
    
    NOTE: Only the item's boundingRect is affected; the item is not transformed in any way. Use viewRangeChanged
    to respond to changes in the view.
    """
    def __init__(self, bounds: Incomplete | None = None, parent: Incomplete | None = None) -> None:
        """
        ============== =============================================================================
        **Arguments:**
        bounds         QRectF with coordinates relative to view box. The default is QRectF(0,0,1,1),
                       which means the item will have the same bounds as the view.
        ============== =============================================================================
        """
    def paint(self, *args) -> None: ...
    def itemChange(self, change, value): ...
    def boundingRect(self): ...
    def dataBounds(self, axis, frac: float = 1.0, orthoRange: Incomplete | None = None) -> None:
        """Called by ViewBox for determining the auto-range bounds.
        By default, UIGraphicsItems are excluded from autoRange."""
    def viewRangeChanged(self) -> None:
        """Called when the view widget/viewbox is resized/rescaled"""
    def setNewBounds(self) -> None:
        """Update the item's bounding rect to match the viewport"""
    def setPos(self, *args) -> None: ...
    def mouseShape(self):
        """Return the shape of this item after expanding by 2 pixels"""
