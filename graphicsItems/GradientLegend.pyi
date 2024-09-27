from .UIGraphicsItem import UIGraphicsItem
from _typeshed import Incomplete

__all__ = ['GradientLegend']

class GradientLegend(UIGraphicsItem):
    """
    Draws a color gradient rectangle along with text labels denoting the value at specific
    points along the gradient.
    """
    size: Incomplete
    offset: Incomplete
    brush: Incomplete
    pen: Incomplete
    textPen: Incomplete
    labels: Incomplete
    gradient: Incomplete
    def __init__(self, size, offset) -> None: ...
    def setGradient(self, g) -> None: ...
    def setColorMap(self, colormap) -> None:
        """
        Set displayed gradient from a :class:`~pyqtgraph.ColorMap` object.
        """
    def setIntColorScale(self, minVal, maxVal, *args, **kargs) -> None: ...
    def setLabels(self, l) -> None:
        """Defines labels to appear next to the color scale. Accepts a dict of {text: value} pairs"""
    b: Incomplete
    def paint(self, p, opt, widget) -> None: ...
