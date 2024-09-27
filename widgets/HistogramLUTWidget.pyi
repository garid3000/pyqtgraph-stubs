from .GraphicsView import GraphicsView
from _typeshed import Incomplete

__all__ = ['HistogramLUTWidget']

class HistogramLUTWidget(GraphicsView):
    """QWidget wrapper for :class:`~pyqtgraph.HistogramLUTItem`.

    All parameters are passed along in creating the HistogramLUTItem.
    """
    item: Incomplete
    orientation: Incomplete
    def __init__(self, parent: Incomplete | None = None, *args, **kargs) -> None: ...
    def sizeHint(self): ...
    def __getattr__(self, attr): ...
