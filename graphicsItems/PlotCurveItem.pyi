from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['PlotCurveItem']

class PlotCurveItem(GraphicsObject):
    """
    Class representing a single plot curve. Instances of this class are created
    automatically as part of :class:`PlotDataItem <pyqtgraph.PlotDataItem>`; 
    these rarely need to be instantiated directly.

    Features:

      - Fast data update
      - Fill under curve
      - Mouse interaction

    =====================  ===============================================
    **Signals:**
    sigPlotChanged(self)   Emitted when the data being plotted has changed
    sigClicked(self, ev)   Emitted when the curve is clicked
    =====================  ===============================================
    """
    sigPlotChanged: Incomplete
    sigClicked: Incomplete
    metaData: Incomplete
    opts: Incomplete
    def __init__(self, *args, **kargs) -> None:
        """
        Forwards all arguments to :func:`setData <pyqtgraph.PlotCurveItem.setData>`.

        Some extra arguments are accepted as well:

        ==============  =======================================================
        **Arguments:**
        parent          The parent GraphicsObject (optional)
        clickable       If `True`, the item will emit ``sigClicked`` when it is
                        clicked on. Defaults to `False`.
        ==============  =======================================================
        """
    def implements(self, interface: Incomplete | None = None): ...
    def name(self): ...
    clickable: Incomplete
    def setClickable(self, s, width: Incomplete | None = None) -> None:
        """Sets whether the item responds to mouse clicks.

        The `width` argument specifies the width in pixels orthogonal to the
        curve that will respond to a mouse click.
        """
    def setCompositionMode(self, mode) -> None:
        """
        Change the composition mode of the item. This is useful when overlaying
        multiple items.
        
        Parameters
        ----------
        mode : ``QtGui.QPainter.CompositionMode``
            Composition of the item, often used when overlaying items.  Common
            options include:

            ``QPainter.CompositionMode.CompositionMode_SourceOver`` (Default)
            Image replaces the background if it is opaque. Otherwise, it uses
            the alpha channel to blend the image with the background.

            ``QPainter.CompositionMode.CompositionMode_Overlay`` Image color is
            mixed with the background color to reflect the lightness or
            darkness of the background

            ``QPainter.CompositionMode.CompositionMode_Plus`` Both the alpha
            and color of the image and background pixels are added together.

            ``QPainter.CompositionMode.CompositionMode_Plus`` The output is the
            image color multiplied by the background.

            See ``QPainter::CompositionMode`` in the Qt Documentation for more
            options and details
        """
    def getData(self): ...
    def dataBounds(self, ax, frac: float = 1.0, orthoRange: Incomplete | None = None): ...
    def pixelPadding(self): ...
    def boundingRect(self): ...
    def viewTransformChanged(self) -> None: ...
    def invalidateBounds(self) -> None: ...
    def setPen(self, *args, **kargs) -> None:
        """Set the pen used to draw the curve."""
    def setShadowPen(self, *args, **kargs) -> None:
        """
        Set the shadow pen used to draw behind the primary pen.
        This pen must have a larger width than the primary
        pen to be visible. Arguments are passed to 
        :func:`mkPen <pyqtgraph.mkPen>`
        """
    def setBrush(self, *args, **kargs) -> None:
        """
        Sets the brush used when filling the area under the curve. All 
        arguments are passed to :func:`mkBrush <pyqtgraph.mkBrush>`.
        """
    fillPath: Incomplete
    def setFillLevel(self, level) -> None:
        """Sets the level filled to when filling under the curve"""
    def setSkipFiniteCheck(self, skipFiniteCheck) -> None:
        """
        When it is known that the plot data passed to ``PlotCurveItem`` contains only finite numerical values,
        the `skipFiniteCheck` property can help speed up plotting. If this flag is set and the data contains 
        any non-finite values (such as `NaN` or `Inf`), unpredictable behavior will occur. The data might not
        be plotted, or there migth be significant performance impact.
        """
    def setData(self, *args, **kargs) -> None:
        """
        =============== =================================================================
        **Arguments:**
        x, y            (numpy arrays) Data to display
        pen             Pen to use when drawing. Any single argument accepted by
                        :func:`mkPen <pyqtgraph.mkPen>` is allowed.
        shadowPen       Pen for drawing behind the primary pen. Usually this
                        is used to emphasize the curve by providing a
                        high-contrast border. Any single argument accepted by
                        :func:`mkPen <pyqtgraph.mkPen>` is allowed.
        fillLevel       (float or None) Fill the area under the curve to
                        the specified value.
        fillOutline     (bool) If True, an outline surrounding the `fillLevel`
                        area is drawn.
        brush           Brush to use when filling. Any single argument accepted
                        by :func:`mkBrush <pyqtgraph.mkBrush>` is allowed.
        antialias       (bool) Whether to use antialiasing when drawing. This
                        is disabled by default because it decreases performance.
        stepMode        (str or None) If 'center', a step is drawn using the `x`
                        values as boundaries and the given `y` values are
                        associated to the mid-points between the boundaries of
                        each step. This is commonly used when drawing
                        histograms. Note that in this case, ``len(x) == len(y) + 1``
                        
                        If 'left' or 'right', the step is drawn assuming that
                        the `y` value is associated to the left or right boundary,
                        respectively. In this case ``len(x) == len(y)``
                        If not passed or an empty string or `None` is passed, the
                        step mode is not enabled.
        connect         Argument specifying how vertexes should be connected
                        by line segments. 
                        
                            | 'all' (default) indicates full connection. 
                            | 'pairs' draws one separate line segment for each two points given.
                            | 'finite' omits segments attached to `NaN` or `Inf` values. 
                            | For any other connectivity, specify an array of boolean values.
        compositionMode See :func:`setCompositionMode
                        <pyqtgraph.PlotCurveItem.setCompositionMode>`.
        skipFiniteCheck (bool, defaults to `False`) Optimization flag that can
                        speed up plotting by not checking and compensating for
                        `NaN` values.  If set to `True`, and `NaN` values exist, the
                        data may not be displayed or the plot may take a
                        significant performance hit.
        =============== =================================================================

        If non-keyword arguments are used, they will be interpreted as
        ``setData(y)`` for a single argument and ``setData(x, y)`` for two
        arguments.
        
        **Notes on performance:**
        
        Line widths greater than 1 pixel affect the performance as discussed in 
        the documentation of :class:`PlotDataItem <pyqtgraph.PlotDataItem>`.
        """
    yData: Incomplete
    xData: Incomplete
    path: Incomplete
    def updateData(self, *args, **kargs) -> None: ...
    def generatePath(self, x, y): ...
    def getPath(self): ...
    def setSegmentedLineMode(self, mode) -> None:
        """
        Sets the mode that decides whether or not lines are drawn as segmented lines. Drawing lines
        as segmented lines is more performant than the standard drawing method with continuous
        lines.

        Parameters
        ----------
        mode : str
               ``'auto'`` (default) segmented lines are drawn if the pen's width > 1, pen style is a
               solid line, the pen color is opaque and anti-aliasing is not enabled.

               ``'on'`` lines are always drawn as segmented lines

               ``'off'`` lines are never drawn as segmented lines, i.e. the drawing
               method with continuous lines is used
        """
    def paint(self, p, opt, widget) -> None: ...
    def paintGL(self, p, opt, widget) -> None: ...
    def clear(self) -> None: ...
    def mouseShape(self):
        """
        Return a QPainterPath representing the clickable shape of the curve

        """
    def mouseClickEvent(self, ev) -> None: ...

class ROIPlotItem(PlotCurveItem):
    """Plot curve that monitors an ROI and image for changes to automatically replot."""
    roi: Incomplete
    roiData: Incomplete
    roiImg: Incomplete
    axes: Incomplete
    xVals: Incomplete
    def __init__(self, roi, data, img, axes=(0, 1), xVals: Incomplete | None = None, color: Incomplete | None = None) -> None: ...
    def getRoiData(self): ...
    def roiChangedEvent(self) -> None: ...
