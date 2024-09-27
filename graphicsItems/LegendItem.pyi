from .GraphicsWidget import GraphicsWidget
from .GraphicsWidgetAnchor import GraphicsWidgetAnchor
from _typeshed import Incomplete

__all__ = ['LegendItem', 'ItemSample']

class LegendItem(GraphicsWidgetAnchor, GraphicsWidget):
    """
    Displays a legend used for describing the contents of a plot.

    LegendItems are most commonly created by calling :meth:`PlotItem.addLegend
    <pyqtgraph.PlotItem.addLegend>`.

    Note that this item should *not* be added directly to a PlotItem (via
    :meth:`PlotItem.addItem <pyqtgraph.PlotItem.addItem>`). Instead, make it a
    direct descendant of the PlotItem::

        legend.setParentItem(plotItem)

    """
    layout: Incomplete
    items: Incomplete
    size: Incomplete
    frame: Incomplete
    columnCount: Incomplete
    rowCount: int
    sampleType: Incomplete
    opts: Incomplete
    def __init__(self, size: Incomplete | None = None, offset: Incomplete | None = None, horSpacing: int = 25, verSpacing: int = 0, pen: Incomplete | None = None, brush: Incomplete | None = None, labelTextColor: Incomplete | None = None, frame: bool = True, labelTextSize: str = '9pt', colCount: int = 1, sampleType: Incomplete | None = None, **kwargs) -> None:
        """
        ==============  ===============================================================
        **Arguments:**
        size            Specifies the fixed size (width, height) of the legend. If
                        this argument is omitted, the legend will automatically resize
                        to fit its contents.
        offset          Specifies the offset position relative to the legend's parent.
                        Positive values offset from the left or top; negative values
                        offset from the right or bottom. If offset is None, the
                        legend must be anchored manually by calling anchor() or
                        positioned by calling setPos().
        horSpacing      Specifies the spacing between the line symbol and the label.
        verSpacing      Specifies the spacing between individual entries of the legend
                        vertically. (Can also be negative to have them really close)
        pen             Pen to use when drawing legend border. Any single argument
                        accepted by :func:`mkPen <pyqtgraph.mkPen>` is allowed.
        brush           QBrush to use as legend background filling. Any single argument
                        accepted by :func:`mkBrush <pyqtgraph.mkBrush>` is allowed.
        labelTextColor  Pen to use when drawing legend text. Any single argument
                        accepted by :func:`mkPen <pyqtgraph.mkPen>` is allowed.
        labelTextSize   Size to use when drawing legend text. Accepts CSS style
                        string arguments, e.g. '9pt'.
        colCount        Specifies the integer number of columns that the legend should
                        be divided into. The number of rows will be calculated
                        based on this argument. This is useful for plots with many
                        curves displayed simultaneously. Default: 1 column.
        sampleType      Customizes the item sample class of the `LegendItem`.
        ==============  ===============================================================

        """
    def setSampleType(self, sample) -> None:
        """Set the new sample item claspes"""
    def offset(self):
        """Get the offset position relative to the parent."""
    def setOffset(self, offset) -> None:
        """Set the offset position relative to the parent."""
    def pen(self):
        """Get the QPen used to draw the border around the legend."""
    def setPen(self, *args, **kargs) -> None:
        """Set the pen used to draw a border around the legend.

        Accepts the same arguments as :func:`~pyqtgraph.mkPen`.
        """
    def brush(self):
        """Get the QBrush used to draw the legend background."""
    def setBrush(self, *args, **kargs) -> None:
        """Set the brush used to draw the legend background.

        Accepts the same arguments as :func:`~pyqtgraph.mkBrush`.
        """
    def labelTextColor(self):
        """Get the QColor used for the item labels."""
    def setLabelTextColor(self, *args, **kargs) -> None:
        """Set the color of the item labels.

        Accepts the same arguments as :func:`~pyqtgraph.mkColor`.
        """
    def labelTextSize(self):
        """Get the `labelTextSize` used for the item labels."""
    def setLabelTextSize(self, size) -> None:
        """Set the `size` of the item labels.

        Accepts the CSS style string arguments, e.g. '8pt'.
        """
    def setParentItem(self, p):
        """Set the parent."""
    def addItem(self, item, name) -> None:
        """
        Add a new entry to the legend.

        ==============  ========================================================
        **Arguments:**
        item            A :class:`~pyqtgraph.PlotDataItem` from which the line
                        and point style of the item will be determined or an
                        instance of ItemSample (or a subclass), allowing the
                        item display to be customized.
        title           The title to display for this item. Simple HTML allowed.
        ==============  ========================================================
        """
    def setColumnCount(self, columnCount) -> None:
        """change the orientation of all items of the legend
        """
    def getLabel(self, plotItem):
        """Return the labelItem inside the legend for a given plotItem

        The label-text can be changed via labelItem.setText
        """
    def removeItem(self, item) -> None:
        """Removes one item from the legend.

        ==============  ========================================================
        **Arguments:**
        item            The item to remove or its name.
        ==============  ========================================================
        """
    def clear(self) -> None:
        """Remove all items from the legend."""
    def updateSize(self) -> None: ...
    def boundingRect(self): ...
    def paint(self, p, *args) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def mouseDragEvent(self, ev) -> None: ...

class ItemSample(GraphicsWidget):
    """Class responsible for drawing a single item in a LegendItem (sans label)
    """
    item: Incomplete
    def __init__(self, item) -> None: ...
    def boundingRect(self): ...
    def paint(self, p, *args) -> None: ...
    def mouseClickEvent(self, event) -> None:
        """Use the mouseClick event to toggle the visibility of the plotItem
        """
