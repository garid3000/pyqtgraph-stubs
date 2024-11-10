from .GraphicsObject import GraphicsObject
from _typeshed import Incomplete
import numpy as np

__all__ = ["ScatterPlotItem", "SpotItem"]

class SymbolAtlas:
    """
    Used to efficiently construct a single QPixmap containing all rendered symbols
    for a ScatterPlotItem. This is required for fragment rendering.

    Use example:
        atlas = SymbolAtlas()
        sc1 = atlas[[('o', 5, QPen(..), QBrush(..))]]
        sc2 = atlas[[('t', 10, QPen(..), QBrush(..))]]
        pm = atlas.pixmap

    """
    def __init__(self) -> None: ...
    def __getitem__(self, styles):
        """
        Given a list of tuples, (symbol, size, pen, brush), return a list of coordinates of
        corresponding symbols within the atlas. Note that these coordinates may change if the atlas is rebuilt.
        """
    def __len__(self) -> int: ...
    def devicePixelRatio(self): ...
    def setDevicePixelRatio(self, dpr) -> None: ...
    @property
    def pixmap(self): ...
    @property
    def maxWidth(self): ...
    def rebuild(self, styles: Incomplete | None = None) -> None: ...
    def clear(self) -> None: ...
    def diagnostics(self): ...

class ScatterPlotItem(GraphicsObject):
    """
    Displays a set of x/y points. Instances of this class are created
    automatically as part of PlotDataItem; these rarely need to be instantiated
    directly.

    The size, shape, pen, and fill brush may be set for each point individually
    or for all points.


    ============================  ===============================================
    **Signals:**
    sigPlotChanged(self)          Emitted when the data being plotted has changed
    sigClicked(self, points, ev)  Emitted when points are clicked. Sends a list
                                  of all the points under the mouse pointer.
    sigHovered(self, points, ev)  Emitted when the item is hovered. Sends a list
                                  of all the points under the mouse pointer.
    ============================  ===============================================

    """

    sigClicked: Incomplete
    sigHovered: Incomplete
    sigPlotChanged: Incomplete
    picture: Incomplete
    fragmentAtlas: Incomplete
    data: Incomplete
    bounds: Incomplete
    opts: Incomplete
    def __init__(self, *args, **kargs) -> None:
        """
        Accepts the same arguments as setData()
        """
    def setData(
        self,
        *args: dict[str, tuple[float, float] | str]
        | list[float]
        | np.ndarray[tuple[int], np.dtype[np.float32]],
        **kargs: list[list[float]]
        | np.ndarray[tuple[int, int], np.dtype[np.float32]]
        | bool
        | str
        | list[str],
    ) -> None:
        """
        **Ordered Arguments:**

        * If there is only one unnamed argument, it will be interpreted like the 'spots' argument.
        * If there are two unnamed arguments, they will be interpreted as sequences of x and y values.

        ====================== ===============================================================================================
        **Keyword Arguments:**
        *spots*                Optional list of dicts. Each dict specifies parameters for a single spot:
                               {'pos': (x,y), 'size', 'pen', 'brush', 'symbol'}. This is just an alternate method
                               of passing in data for the corresponding arguments.
        *x*,*y*                1D arrays of x,y values.
        *pos*                  2D structure of x,y pairs (such as Nx2 array or list of tuples)
        *pxMode*               If True, spots are always the same size regardless of scaling, and size is given in px.
                               Otherwise, size is in scene coordinates and the spots scale with the view. To ensure
                               effective caching, QPen and QBrush objects should be reused as much as possible.
                               Default is True
        *symbol*               can be one (or a list) of symbols. For a list of supported symbols, see
                               :func:`~ScatterPlotItem.setSymbol`. QPainterPath is also supported to specify custom symbol
                               shapes. To properly obey the position and size, custom symbols should be centered at (0,0) and
                               width and height of 1.0. Note that it is also possible to 'install' custom shapes by setting
                               ScatterPlotItem.Symbols[key] = shape.
        *pen*                  The pen (or list of pens) to use for drawing spot outlines.
        *brush*                The brush (or list of brushes) to use for filling spots.
        *size*                 The size (or list of sizes) of spots. If *pxMode* is True, this value is in pixels. Otherwise,
                               it is in the item's local coordinate system.
        *data*                 a list of python objects used to uniquely identify each spot.
        *hoverable*            If True, sigHovered is emitted with a list of hovered points, a tool tip is shown containing
                               information about them, and an optional separate style for them is used. Default is False.
        *tip*                  A string-valued function of a spot's (x, y, data) values. Set to None to prevent a tool tip
                               from being shown.
        *hoverSymbol*          A single symbol to use for hovered spots. Set to None to keep symbol unchanged. Default is None.
        *hoverSize*            A single size to use for hovered spots. Set to -1 to keep size unchanged. Default is -1.
        *hoverPen*             A single pen to use for hovered spots. Set to None to keep pen unchanged. Default is None.
        *hoverBrush*           A single brush to use for hovered spots. Set to None to keep brush unchanged. Default is None.
        *useCache*             (bool) By default, generated point graphics items are cached to
                               improve performance. Setting this to False can improve image quality
                               in certain situations.
        *antialias*            Whether to draw symbols with antialiasing. Note that if pxMode is True, symbols are
                               always rendered with antialiasing (since the rendered symbols can be cached, this
                               incurs very little performance cost)
        *compositionMode*      If specified, this sets the composition mode used when drawing the
                               scatter plot (see QPainter::CompositionMode in the Qt documentation).
        *name*                 The name of this item. Names are used for automatically
                               generating LegendItem entries and by some exporters.
        ====================== ===============================================================================================
        """
    def addPoints(self, *args, **kargs) -> None:
        """
        Add new points to the scatter plot.
        Arguments are the same as setData()
        """
    def invalidate(self) -> None: ...
    def getData(self): ...
    def implements(self, interface: Incomplete | None = None): ...
    def name(self): ...
    def setPen(self, *args, **kargs) -> None:
        """Set the pen(s) used to draw the outline around each spot.
        If a list or array is provided, then the pen for each spot will be set separately.
        Otherwise, the arguments are passed to pg.mkPen and used as the default pen for
        all spots which do not have a pen explicitly set."""
    def setBrush(self, *args, **kargs) -> None:
        """Set the brush(es) used to fill the interior of each spot.
        If a list or array is provided, then the brush for each spot will be set separately.
        Otherwise, the arguments are passed to pg.mkBrush and used as the default brush for
        all spots which do not have a brush explicitly set."""
    def setSymbol(
        self,
        symbol,
        update: bool = True,
        dataSet: Incomplete | None = None,
        mask: Incomplete | None = None,
    ) -> None:
        """Set the symbol(s) used to draw each spot.
        If a list or array is provided, then the symbol for each spot will be set separately.
        Otherwise, the argument will be used as the default symbol for
        all spots which do not have a symbol explicitly set.

        **Supported symbols:**

        * 'o'  circle (default)
        * 's'  square
        * 't'  triangle
        * 'd'  diamond
        * '+'  plus
        * 't1' triangle pointing upwards
        * 't2'  triangle pointing right side
        * 't3'  triangle pointing left side
        * 'p'  pentagon
        * 'h'  hexagon
        * 'star'
        * '|' vertical line
        * '_' horizontal line
        * 'x'  cross
        * 'arrow_up'
        * 'arrow_right'
        * 'arrow_down'
        * 'arrow_left'
        * 'crosshair'
        * any QPainterPath to specify custom symbol shapes.

        """
    def setSize(
        self,
        size,
        update: bool = True,
        dataSet: Incomplete | None = None,
        mask: Incomplete | None = None,
    ) -> None:
        """Set the size(s) used to draw each spot.
        If a list or array is provided, then the size for each spot will be set separately.
        Otherwise, the argument will be used as the default size for
        all spots which do not have a size explicitly set."""
    def setPointsVisible(
        self,
        visible,
        update: bool = True,
        dataSet: Incomplete | None = None,
        mask: Incomplete | None = None,
    ) -> None:
        """Set whether or not each spot is visible.
        If a list or array is provided, then the visibility for each spot will be set separately.
        Otherwise, the argument will be used for all spots."""
    def setPointData(
        self, data, dataSet: Incomplete | None = None, mask: Incomplete | None = None
    ) -> None: ...
    def setPxMode(self, mode) -> None: ...
    def updateSpots(self, dataSet: Incomplete | None = None) -> None: ...
    def clear(self) -> None:
        """Remove all spots from the scatter plot"""
    def dataBounds(
        self, ax, frac: float = 1.0, orthoRange: Incomplete | None = None
    ): ...
    def pixelPadding(self): ...
    def boundingRect(self): ...
    def viewTransformChanged(self) -> None: ...
    def setExportMode(self, *args, **kwds) -> None: ...
    def paint(self, p, option, widget) -> None: ...
    def points(self): ...
    def pointsAt(self, pos): ...
    ptsClicked: Incomplete
    def mouseClickEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...

