from . import GraphicsLayout
from _typeshed import Incomplete

__all__ = ['MultiPlotItem']

class MultiPlotItem(GraphicsLayout.GraphicsLayout):
    """
    :class:`~pyqtgraph.GraphicsLayout` that automatically generates a grid of
    plots from a MetaArray.

    .. seealso:: :class:`~pyqtgraph.MultiPlotWidget`: Widget containing a MultiPlotItem
    """
    plots: Incomplete
    def __init__(self, *args, **kwds) -> None: ...
    def plot(self, data, **plotArgs) -> None:
        """Plot the data from a MetaArray with each array column as a separate
        :class:`~pyqtgraph.PlotItem`.

        Axis labels are automatically extracted from the array info.

        ``plotArgs`` are passed to :meth:`PlotItem.plot
        <pyqtgraph.PlotItem.plot>`.
        """
    def close(self) -> None: ...
