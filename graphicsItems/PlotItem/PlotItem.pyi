from ..PlotDataItem import PlotDataItem
#from ..ScatterPlotItem import ScatterPlotItem
from ..GraphicsWidget import GraphicsWidget
from ..GraphicsItem import GraphicsItem
from ..LegendItem import LegendItem
from _typeshed import Incomplete
from ...Qt import QtGui
import numpy as np
from numpy.typing import NDArray
from ..ViewBox import ViewBox
from ..AxisItem import AxisItem

# from ..Qt import QtCore

__all__ = ['PlotItem']

class PlotItem(GraphicsWidget):
    """GraphicsWidget implementing a standard 2D plotting area with axes.

    **Bases:** :class:`GraphicsWidget <pyqtgraph.GraphicsWidget>`

    This class provides the ViewBox-plus-axes that appear when using
    :func:`pg.plot() <pyqtgraph.plot>`, :class:`PlotWidget <pyqtgraph.PlotWidget>`,
    and :func:`GraphicsLayout.addPlot() <pyqtgraph.GraphicsLayout.addPlot>`.

    It's main functionality is:

      - Manage placement of ViewBox, AxisItems, and LabelItems
      - Create and manage a list of PlotDataItems displayed inside the ViewBox
      - Implement a context menu with commonly used display and analysis options

    Use :func:`plot() <pyqtgraph.PlotItem.plot>` to create a new PlotDataItem and
    add it to the view. Use :func:`addItem() <pyqtgraph.PlotItem.addItem>` to
    add any QGraphicsItem to the view.

    This class wraps several methods from its internal ViewBox:
      - :func:`setXRange <pyqtgraph.ViewBox.setXRange>`
      - :func:`setYRange <pyqtgraph.ViewBox.setYRange>`
      - :func:`setRange <pyqtgraph.ViewBox.setRange>`
      - :func:`autoRange <pyqtgraph.ViewBox.autoRange>`
      - :func:`setDefaultPadding <pyqtgraph.ViewBox.setDefaultPadding>`
      - :func:`setXLink <pyqtgraph.ViewBox.setXLink>`
      - :func:`setYLink <pyqtgraph.ViewBox.setYLink>`
      - :func:`setAutoPan <pyqtgraph.ViewBox.setAutoPan>`
      - :func:`setAutoVisible <pyqtgraph.ViewBox.setAutoVisible>`
      - :func:`setLimits <pyqtgraph.ViewBox.setLimits>`
      - :func:`viewRect <pyqtgraph.ViewBox.viewRect>`
      - :func:`viewRange <pyqtgraph.ViewBox.viewRange>`
      - :func:`setMouseEnabled <pyqtgraph.ViewBox.setMouseEnabled>`
      - :func:`enableAutoRange <pyqtgraph.ViewBox.enableAutoRange>`
      - :func:`disableAutoRange <pyqtgraph.ViewBox.disableAutoRange>`
      - :func:`setAspectLocked <pyqtgraph.ViewBox.setAspectLocked>`
      - :func:`invertY <pyqtgraph.ViewBox.invertY>`
      - :func:`invertX <pyqtgraph.ViewBox.invertX>`
      - :func:`register <pyqtgraph.ViewBox.register>`
      - :func:`unregister <pyqtgraph.ViewBox.unregister>`

    The ViewBox itself can be accessed by calling :func:`getViewBox() <pyqtgraph.PlotItem.getViewBox>`

    ==================== =======================================================================
    **Signals:**
    sigYRangeChanged     wrapped from :class:`ViewBox <pyqtgraph.ViewBox>`
    sigXRangeChanged     wrapped from :class:`ViewBox <pyqtgraph.ViewBox>`
    sigRangeChanged      wrapped from :class:`ViewBox <pyqtgraph.ViewBox>`
    ==================== =======================================================================
    """
    sigRangeChanged: Incomplete
    sigYRangeChanged: Incomplete
    sigXRangeChanged: Incomplete
    lastFileDir: Incomplete
    autoBtn: Incomplete
    buttonsHidden: bool
    mouseHovering: bool
    layout: Incomplete
    vb: Incomplete
    alpha: float
    autoAlpha: bool
    spectrumMode: bool
    legend: Incomplete
    axes: Incomplete
    titleLabel: Incomplete
    items: Incomplete
    curves: Incomplete
    itemMeta: Incomplete
    dataItems: Incomplete
    paramList: Incomplete
    avgCurves: Incomplete
    avgPen: Incomplete
    avgShadowPen: Incomplete
    ctrl: Incomplete
    ctrlMenu: Incomplete
    stateGroup: Incomplete
    fileDialog: Incomplete
    def __init__(self, parent: Incomplete | None = None, name: Incomplete | None = None, labels: Incomplete | None = None, title: Incomplete | None = None, viewBox: Incomplete | None = None, axisItems: Incomplete | None = None, enableMenu: bool = True, **kargs) -> None:
        """
        Create a new PlotItem. All arguments are optional.
        Any extra keyword arguments are passed to :func:`PlotItem.plot() <pyqtgraph.PlotItem.plot>`.

        ==============  ==========================================================================================
        **Arguments:**
        *title*         Title to display at the top of the item. Html is allowed.
        *labels*        A dictionary specifying the axis labels to display::

                            {'left': (args), 'bottom': (args), ...}

                        The name of each axis and the corresponding arguments are passed to
                        :func:`PlotItem.setLabel() <pyqtgraph.PlotItem.setLabel>`
                        Optionally, PlotItem my also be initialized with the keyword arguments left,
                        right, top, or bottom to achieve the same effect.
        *name*          Registers a name for this view so that others may link to it
        *viewBox*       If specified, the PlotItem will be constructed with this as its ViewBox.
        *axisItems*     Optional dictionary instructing the PlotItem to use pre-constructed items
                        for its axes. The dict keys must be axis names ('left', 'bottom', 'right', 'top')
                        and the values must be instances of AxisItem (or at least compatible with AxisItem).
        ==============  ==========================================================================================
        """
    def implements(self, interface: Incomplete | None = None): ...
    def getViewBox(self) -> ViewBox:
        """Return the :class:`ViewBox <pyqtgraph.ViewBox>` contained within."""
    def setAxisItems(self, axisItems: Incomplete | None = None) -> None:
        """
        Place axis items as given by `axisItems`. Initializes non-existing axis items.

        ==============  ==========================================================================================
        **Arguments:**
        *axisItems*     Optional dictionary instructing the PlotItem to use pre-constructed items
                        for its axes. The dict keys must be axis names ('left', 'bottom', 'right', 'top')
                        and the values must be instances of AxisItem (or at least compatible with AxisItem).
        ==============  ==========================================================================================
        """
    def setLogMode(self, x: Incomplete | None = None, y: Incomplete | None = None) -> None:
        """
        Set log scaling for `x` and/or `y` axes.
        This informs PlotDataItems to transform logarithmically and switches
        the axes to use log ticking.

        Note that *no other items* in the scene will be affected by
        this; there is (currently) no generic way to redisplay a GraphicsItem
        with log coordinates.

        """
    def showGrid(self, x: Incomplete | None = None, y: Incomplete | None = None, alpha: Incomplete | None = None) -> None:
        """
        Show or hide the grid for either axis.

        ==============  =====================================
        **Arguments:**
        x               (bool) Whether to show the X grid
        y               (bool) Whether to show the Y grid
        alpha           (0.0-1.0) Opacity of the grid
        ==============  =====================================
        """
    def close(self) -> None: ...
    def registerPlot(self, name) -> None: ...
    def updateGrid(self, *args) -> None: ...
    def viewGeometry(self):
        """Return the screen geometry of the viewbox"""
    def avgToggled(self, b) -> None: ...
    def avgParamListClicked(self, item) -> None: ...
    def recomputeAverages(self) -> None: ...
    def addAvgCurve(self, curve) -> None: ...
    def autoBtnClicked(self) -> None: ...
    def viewStateChanged(self) -> None: ...
    #def addItem(self, item: PlotDataItem | ScatterPlotItem, *args : str|float, **kargs: str|float) -> None:
    def addItem(self, item: GraphicsItem, *args : str|float, **kargs: str|float) -> None:
        """
        Add a graphics item to the view box.
        If the item has plot data (:class:`PlotDataItem <pyqtgraph.PlotDataItem>` ,
        :class:`~pyqtgraph.PlotCurveItem` , :class:`~pyqtgraph.ScatterPlotItem` ),
        it may be included in analysis performed by the PlotItem.
        """
    def listDataItems(self):
        """Return a list of all data items (:class:`PlotDataItem <pyqtgraph.PlotDataItem>`,
        :class:`~pyqtgraph.PlotCurveItem` , :class:`~pyqtgraph.ScatterPlotItem` , etc)
        contained in this PlotItem."""
    def addLine(self, x: Incomplete | None = None, y: Incomplete | None = None, z: Incomplete | None = None, **kwds):
        """
        Create an :class:`~pyqtgraph.InfiniteLine` and add to the plot.

        If `x` is specified,
        the line will be vertical. If `y` is specified, the line will be
        horizontal. All extra keyword arguments are passed to
        :func:`InfiniteLine.__init__() <pyqtgraph.InfiniteLine.__init__>`.
        Returns the item created.
        """
    def removeItem(self, item) -> None:
        """
        Remove an item from the PlotItem's :class:`~pyqtgraph.ViewBox`.
        """
    def clear(self) -> None:
        """
        Remove all items from the PlotItem's :class:`~pyqtgraph.ViewBox`.
        """
    def clearPlots(self) -> None: ...
    #def plot(self, *args: str|bool|int|None, **kargs: str|bool|int|None|tuple[int, int, int]|QtGui.QPen) -> PlotDataItem:
    #def plot(self, *args: list[float] | NDArray[np.int64] | NDArray[np.uint8]| NDArray[np.float64], **kargs: list[float] | NDArray[np.int64] | NDArray[np.uint8]| NDArray[np.float64]) -> PlotDataItem:
    def plot(self, *args: list[float] | NDArray[np.int64] | NDArray[np.uint8]| NDArray[np.float64], **kargs: str|bool|int|None|tuple[int, int, int]|QtGui.QPen| NDArray[np.float32 | np.float64]) -> PlotDataItem:
        """
        Add and return a new plot.
        See :func:`PlotDataItem.__init__ <pyqtgraph.PlotDataItem.__init__>` for data arguments

        **Additional allowed arguments**

        ========= =================================================================
        `clear`   clears all plots before displaying new data
        `params`  sets meta-parameters to associate with this data
        ========= =================================================================
        """
    def addLegend(self, offset:tuple[float,float]|list[float]=(30, 30), **kwargs: None|str|float|bool) -> LegendItem:
        """
        Create a new :class:`~pyqtgraph.LegendItem` and anchor it over the internal
        :class:`~pyqtgraph.ViewBox`. Plots added after this will be automatically
        displayed in the legend if they are created with a 'name' argument.

        If a :class:`~pyqtgraph.LegendItem` has already been created using this method,
        that item will be returned rather than creating a new one.

        Accepts the same arguments as :func:`~pyqtgraph.LegendItem.__init__`.
        """
    def addColorBar(self, image, **kargs):
        """
        Adds a color bar linked to the ImageItem specified by `image`.
        AAdditional parameters will be passed to the `pyqtgraph.ColorBarItem`.

        A call like `plot.addColorBar(img, colorMap='viridis')` is a convenient
        method to assign and show a color map.
        """
    def multiDataPlot(self, *, x: Incomplete | None = None, y: Incomplete | None = None, constKwargs: Incomplete | None = None, **kwargs):
        """
        Allow plotting multiple curves on the same plot, changing some kwargs
        per curve.

        Parameters
        ----------
        x, y: array_like
            can be in the following formats:
              - {x or y} = [n1, n2, n3, ...]: The named argument iterates through
                ``n`` curves, while the unspecified argument is range(len(n)) for
                each curve.
              - x, [y1, y2, y3, ...]
              - [x1, x2, x3, ...], [y1, y2, y3, ...]
              - [x1, x2, x3, ...], y

              where ``x_n`` and ``y_n`` are ``ndarray`` data for each curve. Since
              ``x`` and ``y`` values are matched using ``zip``, unequal lengths mean
              the longer array will be truncated. Note that 2D matrices for either x
              or y are considered lists of curve
              data.
        constKwargs: dict, optional
            A dict of {str: value} passed to each curve during ``plot()``.
        kwargs: dict, optional
            A dict of {str: iterable} where the str is the name of a kwarg and the
            iterable is a list of values, one for each plotted curve.
        """
    def scatterPlot(self, *args, **kargs): ...
    def replot(self) -> None: ...
    def updateParamList(self) -> None: ...
    def writeSvg(self, fileName: Incomplete | None = None) -> None: ...
    def writeImage(self, fileName: Incomplete | None = None) -> None: ...
    def writeCsv(self, fileName: Incomplete | None = None) -> None: ...
    def saveState(self): ...
    def restoreState(self, state) -> None: ...
    def widgetGroupInterface(self): ...
    def updateSpectrumMode(self, b: Incomplete | None = None) -> None: ...
    def updateLogMode(self) -> None: ...
    def updateDerivativeMode(self) -> None: ...
    def updatePhasemapMode(self) -> None: ...
    def setDownsampling(self, ds: Incomplete | None = None, auto: Incomplete | None = None, mode: Incomplete | None = None) -> None:
        """
        Changes the default downsampling mode for all :class:`~pyqtgraph.PlotDataItem` managed by this plot.

        =============== ====================================================================
        **Arguments:**
        ds              (int) Reduce visible plot samples by this factor, or

                        (bool) To enable/disable downsampling without changing the value.

        auto            (bool) If `True`, automatically pick ``ds`` based on visible range

        mode            'subsample': Downsample by taking the first of N samples. This
                        method is fastest but least accurate.

                        'mean': Downsample by taking the mean of N samples.

                        'peak': Downsample by drawing a saw wave that follows the min and
                        max of the original data. This method produces the best visual
                        representation of the data but is slower.
        =============== ====================================================================
        """
    def updateDownsampling(self) -> None: ...
    def downsampleMode(self): ...
    def setClipToView(self, clip) -> None:
        """Set the default clip-to-view mode for all :class:`~pyqtgraph.PlotDataItem` s managed by this plot.
        If *clip* is `True`, then PlotDataItems will attempt to draw only points within the visible
        range of the ViewBox."""
    def clipToViewMode(self): ...
    def updateDecimation(self) -> None:
        """
        Reduce or increase number of visible curves according to value set by the `Max Traces` spinner,
        if `Max Traces` is checked in the context menu. Destroy curves that are not visible if
        `forget traces` is checked. In most cases, this function is called automaticaly when the
        `Max Traces` GUI elements are triggered. It is also alled when the state of PlotItem is updated,
        its state is restored, or new items added added/removed.

        This can cause an unexpected or conflicting state of curve visibility (or destruction) if curve
        visibilities are controlled externally. In the case of external control it is advised to disable
        the `Max Traces` checkbox (or context menu) to prevent unexpected curve state changes.
        """
    def updateAlpha(self, *args) -> None: ...
    def alphaState(self): ...
    def pointMode(self): ...
    def resizeEvent(self, ev) -> None: ...
    def getMenu(self): ...
    def getContextMenus(self, event): ...
    def setMenuEnabled(self, enableMenu: bool = True, enableViewBoxMenu: str = 'same') -> None:
        """
        Enable or disable the context menu for this PlotItem.
        By default, the ViewBox's context menu will also be affected.
        (use ``enableViewBoxMenu=None`` to leave the ViewBox unchanged)
        """
    def menuEnabled(self): ...
    def setContextMenuActionVisible(self, name: str, visible: bool) -> None:
        """
        Changes the context menu action visibility

        Parameters
        ----------
        name: str
            Action name
            must be one of 'Transforms', 'Downsample', 'Average','Alpha', 'Grid', or 'Points'
        visible: bool
            Determines if action will be display
            True action is visible
            False action is invisible.
        """
    def hoverEvent(self, ev) -> None: ...
    def getLabel(self, key) -> None: ...
    def getScale(self, key): ...
    def getAxis(self, name: str) -> AxisItem:
        """Return the specified AxisItem.
        *name* should be 'left', 'bottom', 'top', or 'right'."""
    def setLabel(self, axis: str, text: str | None = None, units: str | None = None, unitPrefix: str | None = None, **args: str) -> None:
        """
        Sets the label for an axis. Basic HTML formatting is allowed.

        ==============  =================================================================
        **Arguments:**
        axis            must be one of 'left', 'bottom', 'right', or 'top'
        text            text to display along the axis. HTML allowed.
        units           units to display after the title. If units are given,
                        then an SI prefix will be automatically appended
                        and the axis values will be scaled accordingly.
                        (ie, use 'V' instead of 'mV'; 'm' will be added automatically)
        ==============  =================================================================
        """
    def setLabels(self, **kwds) -> None:
        """
        Convenience function allowing multiple labels and/or title to be set in one call.
        Keyword arguments can be 'title', 'left', 'bottom', 'right', or 'top'.
        Values may be strings or a tuple of arguments to pass to :func:`setLabel`.
        """
    def showLabel(self, axis, show: bool = True) -> None:
        """
        Show or hide one of the plot's axis labels (the axis itself will be unaffected).
        axis must be one of 'left', 'bottom', 'right', or 'top'
        """
    def setTitle(self, title: str | None = None, **args: str|bool|None) -> None:
        """
        Set the title of the plot. Basic HTML formatting is allowed.
        If title is None, then the title will be hidden.
        """
    def showAxis(self, axis: str, show: bool = True) -> None:
        """
        Show or hide one of the plot's axes.
        axis must be one of 'left', 'bottom', 'right', or 'top'
        """
    def hideAxis(self, axis) -> None:
        """Hide one of the PlotItem's axes. ('left', 'bottom', 'right', or 'top')"""
    def showAxes(self, selection, showValues: bool = True, size: bool = False) -> None:
        """
        Convenience method for quickly configuring axis settings.

        Parameters
        ----------
        selection: bool or tuple of bool
            Determines which AxisItems will be displayed.
            If in tuple form, order is (left, top, right, bottom)
            A single boolean value will set all axes,
            so that ``showAxes(True)`` configures the axes to draw a frame.
        showValues: bool or tuple of bool, optional
            Determines if values will be displayed for the ticks of each axis.
            True value shows values for left and bottom axis (default).
            False shows no values.
            If in tuple form, order is (left, top, right, bottom)
            None leaves settings unchanged.
            If not specified, left and bottom axes will be drawn with values.
        size: float or tuple of float, optional
            Reserves as fixed amount of space (width for vertical axis, height for horizontal axis)
            for each axis where tick values are enabled. If only a single float value is given, it
            will be applied for both width and height. If `None` is given instead of a float value,
            the axis reverts to automatic allocation of space.
            If in tuple form, order is (width, height)
        """
    def hideButtons(self) -> None:
        """Causes auto-scale button ('A' in lower-left corner) to be hidden for this PlotItem"""
    def showButtons(self) -> None:
        """Causes auto-scale button ('A' in lower-left corner) to be visible for this PlotItem"""
    def updateButtons(self) -> None: ...
    def setExportMode(self, export, opts: Incomplete | None = None) -> None: ...