class SpotItem:
    """
    Class referring to individual spots in a scatter plot.
    These can be retrieved by calling ScatterPlotItem.points() or
    by connecting to the ScatterPlotItem's click signals.
    """
    def __init__(self, data, plot, index) -> None: ...
    def data(self):
        """Return the user data associated with this spot."""
    def index(self):
        """Return the index of this point as given in the scatter plot data."""
    def size(self):
        """Return the size of this spot.
        If the spot has no explicit size set, then return the ScatterPlotItem's default size instead."""
    def pos(self): ...
    def viewPos(self): ...
    def setSize(self, size) -> None:
        """Set the size of this spot.
        If the size is set to -1, then the ScatterPlotItem's default size
        will be used instead."""
    def symbol(self):
        """Return the symbol of this spot.
        If the spot has no explicit symbol set, then return the ScatterPlotItem's default symbol instead.
        """
    def setSymbol(self, symbol) -> None:
        """Set the symbol for this spot.
        If the symbol is set to '', then the ScatterPlotItem's default symbol will be used instead."""
    def pen(self): ...
    def setPen(self, *args, **kargs) -> None:
        """Set the outline pen for this spot"""
    def resetPen(self) -> None:
        """Remove the pen set for this spot; the scatter plot's default pen will be used instead."""
    def brush(self): ...
    def setBrush(self, *args, **kargs) -> None:
        """Set the fill brush for this spot"""
    def resetBrush(self) -> None:
        """Remove the brush set for this spot; the scatter plot's default brush will be used instead."""
    def isVisible(self): ...
    def setVisible(self, visible) -> None:
        """Set whether or not this spot is visible."""
    def setData(self, data) -> None:
        """Set the user-data associated with this spot"""
    def updateItem(self) -> None: ...
