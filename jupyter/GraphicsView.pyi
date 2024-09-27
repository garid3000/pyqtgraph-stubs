import jupyter_rfb
from _typeshed import Incomplete

__all__ = ['GraphicsLayoutWidget', 'PlotWidget']

class GraphicsView(jupyter_rfb.RemoteFrameBuffer):
    """jupyter_rfb.RemoteFrameBuffer sub-class that wraps around
    :class:`GraphicsView <pyqtgraph.GraphicsView>`.

    Generally speaking, there is no Qt event loop running. The implementation works by
    requesting a render() of the scene. Thus things that would work for exporting
    purposes would be expected to work here. Things that are not part of the scene
    would not work, e.g. context menus, tooltips.

    This class should not be used directly. Its corresponding sub-classes
    :class:`GraphicsLayoutWidget <pyqtgraph.jupyter.GraphicsLayoutWidget>` and
    :class:`PlotWidget <pyqtgraph.jupyter.PlotWidget>` should be used instead."""
    gfxView: Incomplete
    logical_size: Incomplete
    pixel_ratio: float
    def __init__(self, **kwds) -> None: ...
    def get_frame(self): ...
    def handle_event(self, event) -> None: ...

class GraphicsLayoutWidget(GraphicsView):
    """jupyter_rfb analogue of
    :class:`GraphicsLayoutWidget <pyqtgraph.GraphicsLayoutWidget>`."""
    gfxLayout: Incomplete
    def __init__(self, **kwds) -> None: ...
    def addPlot(self, *args, **kwds): ...
    def addViewBox(self, *args, **kwds): ...

class PlotWidget(GraphicsView):
    """jupyter_rfb analogue of
    :class:`PlotWidget <pyqtgraph.PlotWidget>`."""
    plotItem: Incomplete
    def __init__(self, **kwds) -> None: ...
    def getPlotItem(self): ...
    def __getattr__(self, attr): ...
