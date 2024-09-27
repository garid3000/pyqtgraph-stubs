from .GraphicsWidget import GraphicsWidget
from _typeshed import Incomplete

__all__ = ['HistogramLUTItem']

class HistogramLUTItem(GraphicsWidget):
    """
    :class:`~pyqtgraph.GraphicsWidget` with controls for adjusting the display of an
    :class:`~pyqtgraph.ImageItem`.

    Includes:

      - Image histogram
      - Movable region over the histogram to select black/white levels
      - Gradient editor to define color lookup table for single-channel images

    Parameters
    ----------
    image : pyqtgraph.ImageItem, optional
        If provided, control will be automatically linked to the image and changes to
        the control will be reflected in the image's appearance. This may also be set
        via :meth:`setImageItem`.
    fillHistogram : bool, optional
        By default, the histogram is rendered with a fill. Performance may be improved
        by disabling the fill. Additional control over the fill is provided by
        :meth:`fillHistogram`.
    levelMode : str, optional
        'mono' (default)
            One histogram with a :class:`~pyqtgraph.LinearRegionItem` is displayed to
            control the black/white levels of the image. This option may be used for
            color images, in which case the histogram and levels correspond to all
            channels of the image.
        'rgba'
            A histogram and level control pair is provided for each image channel. The
            alpha channel histogram and level control are only shown if the image
            contains an alpha channel.
    gradientPosition : str, optional
        Position of the gradient editor relative to the histogram. Must be one of
        {'right', 'left', 'top', 'bottom'}. 'right' and 'left' options should be used
        with a 'vertical' orientation; 'top' and 'bottom' options are for 'horizontal'
        orientation.
    orientation : str, optional
        The orientation of the axis along which the histogram is displayed. Either
        'vertical' (default) or 'horizontal'.

    Attributes
    ----------
    sigLookupTableChanged : QtCore.Signal
        Emits the HistogramLUTItem itself when the gradient changes
    sigLevelsChanged : QtCore.Signal
        Emits the HistogramLUTItem itself while the movable region is changing
    sigLevelChangeFinished : QtCore.Signal
        Emits the HistogramLUTItem itself when the movable region is finished changing

    See Also
    --------
    :class:`~pyqtgraph.ImageItem`
        HistogramLUTItem is most useful when paired with an ImageItem.
    :class:`~pyqtgraph.ImageView`
        Widget containing a paired ImageItem and HistogramLUTItem.
    :class:`~pyqtgraph.HistogramLUTWidget`
        QWidget containing a HistogramLUTItem for widget-based layouts.
    """
    sigLookupTableChanged: Incomplete
    sigLevelsChanged: Incomplete
    sigLevelChangeFinished: Incomplete
    lut: Incomplete
    imageItem: Incomplete
    levelMode: Incomplete
    orientation: Incomplete
    gradientPosition: Incomplete
    layout: Incomplete
    vb: Incomplete
    gradient: Incomplete
    regions: Incomplete
    region: Incomplete
    axis: Incomplete
    plots: Incomplete
    plot: Incomplete
    def __init__(self, image: Incomplete | None = None, fillHistogram: bool = True, levelMode: str = 'mono', gradientPosition: str = 'right', orientation: str = 'vertical') -> None: ...
    def fillHistogram(self, fill: bool = True, level: float = 0.0, color=(100, 100, 200)) -> None:
        '''Control fill of the histogram curve(s).

        Parameters
        ----------
        fill : bool, optional
            Set whether or not the histogram should be filled.
        level : float, optional
            Set the fill level. See :meth:`PlotCurveItem.setFillLevel
            <pyqtgraph.PlotCurveItem.setFillLevel>`. Only used if ``fill`` is True.
        color : color_like, optional
            Color to use for the fill when the histogram ``levelMode == "mono"``. See
            :meth:`PlotCurveItem.setBrush <pyqtgraph.PlotCurveItem.setBrush>`.
        '''
    def paint(self, p, *args) -> None: ...
    def setHistogramRange(self, mn, mx, padding: float = 0.1) -> None:
        """Set the X/Y range on the histogram plot, depending on the orientation. This disables auto-scaling."""
    def getHistogramRange(self):
        """Returns range on the histogram plot."""
    def autoHistogramRange(self) -> None:
        """Enable auto-scaling on the histogram plot."""
    def disableAutoHistogramRange(self) -> None:
        """Disable auto-scaling on the histogram plot."""
    def setImageItem(self, img) -> None:
        """Set an ImageItem to have its levels and LUT automatically controlled by this
        HistogramLUTItem.
        """
    def viewRangeChanged(self) -> None: ...
    def gradientChanged(self) -> None: ...
    def getLookupTable(self, img: Incomplete | None = None, n: Incomplete | None = None, alpha: Incomplete | None = None):
        """Return a lookup table from the color gradient defined by this
        HistogramLUTItem.
        """
    def regionChanged(self) -> None: ...
    def regionChanging(self) -> None: ...
    def imageChanged(self, autoLevel: bool = False, autoRange: bool = False) -> None: ...
    def getLevels(self):
        """Return the min and max levels.

        For rgba mode, this returns a list of the levels for each channel.
        """
    def setLevels(self, min: Incomplete | None = None, max: Incomplete | None = None, rgba: Incomplete | None = None) -> None:
        """Set the min/max (bright and dark) levels.

        Parameters
        ----------
        min : float, optional
            Minimum level.
        max : float, optional
            Maximum level.
        rgba : list, optional
            Sequence of (min, max) pairs for each channel for 'rgba' mode.
        """
    def setLevelMode(self, mode) -> None:
        """Set the method of controlling the image levels offered to the user.

        Options are 'mono' or 'rgba'.
        """
    def saveState(self): ...
    def restoreState(self, state) -> None: ...
