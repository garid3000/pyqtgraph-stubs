from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['IsocurveItem']

class IsocurveItem(GraphicsObject):
    """
    **Bases:** :class:`GraphicsObject <pyqtgraph.GraphicsObject>`
    
    Item displaying an isocurve of a 2D array. To align this item correctly with an 
    ImageItem, call ``isocurve.setParentItem(image)``.
    """
    level: Incomplete
    data: Incomplete
    path: Incomplete
    axisOrder: Incomplete
    def __init__(self, data: Incomplete | None = None, level: int = 0, pen: str = 'w', axisOrder: Incomplete | None = None) -> None:
        """
        Create a new isocurve item. 
        
        ==============  ===============================================================
        **Arguments:**
        data            A 2-dimensional ndarray. Can be initialized as None, and set
                        later using :func:`setData <pyqtgraph.IsocurveItem.setData>`
        level           The cutoff value at which to draw the isocurve.
        pen             The color of the curve item. Can be anything valid for
                        :func:`mkPen <pyqtgraph.mkPen>`
        axisOrder       May be either 'row-major' or 'col-major'. By default this uses
                        the ``imageAxisOrder``
                        :ref:`global configuration option <apiref_config>`.
        ==============  ===============================================================
        """
    def setData(self, data, level: Incomplete | None = None) -> None:
        """
        Set the data/image to draw isocurves for.
        
        ==============  ========================================================================
        **Arguments:**
        data            A 2-dimensional ndarray.
        level           The cutoff value at which to draw the curve. If level is not specified,
                        the previously set level is used.
        ==============  ========================================================================
        """
    def setLevel(self, level) -> None:
        """Set the level at which the isocurve is drawn."""
    pen: Incomplete
    def setPen(self, *args, **kwargs) -> None:
        """Set the pen used to draw the isocurve. Arguments can be any that are valid 
        for :func:`mkPen <pyqtgraph.mkPen>`"""
    brush: Incomplete
    def setBrush(self, *args, **kwargs) -> None:
        """Set the brush used to draw the isocurve. Arguments can be any that are valid 
        for :func:`mkBrush <pyqtgraph.mkBrush>`"""
    def updateLines(self, data, level) -> None: ...
    def boundingRect(self): ...
    def generatePath(self) -> None: ...
    def paint(self, p, *args) -> None: ...
