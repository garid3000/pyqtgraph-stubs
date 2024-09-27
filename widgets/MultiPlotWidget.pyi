from .GraphicsView import GraphicsView
from _typeshed import Incomplete

__all__ = ['MultiPlotWidget']

class MultiPlotWidget(GraphicsView):
    """Widget implementing a :class:`~pyqtgraph.GraphicsView` with a single
    :class:`~pyqtgraph.MultiPlotItem` inside."""
    minPlotHeight: int
    mPlotItem: Incomplete
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def __getattr__(self, attr): ...
    def setMinimumPlotHeight(self, min) -> None:
        """Set the minimum height for each sub-plot displayed. 
        
        If the total height of all plots is greater than the height of the 
        widget, then a scroll bar will appear to provide access to the entire
        set of plots.
        
        Added in version 0.9.9
        """
    def widgetGroupInterface(self): ...
    def saveState(self): ...
    def restoreState(self, state) -> None: ...
    def close(self) -> None: ...
    def setRange(self, *args, **kwds) -> None: ...
    range: Incomplete
    def resizeEvent(self, ev) -> None: ...
