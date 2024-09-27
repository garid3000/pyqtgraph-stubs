from .PlotItem import PlotItem
from _typeshed import Incomplete

__all__ = ['ColorBarItem']

class ColorBarItem(PlotItem):
    """
    **Bases:** :class:`PlotItem <pyqtgraph.PlotItem>`

    :class:`ColorBarItem` controls the application of a 
    :ref:`color map <apiref_colormap>` to one (or more) 
    :class:`~pyqtgraph.ImageItem`. It is a simpler, compact alternative to 
    :class:`~pyqtgraph.HistogramLUTItem`, without histogram or the 
    option to adjust the colors of the look-up table.

    A labeled axis is displayed directly next to the gradient to help identify values.
    Handles included in the color bar allow for interactive adjustment.

    A ColorBarItem can be assigned one or more :class:`~pyqtgraph.ImageItem` s 
    that will be displayed according to the selected color map and levels. The
    ColorBarItem can be used as a separate element in a 
    :class:`~pyqtgraph.GraphicsLayout` or added to the layout of a 
    :class:`~pyqtgraph.PlotItem` used to display image data with coordinate axes.

    =============================  =============================================
    **Signals:**
    sigLevelsChanged(self)         Emitted when the range sliders are moved
    sigLevelsChangeFinished(self)  Emitted when the range sliders are released
    =============================  =============================================
    """
    sigLevelsChanged: Incomplete
    sigLevelsChangeFinished: Incomplete
    img_list: Incomplete
    values: Incomplete
    rounding: Incomplete
    horizontal: Incomplete
    lo_lim: Incomplete
    hi_lim: Incomplete
    colorMapMenu: Incomplete
    axis: Incomplete
    bar: Incomplete
    interactive: Incomplete
    region: Incomplete
    region_changed_enable: bool
    def __init__(self, values: Incomplete | None = None, width: int = 25, colorMap: Incomplete | None = None, label: Incomplete | None = None, interactive: bool = True, limits: Incomplete | None = None, rounding: int = 1, orientation: str = 'vertical', pen: str = 'w', hoverPen: str = 'r', hoverBrush: str = '#FF000080', *, colorMapMenu: bool = True) -> None:
        """
        Creates a new ColorBarItem.

        Parameters
        ----------
        colorMap: `str` or :class:`~pyqtgraph.ColorMap`
            Determines the color map displayed and applied to assigned ImageItem(s).
        values: tuple of float, optional
            The range of values that will be represented by the color bar, as ``(min, max)``.
            If no values are supplied, the default is to use user-specified values from 
            an assigned image. If that does not exist, values will default to (0,1). 
        width: float, default=25.0
            The width of the displayed color bar.
        label: str, optional
            Label applied to the color bar axis.
        interactive: bool, default=True
            If `True`, handles are displayed to interactively adjust the level range.
        limits: `tuple of float`, optional
            Limits the adjustment range to `(low, high)`, `None` disables the limit.
        rounding: float, default=1
            Adjusted range values are rounded to multiples of this value.
        orientation: str, default 'vertical'
            'horizontal' or 'h' gives a horizontal color bar instead of the default vertical bar
        pen: :class:`QPen` or color_like
            Sets the color of adjustment handles in interactive mode.
        hoverPen: :class:`QPen` or color_like
            Sets the color of adjustment handles when hovered over.
        hoverBrush: :class:`QBrush` or color_like
            Sets the color of movable center region when hovered over.
        colorMapMenu: `bool` or :class:`~pyqtgraph.ColorMapMenu`, default=True
            Determines whether colormap menu functionality is enabled.
        """
    def setImageItem(self, img, insert_in: Incomplete | None = None) -> None:
        '''
        Assigns an item or list of items to be represented and controlled.
        Supported "image items": class:`~pyqtgraph.ImageItem`, class:`~pyqtgraph.PColorMeshItem`

        Parameters
        ----------
        image: :class:`~pyqtgraph.ImageItem` or list of :class:`~pyqtgraph.ImageItem`
            Assigns one or more image items to this ColorBarItem.
            If a :class:`~pyqtgraph.ColorMap` is defined for ColorBarItem, this will be assigned to the 
            ImageItems. Otherwise, the ColorBarItem will attempt to retrieve a color map from the image items.
            In interactive mode, ColorBarItem will control the levels of the assigned image items, 
            simultaneously if there is more than one.
            If the ColorBarItem was initialized without a specified ``values`` parameter, it will attempt 
            to retrieve a set of user-defined ``levels`` from one of the image items. If this fails,
            the default values of ColorBarItem will be used as the (min, max) levels of the colorbar. 
            Note that, for non-interactive ColorBarItems, levels may be overridden by image items with 
            auto-scaling colors (defined by ``enableAutoLevels``). When using an interactive ColorBarItem
            in an animated plot, auto-scaling for its assigned image items should be *manually* disabled.
        insert_in: :class:`~pyqtgraph.PlotItem`, optional
            If a PlotItem is given, the color bar is inserted on the right
            or bottom of the plot, depending on the specified orientation.
        '''
    def setColorMap(self, colorMap) -> None:
        """
        Sets a color map to determine the ColorBarItem's look-up table. The same
        look-up table is applied to any assigned ImageItem.
        
        `colorMap` can be a :class:`~pyqtgraph.ColorMap` or a string argument that is passed to 
        :func:`colormap.get() <pyqtgraph.colormap.get>`.
        """
    def colorMap(self):
        """
        Returns the assigned ColorMap object.
        """
    def setLevels(self, values: Incomplete | None = None, low: Incomplete | None = None, high: Incomplete | None = None, update_items: bool = True) -> None:
        """
        Sets the displayed range of image levels.

        Parameters
        ----------
        values: tuple of float
            Specifies levels as tuple ``(low, high)``. Either value can be `None` to leave
            the previous value unchanged. Takes precedence over `low` and `high` parameters.
        low: float
            Applies a new low level to color bar and assigned images
        high: float
            Applies a new high level to color bar and assigned images
        """
    def levels(self):
        """ Returns the currently set levels as the tuple ``(low, high)``. """
    def mouseClickEvent(self, ev) -> None: ...
