from numpy._typing import NDArray
import numpy as np
from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete
from ..Qt import QtGui # QtCore #,QT_LIB,

__all__ = ['PlotDataItem']

class PlotDataset:
    """
    :orphan:
    .. warning:: This class is intended for internal use. The interface may change without warning.

    Holds collected information for a plotable dataset.
    Numpy arrays containing x and y coordinates are available as ``dataset.x`` and ``dataset.y``.

    After a search has been performed, typically during a call to :func:`dataRect() <pyqtgraph.PlotDataset.dataRect>`,
    ``dataset.containsNonfinite`` is `True` if any coordinate values are nonfinite (e.g. NaN or inf) or `False` if all
    values are finite. If no search has been performed yet, ``dataset.containsNonfinite`` is `None`.

    For internal use in :class:`PlotDataItem <pyqtgraph.PlotDataItem>`, this class should not be instantiated when no data is available.
    """
    x: Incomplete
    y: Incomplete
    xAllFinite: Incomplete
    yAllFinite: Incomplete
    def __init__(self, x, y, xAllFinite: Incomplete | None = None, yAllFinite: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        x: array
            x coordinates of data points.
        y: array
            y coordinates of data points.
        """
    @property
    def containsNonfinite(self): ...
    def dataRect(self):
        """
        Returns a bounding rectangle (as :class:`QtCore.QRectF`) for the finite subset of data.
        If there is an active mapping function, such as logarithmic scaling, then bounds represent the mapped data.
        Will return `None` if there is no data or if all values (`x` or `y`) are NaN.
        """
    def applyLogMapping(self, logMode) -> None:
        """
        Applies a logarithmic mapping transformation (base 10) if requested for the respective axis.
        This replaces the internal data. Values of ``-inf`` resulting from zeros in the original dataset are
        replaced by ``np.nan``.

        Parameters
        ----------
        logmode: tuple or list of two bool
            A `True` value requests log-scale mapping for the x and y axis (in this order).
        """

class PlotDataItem(GraphicsObject):
    """
    **Bases:** :class:`GraphicsObject <pyqtgraph.GraphicsObject>`

    :class:`PlotDataItem` provides a unified interface for displaying plot curves, scatter plots, or both.
    It also contains methods to transform or decimate the original data before it is displayed.

    As pyqtgraph's standard plotting object, ``plot()`` methods such as :func:`pyqtgraph.plot` and
    :func:`PlotItem.plot() <pyqtgraph.PlotItem.plot>` create instances of :class:`PlotDataItem`.

    While it is possible to use :class:`PlotCurveItem <pyqtgraph.PlotCurveItem>` or
    :class:`ScatterPlotItem <pyqtgraph.ScatterPlotItem>` individually, this is recommended only
    where performance is critical and the limited functionality of these classes is sufficient.

    ==================================  ==============================================
    **Signals:**
    sigPlotChanged(self)                Emitted when the data in this item is updated.
    sigClicked(self, ev)                Emitted when the item is clicked.
    sigPointsClicked(self, points, ev)  Emitted when a plot point is clicked
                                        Sends the list of points under the mouse.
    sigPointsHovered(self, points, ev)  Emitted when a plot point is hovered over.
                                        Sends the list of points under the mouse.
    ==================================  ==============================================
    """
    sigPlotChanged: Incomplete
    sigClicked: Incomplete
    sigPointsClicked: Incomplete
    sigPointsHovered: Incomplete
    curve: Incomplete
    scatter: Incomplete
    opts: Incomplete
    def __init__(self, *args: str | list[float] | NDArray[np.int64] | NDArray[np.uint8]| NDArray[np.float64], **kargs: str | list[float] | NDArray[np.int64] | NDArray[np.uint8] | NDArray[np.float64]| QtGui.QPen ) -> None:
        """
        There are many different ways to create a PlotDataItem.

        **Data initialization arguments:** (x,y data only)

            ========================== =========================================
            PlotDataItem(x, y)         x, y: array_like coordinate values
            PlotDataItem(y)            y values only -- x will be
                                       automatically set to ``range(len(y))``
            PlotDataItem(x=x, y=y)     x and y given by keyword arguments
            PlotDataItem(ndarray(N,2)) single numpy array with shape (N, 2),
                                       where ``x=data[:,0]`` and ``y=data[:,1]``
            ========================== =========================================

        **Data initialization arguments:** (x,y data AND may include spot style)

            ============================ ===============================================
            PlotDataItem(recarray)       numpy record array with ``dtype=[('x', float),
                                         ('y', float), ...]``
            PlotDataItem(list-of-dicts)  ``[{'x': x, 'y': y, ...},   ...]``
            PlotDataItem(dict-of-lists)  ``{'x': [...], 'y': [...],  ...}``
            ============================ ===============================================

        **Line style keyword arguments:**

            ============ ==============================================================================
            connect      Specifies how / whether vertexes should be connected. See below for details.
            pen          Pen to use for drawing the lines between points.
                         Default is solid grey, 1px width. Use None to disable line drawing.
                         May be a ``QPen`` or any single argument accepted by
                         :func:`mkPen() <pyqtgraph.mkPen>`
            shadowPen    Pen for secondary line to draw behind the primary line. Disabled by default.
                         May be a ``QPen`` or any single argument accepted by
                         :func:`mkPen() <pyqtgraph.mkPen>`
            fillLevel    If specified, the area between the curve and fillLevel is filled.
            fillOutline  (bool) If True, an outline surrounding the *fillLevel* area is drawn.
            fillBrush    Fill to use in the *fillLevel* area. May be any single argument accepted by
                         :func:`mkBrush() <pyqtgraph.mkBrush>`
            stepMode     (str or None) If specified and not None, a stepped curve is drawn.
                         For 'left' the specified points each describe the left edge of a step.
                         For 'right', they describe the right edge.
                         For 'center', the x coordinates specify the location of the step boundaries.
                         This mode is commonly used for histograms. Note that it requires an additional
                         x value, such that len(x) = len(y) + 1 .

            ============ ==============================================================================

        ``connect`` supports the following arguments:

        - 'all' connects all points.
        - 'pairs' generates lines between every other point.
        - 'finite' creates a break when a nonfinite points is encountered.
        - If an ndarray is passed, it should contain `N` int32 values of 0 or 1.
          Values of 1 indicate that the respective point will be connected to the next.
        - In the default 'auto' mode, PlotDataItem will normally use 'all', but if any
          nonfinite data points are detected, it will automatically switch to 'finite'.

        See :func:`arrayToQPath() <pyqtgraph.arrayToQPath>` for more details.

        **Point style keyword arguments:**  (see :func:`ScatterPlotItem.setData() <pyqtgraph.ScatterPlotItem.setData>` for more information)

            ============ ======================================================
            symbol       Symbol to use for drawing points, or a list of symbols
                         for each. The default is no symbol.
            symbolPen    Outline pen for drawing points, or a list of pens, one
                         per point. May be any single argument accepted by
                         :func:`mkPen() <pyqtgraph.mkPen>`.
            symbolBrush  Brush for filling points, or a list of brushes, one
                         per point. May be any single argument accepted by
                         :func:`mkBrush() <pyqtgraph.mkBrush>`.
            symbolSize   Diameter of symbols, or list of diameters.
            pxMode       (bool) If True, then symbolSize is specified in
                         pixels. If False, then symbolSize is
                         specified in data coordinates.
            ============ ======================================================

        Any symbol recognized by :class:`ScatterPlotItem <pyqtgraph.ScatterPlotItem>` can be specified,
        including 'o' (circle), 's' (square), 't', 't1', 't2', 't3' (triangles of different orientation),
        'd' (diamond), '+' (plus sign), 'x' (x mark), 'p' (pentagon), 'h' (hexagon) and 'star'.

        Symbols can also be directly given in the form of a :class:`QtGui.QPainterPath` instance.

        **Optimization keyword arguments:**

            ================= =======================================================================
            useCache          (bool) By default, generated point graphics items are cached to
                              improve performance. Setting this to False can improve image quality
                              in certain situations.
            antialias         (bool) By default, antialiasing is disabled to improve performance.
                              Note that in some cases (in particular, when ``pxMode=True``), points
                              will be rendered antialiased even if this is set to `False`.
            downsample        (int) Reduce the number of samples displayed by the given factor.
            downsampleMethod  'subsample': Downsample by taking the first of N samples.
                              This method is fastest and least accurate.
                              'mean': Downsample by taking the mean of N samples.
                              'peak': Downsample by drawing a saw wave that follows the min
                              and max of the original data. This method produces the best
                              visual representation of the data but is slower.
            autoDownsample    (bool) If `True`, resample the data before plotting to avoid plotting
                              multiple line segments per pixel. This can improve performance when
                              viewing very high-density data, but increases the initial overhead
                              and memory usage.
            clipToView        (bool) If `True`, only data visible within the X range of the containing
                              :class:`ViewBox` is plotted. This can improve performance when plotting
                              very large data sets where only a fraction of the data is visible
                              at any time.
            dynamicRangeLimit (float or `None`) Limit off-screen y positions of data points.
                              `None` disables the limiting. This can increase performance but may
                              cause plots to disappear at high levels of magnification.
                              The default of 1e6 limits data to approximately 1,000,000 times the
                              :class:`ViewBox` height.
            dynamicRangeHyst  (float) Permits changes in vertical zoom up to the given hysteresis
                              factor (the default is 3.0) before the limit calculation is repeated.
            skipFiniteCheck   (bool, default `False`) Optimization flag that can speed up plotting by not
                              checking and compensating for NaN values.  If set to `True`, and NaN
                              values exist, unpredictable behavior will occur. The data may not be
                              displayed or the plot may take a significant performance hit.

                              In the default 'auto' connect mode, `PlotDataItem` will automatically
                              override this setting.
            ================= =======================================================================

        **Meta-info keyword arguments:**

            ==========   ================================================
            name         (string) Name of item for use in the plot legend
            ==========   ================================================

        **Notes on performance:**

        Plotting lines with the default single-pixel width is the fastest available option. For such lines,
        translucent colors (`alpha` < 1) do not result in a significant slowdown.

        Wider lines increase the complexity due to the overlap of individual line segments. Translucent colors
        require merging the entire plot into a single entity before the alpha value can be applied. For plots with more
        than a few hundred points, this can result in excessive slowdown.

        Since version 0.12.4, this slowdown is automatically avoided by an algorithm that draws line segments
        separately for fully opaque lines. Setting `alpha` < 1 reverts to the previous, slower drawing method.

        For lines with a width of more than 4 pixels, :func:`pyqtgraph.mkPen() <pyqtgraph.mkPen>` will automatically
        create a ``QPen`` with `Qt.PenCapStyle.RoundCap` to ensure a smooth connection of line segments. This incurs a
        small performance penalty.

        """
    @property
    def xData(self): ...
    @property
    def yData(self): ...
    def implements(self, interface: Incomplete | None = None): ...
    def name(self):
        """ Returns the name that represents this item in the legend. """
    def setCurveClickable(self, state, width: Incomplete | None = None) -> None:
        """ ``state=True`` sets the curve to be clickable, with a tolerance margin represented by `width`. """
    def curveClickable(self):
        """ Returns `True` if the curve is set to be clickable. """
    def boundingRect(self): ...
    def setPos(self, x, y) -> None: ...
    def setAlpha(self, alpha, auto) -> None: ...
    def setFftMode(self, state) -> None:
        """
        ``state = True`` enables mapping the data by a fast Fourier transform.
        If the `x` values are not equidistant, the data set is resampled at
        equal intervals.
        """
    def setLogMode(self, xState, yState) -> None:
        """
        When log mode is enabled for the respective axis by setting ``xState`` or
        ``yState`` to `True`, a mapping according to ``mapped = np.log10( value )``
        is applied to the data. For negative or zero values, this results in a
        `NaN` value.
        """
    def setDerivativeMode(self, state) -> None:
        """
        ``state = True`` enables derivative mode, where a mapping according to
        ``y_mapped = dy / dx`` is applied, with `dx` and `dy` representing the
        differences between adjacent `x` and `y` values.
        """
    def setPhasemapMode(self, state) -> None:
        """
        ``state = True`` enables phase map mode, where a mapping
        according to ``x_mappped = y`` and ``y_mapped = dy / dx``
        is applied, plotting the numerical derivative of the data over the
        original `y` values.
        """
    def setPen(self, *args, **kargs) -> None:
        """
        Sets the pen used to draw lines between points.
        The argument can be a :class:`QtGui.QPen` or any combination of arguments accepted by
        :func:`pyqtgraph.mkPen() <pyqtgraph.mkPen>`.
        """
    def setShadowPen(self, *args, **kargs) -> None:
        """
        Sets the shadow pen used to draw lines between points (this is for enhancing contrast or
        emphasizing data). This line is drawn behind the primary pen and should generally be assigned
        greater width than the primary pen.
        The argument can be a :class:`QtGui.QPen` or any combination of arguments accepted by
        :func:`pyqtgraph.mkPen() <pyqtgraph.mkPen>`.
        """
    def setFillBrush(self, *args, **kargs) -> None:
        """
        Sets the :class:`QtGui.QBrush` used to fill the area under the curve.
        See :func:`mkBrush() <pyqtgraph.mkBrush>`) for arguments.
        """
    def setBrush(self, *args, **kargs):
        """
        See :func:`~pyqtgraph.PlotDataItem.setFillBrush`
        """
    def setFillLevel(self, level) -> None:
        """
        Enables filling the area under the curve towards the value specified by
        `level`. `None` disables the filling.
        """
    def setSymbol(self, symbol) -> None:
        """ `symbol` can be any string recognized by
        :class:`ScatterPlotItem <pyqtgraph.ScatterPlotItem>` or a list that
        specifies a symbol for each point.
        """
    def setSymbolPen(self, *args, **kargs) -> None:
        """
        Sets the :class:`QtGui.QPen` used to draw symbol outlines.
        See :func:`mkPen() <pyqtgraph.mkPen>`) for arguments.
        """
    def setSymbolBrush(self, *args, **kargs) -> None:
        """
        Sets the :class:`QtGui.QBrush` used to fill symbols.
        See :func:`mkBrush() <pyqtgraph.mkBrush>`) for arguments.
        """
    def setSymbolSize(self, size) -> None:
        """
        Sets the symbol size.
        """
    def setDownsampling(self, ds: Incomplete | None = None, auto: Incomplete | None = None, method: Incomplete | None = None) -> None:
        """
        Sets the downsampling mode of this item. Downsampling reduces the number
        of samples drawn to increase performance.

        ==============  =================================================================
        **Arguments:**
        ds              (int) Reduce visible plot samples by this factor. To disable,
                        set ds=1.
        auto            (bool) If True, automatically pick *ds* based on visible range
        mode            'subsample': Downsample by taking the first of N samples.
                        This method is fastest and least accurate.
                        'mean': Downsample by taking the mean of N samples.
                        'peak': Downsample by drawing a saw wave that follows the min
                        and max of the original data. This method produces the best
                        visual representation of the data but is slower.
        ==============  =================================================================
        """
    def setClipToView(self, state) -> None:
        """
        ``state=True`` enables clipping the displayed data set to the
        visible x-axis range.
        """
    def setDynamicRangeLimit(self, limit: float = 1000000.0, hysteresis: float = 3.0) -> None:
        """
        Limit the off-screen positions of data points at large magnification
        This avoids errors with plots not displaying because their visibility is incorrectly determined.
        The default setting repositions far-off points to be within ±10^6 times the viewport height.

        =============== ================================================================
        **Arguments:**
        limit           (float or None) Any data outside the range of limit * hysteresis
                        will be constrained to the limit value limit.
                        All values are relative to the viewport height.
                        'None' disables the check for a minimal increase in performance.
                        Default is 1E+06.

        hysteresis      (float) Hysteresis factor that controls how much change
                        in zoom level (vertical height) is allowed before recalculating
                        Default is 3.0
        =============== ================================================================
        """
    def setSkipFiniteCheck(self, skipFiniteCheck) -> None:
        """
        When it is known that the plot data passed to ``PlotDataItem`` contains only finite numerical values,
        the ``skipFiniteCheck`` property can help speed up plotting. If this flag is set and the data contains
        any non-finite values (such as `NaN` or `Inf`), unpredictable behavior will occur. The data might not
        be plotted, or there migth be significant performance impact.

        In the default 'auto' connect mode, ``PlotDataItem`` will apply this setting automatically.
        """
    def setData(self, *args: list[float] | NDArray[np.int64] | NDArray[np.uint8]| NDArray[np.float64], **kargs: list[float] | NDArray[np.int64] | NDArray[np.uint8]| NDArray[np.float64]) -> None:
        """
        Clear any data displayed by this item and display new data.
        See :func:`__init__() <pyqtgraph.PlotDataItem.__init__>` for details; it accepts the same arguments.
        """
    def updateItems(self, styleUpdate: bool = True) -> None: ...
    def getOriginalDataset(self):
        """
            Returns the original, unmapped data as the tuple (`xData`, `yData`).
            """
    def getData(self):
        """
        Returns the displayed data as the tuple (`xData`, `yData`) after mapping and data reduction.
        """
    def dataRect(self):
        """
        Returns a bounding rectangle (as :class:`QtCore.QRectF`) for the full set of data.
        Will return `None` if there is no data or if all values (x or y) are NaN.
        """
    def dataBounds(self, ax, frac: float = 1.0, orthoRange: Incomplete | None = None):
        """
        Returns the range occupied by the data (along a specific axis) in this item.
        This method is called by :class:`ViewBox` when auto-scaling.

        =============== ====================================================================
        **Arguments:**
        ax              (0 or 1) the axis for which to return this item's data range
        frac            (float 0.0-1.0) Specifies what fraction of the total data
                        range to return. By default, the entire range is returned.
                        This allows the :class:`ViewBox` to ignore large spikes in the data
                        when auto-scaling.
        orthoRange      ([min,max] or None) Specifies that only the data within the
                        given range (orthogonal to *ax*) should me measured when
                        returning the data range. (For example, a ViewBox might ask
                        what is the y-range of all data with x-values between min
                        and max)
        =============== ====================================================================
        """
    def pixelPadding(self):
        """
        Returns the size in pixels that this item may draw beyond the values returned by dataBounds().
        This method is called by :class:`ViewBox` when auto-scaling.
        """
    def clear(self) -> None: ...
    def appendData(self, *args, **kargs) -> None: ...
    def curveClicked(self, curve, ev) -> None: ...
    def scatterClicked(self, plt, points, ev) -> None: ...
    def scatterHovered(self, plt, points, ev) -> None: ...
    def viewRangeChanged(self, vb: Incomplete | None = None, ranges: Incomplete | None = None, changed: Incomplete | None = None) -> None: ...
