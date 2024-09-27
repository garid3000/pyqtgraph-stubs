from ...Qt import QtWidgets #, isQObjectAlive, QT_LIB QtCore, QtGui,
from ..GraphicsWidget import GraphicsWidget
from ..ItemGroup import ItemGroup
from _typeshed import Incomplete

__all__ = ['ViewBox']

class WeakList:
    def __init__(self) -> None: ...
    def append(self, obj) -> None: ...
    def __iter__(self): ...

class ChildGroup(ItemGroup):
    itemsChangedListeners: Incomplete
    def __init__(self, parent) -> None: ...
    def itemChange(self, change, value): ...

class ViewBox(GraphicsWidget):
    """
    **Bases:** :class:`GraphicsWidget <pyqtgraph.GraphicsWidget>`

    Box that allows internal scaling/panning of children by mouse drag.
    This class is usually created automatically as part of a :class:`PlotItem <pyqtgraph.PlotItem>` or :ref:`Canvas <Canvas>` or with :func:`GraphicsLayout.addViewBox() <pyqtgraph.GraphicsLayout.addViewBox>`.

    Features:

      * Scaling contents by mouse or auto-scale when contents change
      * View linking--multiple views display the same data ranges
      * Configurable by context menu
      * Item coordinate mapping methods

    """
    sigYRangeChanged: Incomplete
    sigXRangeChanged: Incomplete
    sigRangeChangedManually: Incomplete
    sigRangeChanged: Incomplete
    sigStateChanged: Incomplete
    sigTransformChanged: Incomplete
    sigResized: Incomplete
    PanMode: int
    RectMode: int
    XAxis: int
    YAxis: int
    XYAxes: int
    NamedViews: Incomplete
    AllViews: Incomplete
    name: Incomplete
    linksBlocked: bool
    addedItems: Incomplete
    state: Incomplete
    locateGroup: Incomplete
    childGroup: Incomplete
    background: Incomplete
    border: Incomplete
    borderRect: Incomplete
    target: Incomplete
    axHistory: Incomplete
    axHistoryPointer: int
    menu: Incomplete
    def __init__(self, parent: Incomplete | None = None, border: Incomplete | None = None, lockAspect: bool = False, enableMouse: bool = True, invertY: bool = False, enableMenu: bool = True, name: Incomplete | None = None, invertX: bool = False, defaultPadding: float = 0.02) -> None:
        '''
        =================  =============================================================
        **Arguments:**
        *parent*           (QGraphicsWidget) Optional parent widget
        *border*           (QPen) Do draw a border around the view, give any
                           single argument accepted by :func:`mkPen <pyqtgraph.mkPen>`
        *lockAspect*       (False or float) The aspect ratio to lock the view
                           coorinates to. (or False to allow the ratio to change)
        *enableMouse*      (bool) Whether mouse can be used to scale/pan the view
        *invertY*          (bool) See :func:`invertY <pyqtgraph.ViewBox.invertY>`
        *invertX*          (bool) See :func:`invertX <pyqtgraph.ViewBox.invertX>`
        *enableMenu*       (bool) Whether to display a context menu when
                           right-clicking on the ViewBox background.
        *name*             (str) Used to register this ViewBox so that it appears
                           in the "Link axis" dropdown inside other ViewBox
                           context menus. This allows the user to manually link
                           the axes of any other view to this one.
        *defaultPadding*   (float) fraction of the data range that will be added
                           as padding by default
        =================  =============================================================
        '''
    @property
    def rbScaleBox(self): ...
    @rbScaleBox.setter
    def rbScaleBox(self, scaleBox) -> None: ...
    def getAspectRatio(self):
        """return the current aspect ratio"""
    def register(self, name):
        """
        Add this ViewBox to the registered list of views.

        This allows users to manually link the axes of any other ViewBox to
        this one. The specified *name* will appear in the drop-down lists for
        axis linking in the context menus of all other views.

        The same can be accomplished by initializing the ViewBox with the *name* attribute.
        """
    def unregister(self) -> None:
        """
        Remove this ViewBox from the list of linkable views. (see :func:`register() <pyqtgraph.ViewBox.register>`)
        """
    def close(self) -> None: ...
    def implements(self, interface): ...
    def itemChange(self, change, value): ...
    def prepareForPaint(self) -> None: ...
    def getState(self, copy: bool = True):
        """Return the current state of the ViewBox.
        Linked views are always converted to view names in the returned state."""
    def setState(self, state) -> None:
        """Restore the state of this ViewBox.
        (see also getState)"""
    def setBackgroundColor(self, color) -> None:
        """
        Set the background color of the ViewBox.

        If color is None, then no background will be drawn.

        Added in version 0.9.9
        """
    def setMouseMode(self, mode) -> None:
        """
        Set the mouse interaction mode. *mode* must be either ViewBox.PanMode or ViewBox.RectMode.
        In PanMode, the left mouse button pans the view and the right button scales.
        In RectMode, the left button draws a rectangle which updates the visible region (this mode is more suitable for single-button mice)
        """
    def setLeftButtonAction(self, mode: str = 'rect') -> None: ...
    def innerSceneItem(self): ...
    def setMouseEnabled(self, x: Incomplete | None = None, y: Incomplete | None = None) -> None:
        """
        Set whether each axis is enabled for mouse interaction. *x*, *y* arguments must be True or False.
        This allows the user to pan/scale one axis of the view while leaving the other axis unchanged.
        """
    def mouseEnabled(self): ...
    def setMenuEnabled(self, enableMenu: bool = True) -> None: ...
    def menuEnabled(self): ...
    def addItem(self, item: QtWidgets.QGraphicsItem, ignoreBounds: bool = False) -> None:
        """
        Add a QGraphicsItem to this view. The view will include this item when determining how to set its range
        automatically unless *ignoreBounds* is True.
        """
    def removeItem(self, item) -> None:
        """Remove an item from this view."""
    def clear(self) -> None: ...
    def resizeEvent(self, ev) -> None: ...
    def boundingRect(self): ...
    def viewRange(self):
        """Return a the view's visible range as a list: [[xmin, xmax], [ymin, ymax]]"""
    def viewRect(self):
        """Return a QRectF bounding the region visible within the ViewBox"""
    def targetRange(self): ...
    def targetRect(self):
        """
        Return the region which has been requested to be visible.
        (this is not necessarily the same as the region that is *actually* visible--
        resizing and aspect ratio constraints can cause targetRect() and viewRect() to differ)
        """
    def setRange(self, rect: Incomplete | None = None, xRange: Incomplete | None = None, yRange: Incomplete | None = None, padding: Incomplete | None = None, update: bool = True, disableAutoRange: bool = True) -> None:
        """
        Set the visible range of the ViewBox.
        Must specify at least one of *rect*, *xRange*, or *yRange*.

        ================== =====================================================================
        **Arguments:**
        *rect*             (QRectF) The full range that should be visible in the view box.
        *xRange*           (min,max) The range that should be visible along the x-axis.
        *yRange*           (min,max) The range that should be visible along the y-axis.
        *padding*          (float) Expand the view by a fraction of the requested range.
                           By default, this value is set between the default padding value
                           and 0.1 depending on the size of the ViewBox.
        *update*           (bool) If True, update the range of the ViewBox immediately.
                           Otherwise, the update is deferred until before the next render.
        *disableAutoRange* (bool) If True, auto-ranging is diabled. Otherwise, it is left
                           unchanged.
        ================== =====================================================================

        """
    def setYRange(self, min:float, max:float, padding: float | None = None, update: bool = True) -> None:
        """
        Set the visible Y range of the view to [*min*, *max*].
        The *padding* argument causes the range to be set larger by the fraction specified.
        (by default, this value is between the default padding and 0.1 depending on the size of the ViewBox)
        """
    def setXRange(self, min, max, padding: Incomplete | None = None, update: bool = True) -> None:
        """
        Set the visible X range of the view to [*min*, *max*].
        The *padding* argument causes the range to be set larger by the fraction specified.
        (by default, this value is between the default padding and 0.1 depending on the size of the ViewBox)
        """
    def autoRange(self, padding: Incomplete | None = None, items: Incomplete | None = None, item: Incomplete | None = None) -> None:
        """
        Set the range of the view box to make all children visible.
        Note that this is not the same as enableAutoRange, which causes the view to
        automatically auto-range whenever its contents are changed.

        ==============  =============================================================
        **Arguments:**
        padding         The fraction of the total data range to add on to the final
                        visible range. By default, this value is set between the
                        default padding and 0.1 depending on the size of the ViewBox.
        items           If specified, this is a list of items to consider when
                        determining the visible range.
        ==============  =============================================================
        """
    def suggestPadding(self, axis): ...
    def setLimits(self, **kwds) -> None:
        """
        Set limits that constrain the possible view ranges.

        **Panning limits**. The following arguments define the region within the
        viewbox coordinate system that may be accessed by panning the view.

        =========== ============================================================
        xMin        Minimum allowed x-axis value
        xMax        Maximum allowed x-axis value
        yMin        Minimum allowed y-axis value
        yMax        Maximum allowed y-axis value
        =========== ============================================================

        **Scaling limits**. These arguments prevent the view being zoomed in or
        out too far.

        =========== ============================================================
        minXRange   Minimum allowed left-to-right span across the view.
        maxXRange   Maximum allowed left-to-right span across the view.
        minYRange   Minimum allowed top-to-bottom span across the view.
        maxYRange   Maximum allowed top-to-bottom span across the view.
        =========== ============================================================

        Added in version 0.9.9
        """
    def scaleBy(self, s: Incomplete | None = None, center: Incomplete | None = None, x: Incomplete | None = None, y: Incomplete | None = None) -> None:
        """
        Scale by *s* around given center point (or center of view).
        *s* may be a Point or tuple (x, y).

        Optionally, x or y may be specified individually. This allows the other
        axis to be left unaffected (note that using a scale factor of 1.0 may
        cause slight changes due to floating-point error).
        """
    def translateBy(self, t: Incomplete | None = None, x: Incomplete | None = None, y: Incomplete | None = None) -> None:
        """
        Translate the view by *t*, which may be a Point or tuple (x, y).

        Alternately, x or y may be specified independently, leaving the other
        axis unchanged (note that using a translation of 0 may still cause
        small changes due to floating-point error).
        """
    def enableAutoRange(self, axis: Incomplete | None = None, enable: bool = True, x: Incomplete | None = None, y: Incomplete | None = None) -> None:
        """
        Enable (or disable) auto-range for *axis*, which may be ViewBox.XAxis, ViewBox.YAxis, or ViewBox.XYAxes for both
        (if *axis* is omitted, both axes will be changed).
        When enabled, the axis will automatically rescale when items are added/removed or change their shape.
        The argument *enable* may optionally be a float (0.0-1.0) which indicates the fraction of the data that should
        be visible (this only works with items implementing a dataBounds method, such as PlotDataItem).
        """
    def disableAutoRange(self, axis: Incomplete | None = None) -> None:
        """Disables auto-range. (See enableAutoRange)"""
    def autoRangeEnabled(self): ...
    def setAutoPan(self, x: Incomplete | None = None, y: Incomplete | None = None) -> None:
        """Set whether automatic range will only pan (not scale) the view.
        """
    def setAutoVisible(self, x: Incomplete | None = None, y: Incomplete | None = None) -> None:
        """Set whether automatic range uses only visible data when determining
        the range to show.
        """
    def updateAutoRange(self) -> None: ...
    def setXLink(self, view: ViewBox) -> None:
        """Link this view's X axis to another view. (see LinkView)"""
    def setYLink(self, view: ViewBox) -> None:
        """Link this view's Y axis to another view. (see LinkView)"""
    def setLogMode(self, axis, logMode) -> None:
        """Informs ViewBox that log mode is active for the specified axis, so that the view range cen be restricted"""
    def linkView(self, axis, view) -> None:
        """
        Link X or Y axes of two views and unlink any previously connected axes. *axis* must be ViewBox.XAxis or ViewBox.YAxis.
        If view is None, the axis is left unlinked.
        """
    def blockLink(self, b) -> None: ...
    def linkedXChanged(self) -> None: ...
    def linkedYChanged(self) -> None: ...
    def linkedView(self, ax): ...
    def linkedViewChanged(self, view: ViewBox, axis: int) -> None: ...
    def screenGeometry(self):
        """return the screen geometry of the viewbox"""
    def itemsChanged(self) -> None: ...
    def itemBoundsChanged(self, item) -> None: ...
    def invertY(self, b: bool = True) -> None:
        """
        By default, the positive y-axis points upward on the screen. Use invertY(True) to reverse the y-axis.
        """
    def yInverted(self): ...
    def invertX(self, b: bool = True) -> None:
        """
        By default, the positive x-axis points rightward on the screen. Use invertX(True) to reverse the x-axis.
        """
    def xInverted(self): ...
    def setBorder(self, *args, **kwds) -> None:
        """
        Set the pen used to draw border around the view

        If border is None, then no border will be drawn.

        Added in version 0.9.10

        See :func:`mkPen <pyqtgraph.mkPen>` for arguments.
        """
    def setDefaultPadding(self, padding: float = 0.02) -> None:
        """
        Sets the fraction of the data range that is used to pad the view range in when auto-ranging.
        By default, this fraction is 0.02.
        """
    def setAspectLocked(self, lock: bool = True, ratio: int = 1) -> None:
        """
        If the aspect ratio is locked, view scaling must always preserve the aspect ratio.
        By default, the ratio is set to 1; x and y both have the same scaling.
        This ratio can be overridden (xScale/yScale), or use None to lock in the current ratio.
        """
    def childTransform(self):
        """
        Return the transform that maps from child(item in the childGroup) coordinates to local coordinates.
        (This maps from inside the viewbox to outside)
        """
    def mapToView(self, obj):
        """Maps from the local coordinates of the ViewBox to the coordinate system displayed inside the ViewBox"""
    def mapFromView(self, obj):
        """Maps from the coordinate system displayed inside the ViewBox to the local coordinates of the ViewBox"""
    def mapSceneToView(self, obj):
        """Maps from scene coordinates to the coordinate system displayed inside the ViewBox"""
    def mapViewToScene(self, obj):
        """Maps from the coordinate system displayed inside the ViewBox to scene coordinates"""
    def mapFromItemToView(self, item, obj):
        """Maps *obj* from the local coordinate system of *item* to the view coordinates"""
    def mapFromViewToItem(self, item, obj):
        """Maps *obj* from view coordinates to the local coordinate system of *item*."""
    def mapViewToDevice(self, obj): ...
    def mapDeviceToView(self, obj): ...
    def viewPixelSize(self):
        """Return the (width, height) of a screen pixel in view coordinates."""
    def itemBoundingRect(self, item):
        """Return the bounding rect of the item in view coordinates"""
    def wheelEvent(self, ev, axis: Incomplete | None = None) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def raiseContextMenu(self, ev) -> None: ...
    def getMenu(self, ev): ...
    def getContextMenus(self, event): ...
    def mouseDragEvent(self, ev, axis: Incomplete | None = None) -> None: ...
    def keyPressEvent(self, ev) -> None:
        '''
        This routine should capture key presses in the current view box.
        Key presses are used only when mouse mode is RectMode
        The following events are implemented:
        ctrl-A : zooms out to the default "full" view of the plot
        ctrl-+ : moves forward in the zooming stack (if it exists)
        ctrl-- : moves backward in the zooming stack (if it exists)

        '''
    def scaleHistory(self, d) -> None: ...
    def updateScaleBox(self, p1, p2) -> None: ...
    def showAxRect(self, ax, **kwargs) -> None:
        """Set the visible range to the given rectangle
        Passes keyword arguments to setRange
        """
    def allChildren(self, item: Incomplete | None = None):
        """Return a list of all children and grandchildren of this ViewBox"""
    def childrenBounds(self, frac: Incomplete | None = None, orthoRange=(None, None), items: Incomplete | None = None):
        """Return the bounding range of all children.
        [[xmin, xmax], [ymin, ymax]]
        Values may be None if there are no specific bounds for an axis.
        """
    def childrenBoundingRect(self, *args, **kwds): ...
    def updateViewRange(self, forceX: bool = False, forceY: bool = False) -> None: ...
    def updateMatrix(self, changed: Incomplete | None = None) -> None: ...
    def paint(self, p, opt, widget) -> None: ...
    def updateBackground(self) -> None: ...
    def updateViewLists(self): ...
    @staticmethod
    def updateAllViewLists() -> None: ...
    @staticmethod
    def forgetView(vid, name) -> None: ...
    @staticmethod
    def quit() -> None: ...
    def locate(self, item, timeout: float = 3.0, children: bool = False) -> None:
        """
        Temporarily display the bounding rect of an item and lines connecting to the center of the view.
        This is useful for determining the location of items that may be out of the range of the ViewBox.
        if allChildren is True, then the bounding rect of all item's children will be shown instead.
        """
    def clearLocate(self) -> None: ...
