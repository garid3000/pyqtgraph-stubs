from typing import SupportsIndex
from ..Qt import QtWidgets, QtCore
from .GraphicsObject import GraphicsObject
from .UIGraphicsItem import UIGraphicsItem
from _typeshed import Incomplete
from ..Point import Point



__all__ = ['ROI', 'TestROI', 'RectROI', 'EllipseROI', 'CircleROI', 'LineROI', 'MultiLineROI', 'MultiRectROI', 'LineSegmentROI', 'PolyLineROI', 'CrosshairROI', 'TriangleROI']

class ROI(GraphicsObject):
    """
    Generic region-of-interest widget.

    Can be used for implementing many types of selection box with
    rotate/translate/scale handles.
    ROIs can be customized to have a variety of shapes (by subclassing or using
    any of the built-in subclasses) and any combination of draggable handles
    that allow the user to manipulate the ROI.

    Default mouse interaction:

      * Left drag moves the ROI
      * Left drag + Ctrl moves the ROI with position snapping
      * Left drag + Alt rotates the ROI
      * Left drag + Alt + Ctrl rotates the ROI with angle snapping
      * Left drag + Shift scales the ROI
      * Left drag + Shift + Ctrl scales the ROI with size snapping

    In addition to the above interaction modes, it is possible to attach any
    number of handles to the ROI that can be dragged to change the ROI in
    various ways (see the ROI.add____Handle methods).


    ================ ===========================================================
    **Arguments**
    pos              (length-2 sequence) Indicates the position of the ROI's
                     origin. For most ROIs, this is the lower-left corner of
                     its bounding rectangle.
    size             (length-2 sequence) Indicates the width and height of the
                     ROI.
    angle            (float) The rotation of the ROI in degrees. Default is 0.
    invertible       (bool) If True, the user may resize the ROI to have
                     negative width or height (assuming the ROI has scale
                     handles). Default is False.
    maxBounds        (QRect, QRectF, or None) Specifies boundaries that the ROI
                     cannot be dragged outside of by the user. Default is None.
    snapSize         (float) The spacing of snap positions used when *scaleSnap*
                     or *translateSnap* are enabled. Default is 1.0.
    scaleSnap        (bool) If True, the width and height of the ROI are forced
                     to be integer multiples of *snapSize* when being resized
                     by the user. Default is False.
    translateSnap    (bool) If True, the x and y positions of the ROI are forced
                     to be integer multiples of *snapSize* when being resized
                     by the user. Default is False.
    rotateSnap       (bool) If True, the ROI angle is forced to a multiple of
                     the ROI's snap angle (default is 15 degrees) when rotated
                     by the user. Default is False.
    parent           (QGraphicsItem) The graphics item parent of this ROI. It
                     is generally not necessary to specify the parent.
    pen              (QPen or argument to pg.mkPen) The pen to use when drawing
                     the shape of the ROI.
    hoverPen         (QPen or argument to mkPen) The pen to use while the
                     mouse is hovering over the ROI shape.
    handlePen        (QPen or argument to mkPen) The pen to use when drawing
                     the ROI handles.
    handleHoverPen   (QPen or argument to mkPen) The pen to use while the mouse
                     is hovering over an ROI handle.
    movable          (bool) If True, the ROI can be moved by dragging anywhere
                     inside the ROI. Default is True.
    rotatable        (bool) If True, the ROI can be rotated by mouse drag + ALT
    resizable        (bool) If True, the ROI can be resized by mouse drag +
                     SHIFT
    removable        (bool) If True, the ROI will be given a context menu with
                     an option to remove the ROI. The ROI emits
                     sigRemoveRequested when this menu action is selected.
                     Default is False.
    antialias        (bool) If True, the ROI will render using AntiAliasing,
                     this is what is desired in almost all cases, the option is
                     added for testing purposes.
                     Default is True
    ================ ===========================================================



    ======================= ====================================================
    **Signals**
    sigRegionChangeFinished Emitted when the user stops dragging the ROI (or
                            one of its handles) or if the ROI is changed
                            programatically.
    sigRegionChangeStarted  Emitted when the user starts dragging the ROI (or
                            one of its handles).
    sigRegionChanged        Emitted any time the position of the ROI changes,
                            including while it is being dragged by the user.
    sigHoverEvent           Emitted when the mouse hovers over the ROI.
    sigClicked              Emitted when the user clicks on the ROI.
                            Note that clicking is disabled by default to prevent
                            stealing clicks from objects behind the ROI. To
                            enable clicking, call
                            roi.setAcceptedMouseButtons(QtCore.Qt.MouseButton.LeftButton).
                            See QtWidgets.QGraphicsItem documentation for more
                            details.
    sigRemoveRequested      Emitted when the user selects 'remove' from the
                            ROI's context menu (if available).
    ======================= ====================================================
    """
    sigRegionChangeFinished: QtCore.Signal
    sigRegionChangeStarted: QtCore.Signal
    sigRegionChanged: QtCore.Signal
    sigHoverEvent: Incomplete
    sigClicked: Incomplete
    sigRemoveRequested: Incomplete
    aspectLocked: Incomplete
    translatable: Incomplete
    rotatable: Incomplete
    resizable: Incomplete
    removable: Incomplete
    menu: Incomplete
    freeHandleMoved: bool
    mouseHovering: bool
    hoverPen: Incomplete
    handlePen: Incomplete
    handleHoverPen: Incomplete
    handles: Incomplete
    state: Incomplete
    lastState: Incomplete
    isMoving: bool
    handleSize: int
    invertible: Incomplete
    maxBounds: Incomplete
    snapSize: Incomplete
    translateSnap: Incomplete
    rotateSnap: Incomplete
    rotateSnapAngle: float
    scaleSnap: Incomplete
    scaleSnapSize: Incomplete
    mouseDragHandler: Incomplete
    def __init__(self, pos, size=..., angle: float = 0.0, invertible: bool = False, maxBounds: Incomplete | None = None, snapSize: float = 1.0, scaleSnap: bool = False, translateSnap: bool = False, rotateSnap: bool = False, parent: Incomplete | None = None, pen: Incomplete | None = None, hoverPen: Incomplete | None = None, handlePen: Incomplete | None = None, handleHoverPen: Incomplete | None = None, movable: bool = True, rotatable: bool = True, resizable: bool = True, removable: bool = False, aspectLocked: bool = False, antialias: bool = True) -> None: ...
    def getState(self) -> dict[str, Point | float]: ...
    def stateCopy(self): ...
    def saveState(self):
        """Return the state of the widget in a format suitable for storing to
        disk. (Points are converted to tuple)

        Combined with setState(), this allows ROIs to be easily saved and
        restored."""
    def setState(self, state, update: bool = True) -> None:
        """
        Set the state of the ROI from a structure generated by saveState() or
        getState().
        """
    def setZValue(self, z:float) -> None: ...
    def parentBounds(self):
        """
        Return the bounding rectangle of this ROI in the coordinate system
        of its parent.
        """
    pen: Incomplete
    currentPen: Incomplete
    def setPen(self, *args, **kwargs) -> None:
        """
        Set the pen to use when drawing the ROI shape.
        For arguments, see :func:`mkPen <pyqtgraph.mkPen>`.
        """
    def size(self):
        """Return the size (w,h) of the ROI."""
    def pos(self):
        """Return the position (x,y) of the ROI's origin.
        For most ROIs, this will be the lower-left corner."""
    def angle(self):
        """Return the angle of the ROI in degrees."""
    def setPos(self, pos: float | Point | QtCore.QPointF | tuple[float, float] | list[float], y: float | None = None, update: bool = True, finish: bool = True) -> None:
        """Set the position of the ROI (in the parent's coordinate system).

        Accepts either separate (x, y) arguments or a single :class:`Point` or
        ``QPointF`` argument.

        By default, this method causes both ``sigRegionChanged`` and
        ``sigRegionChangeFinished`` to be emitted. If *finish* is False, then
        ``sigRegionChangeFinished`` will not be emitted. You can then use
        stateChangeFinished() to cause the signal to be emitted after a series
        of state changes.

        If *update* is False, the state change will be remembered but not processed and no signals
        will be emitted. You can then use stateChanged() to complete the state change. This allows
        multiple change functions to be called sequentially while minimizing processing overhead
        and repeated signals. Setting ``update=False`` also forces ``finish=False``.
        """
    def setSize(self, size: tuple[float, float] | list[float] | Point | QtCore.QPointF, center: Point | None | tuple[float, float] = None, centerLocal: Incomplete | None = None, snap: bool = False, update: bool = True, finish: bool = True) -> None:
        """
        Set the ROI's size.

        =============== ==========================================================================
        **Arguments**
        size            (Point | QPointF | sequence) The final size of the ROI
        center          (None | Point) Optional center point around which the ROI is scaled,
                        expressed as [0-1, 0-1] over the size of the ROI.
        centerLocal     (None | Point) Same as *center*, but the position is expressed in the
                        local coordinate system of the ROI
        snap            (bool) If True, the final size is snapped to the nearest increment (see
                        ROI.scaleSnapSize)
        update          (bool) See setPos()
        finish          (bool) See setPos()
        =============== ==========================================================================
        """
    def setAngle(self, angle, center: Incomplete | None = None, centerLocal: Incomplete | None = None, snap: bool = False, update: bool = True, finish: bool = True) -> None:
        """
        Set the ROI's rotation angle.

        =============== ==========================================================================
        **Arguments**
        angle           (float) The final ROI angle in degrees
        center          (None | Point) Optional center point around which the ROI is rotated,
                        expressed as [0-1, 0-1] over the size of the ROI.
        centerLocal     (None | Point) Same as *center*, but the position is expressed in the
                        local coordinate system of the ROI
        snap            (bool) If True, the final ROI angle is snapped to the nearest increment
                        (default is 15 degrees; see ROI.rotateSnapAngle)
        update          (bool) See setPos()
        finish          (bool) See setPos()
        =============== ==========================================================================
        """
    def scale(self, s, center: Incomplete | None = None, centerLocal: Incomplete | None = None, snap: bool = False, update: bool = True, finish: bool = True) -> None:
        """
        Resize the ROI by scaling relative to *center*.
        See setPos() for an explanation of the *update* and *finish* arguments.
        """
    def translate(self, *args, **kargs) -> None:
        """
        Move the ROI to a new position.
        Accepts either (x, y, snap) or ([x,y], snap) as arguments
        If the ROI is bounded and the move would exceed boundaries, then the ROI
        is moved to the nearest acceptable position instead.

        *snap* can be:

        =============== ==========================================================================
        None (default)  use self.translateSnap and self.snapSize to determine whether/how to snap
        False           do not snap
        Point(w,h)      snap to rectangular grid with spacing (w,h)
        True            snap using self.snapSize (and ignoring self.translateSnap)
        =============== ==========================================================================

        Also accepts *update* and *finish* arguments (see setPos() for a description of these).
        """
    def rotate(self, angle, center: Incomplete | None = None, snap: bool = False, update: bool = True, finish: bool = True) -> None:
        """
        Rotate the ROI by *angle* degrees.

        =============== ==========================================================================
        **Arguments**
        angle           (float) The angle in degrees to rotate
        center          (None | Point) Optional center point around which the ROI is rotated, in
                        the local coordinate system of the ROI
        snap            (bool) If True, the final ROI angle is snapped to the nearest increment
                        (default is 15 degrees; see ROI.rotateSnapAngle)
        update          (bool) See setPos()
        finish          (bool) See setPos()
        =============== ==========================================================================
        """
    preMoveState: Incomplete
    def handleMoveStarted(self) -> None: ...
    def addTranslateHandle(self, pos, axes: Incomplete | None = None, item: Incomplete | None = None, name: Incomplete | None = None, index: Incomplete | None = None):
        """
        Add a new translation handle to the ROI. Dragging the handle will move
        the entire ROI without changing its angle or shape.

        Note that, by default, ROIs may be moved by dragging anywhere inside the
        ROI. However, for larger ROIs it may be desirable to disable this and
        instead provide one or more translation handles.

        =================== ====================================================
        **Arguments**
        pos                 (length-2 sequence) The position of the handle
                            relative to the shape of the ROI. A value of (0,0)
                            indicates the origin, whereas (1, 1) indicates the
                            upper-right corner, regardless of the ROI's size.
        item                The Handle instance to add. If None, a new handle
                            will be created.
        name                The name of this handle (optional). Handles are
                            identified by name when calling
                            getLocalHandlePositions and getSceneHandlePositions.
        =================== ====================================================
        """
    def addFreeHandle(self, pos: Incomplete | None = None, axes: Incomplete | None = None, item: Incomplete | None = None, name: Incomplete | None = None, index: Incomplete | None = None):
        """
        Add a new free handle to the ROI. Dragging free handles has no effect
        on the position or shape of the ROI.

        =================== ====================================================
        **Arguments**
        pos                 (length-2 sequence) The position of the handle
                            relative to the shape of the ROI. A value of (0,0)
                            indicates the origin, whereas (1, 1) indicates the
                            upper-right corner, regardless of the ROI's size.
        item                The Handle instance to add. If None, a new handle
                            will be created.
        name                The name of this handle (optional). Handles are
                            identified by name when calling
                            getLocalHandlePositions and getSceneHandlePositions.
        =================== ====================================================
        """
    def addScaleHandle(self, pos: tuple[float, float]|list[float], center: tuple[float, float]|list[float], axes: int  | tuple[int, int] | tuple[int, int, int] | None = None, item: Handle | None = None, name: str | None = None, lockAspect: bool = False, index: SupportsIndex | None = None) -> Handle:
        """
        Add a new scale handle to the ROI. Dragging a scale handle allows the
        user to change the height and/or width of the ROI.

        =================== ====================================================
        **Arguments**
        pos                 (length-2 sequence) The position of the handle
                            relative to the shape of the ROI. A value of (0,0)
                            indicates the origin, whereas (1, 1) indicates the
                            upper-right corner, regardless of the ROI's size.
        center              (length-2 sequence) The center point around which
                            scaling takes place. If the center point has the
                            same x or y value as the handle position, then
                            scaling will be disabled for that axis.
        item                The Handle instance to add. If None, a new handle
                            will be created.
        name                The name of this handle (optional). Handles are
                            identified by name when calling
                            getLocalHandlePositions and getSceneHandlePositions.
        =================== ====================================================
        """
    def addRotateHandle(self, pos, center, item: Incomplete | None = None, name: Incomplete | None = None, index: Incomplete | None = None):
        """
        Add a new rotation handle to the ROI. Dragging a rotation handle allows
        the user to change the angle of the ROI.

        =================== ====================================================
        **Arguments**
        pos                 (length-2 sequence) The position of the handle
                            relative to the shape of the ROI. A value of (0,0)
                            indicates the origin, whereas (1, 1) indicates the
                            upper-right corner, regardless of the ROI's size.
        center              (length-2 sequence) The center point around which
                            rotation takes place.
        item                The Handle instance to add. If None, a new handle
                            will be created.
        name                The name of this handle (optional). Handles are
                            identified by name when calling
                            getLocalHandlePositions and getSceneHandlePositions.
        =================== ====================================================
        """
    def addScaleRotateHandle(self, pos, center, item: Incomplete | None = None, name: Incomplete | None = None, index: Incomplete | None = None):
        """
        Add a new scale+rotation handle to the ROI. When dragging a handle of
        this type, the user can simultaneously rotate the ROI around an
        arbitrary center point as well as scale the ROI by dragging the handle
        toward or away from the center point.

        =================== ====================================================
        **Arguments**
        pos                 (length-2 sequence) The position of the handle
                            relative to the shape of the ROI. A value of (0,0)
                            indicates the origin, whereas (1, 1) indicates the
                            upper-right corner, regardless of the ROI's size.
        center              (length-2 sequence) The center point around which
                            scaling and rotation take place.
        item                The Handle instance to add. If None, a new handle
                            will be created.
        name                The name of this handle (optional). Handles are
                            identified by name when calling
                            getLocalHandlePositions and getSceneHandlePositions.
        =================== ====================================================
        """
    def addRotateFreeHandle(self, pos, center, axes: Incomplete | None = None, item: Incomplete | None = None, name: Incomplete | None = None, index: Incomplete | None = None):
        """
        Add a new rotation+free handle to the ROI. When dragging a handle of
        this type, the user can rotate the ROI around an
        arbitrary center point, while moving toward or away from the center
        point has no effect on the shape of the ROI.

        =================== ====================================================
        **Arguments**
        pos                 (length-2 sequence) The position of the handle
                            relative to the shape of the ROI. A value of (0,0)
                            indicates the origin, whereas (1, 1) indicates the
                            upper-right corner, regardless of the ROI's size.
        center              (length-2 sequence) The center point around which
                            rotation takes place.
        item                The Handle instance to add. If None, a new handle
                            will be created.
        name                The name of this handle (optional). Handles are
                            identified by name when calling
                            getLocalHandlePositions and getSceneHandlePositions.
        =================== ====================================================
        """
    def addHandle(self, info, index: Incomplete | None = None): ...
    def indexOfHandle(self, handle):
        """
        Return the index of *handle* in the list of this ROI's handles.
        """
    def removeHandle(self, handle) -> None:
        """Remove a handle from this ROI. Argument may be either a Handle
        instance or the integer index of the handle."""
    def replaceHandle(self, oldHandle, newHandle) -> None:
        """Replace one handle in the ROI for another. This is useful when
        connecting multiple ROIs together.

        *oldHandle* may be a Handle instance or the index of a handle to be
        replaced."""
    def checkRemoveHandle(self, handle): ...
    def getLocalHandlePositions(self, index: Incomplete | None = None):
        """Returns the position of handles in the ROI's coordinate system.

        The format returned is a list of (name, pos) tuples.
        """
    def getSceneHandlePositions(self, index: Incomplete | None = None):
        """Returns the position of handles in the scene coordinate system.

        The format returned is a list of (name, pos) tuples.
        """
    def getHandles(self):
        """
        Return a list of this ROI's Handles.
        """
    def mapSceneToParent(self, pt): ...
    def setSelected(self, s) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def setMouseHover(self, hover) -> None: ...
    def contextMenuEnabled(self): ...
    def raiseContextMenu(self, ev) -> None: ...
    def getMenu(self): ...
    def removeClicked(self) -> None: ...
    def mouseDragEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def cancelMove(self) -> None: ...
    def checkPointMove(self, handle, pos, modifiers):
        """When handles move, they must ask the ROI if the move is acceptable.
        By default, this always returns True. Subclasses may wish override.
        """
    def movePoint(self, handle, pos, modifiers: Incomplete | None = None, finish: bool = True, coords: str = 'parent') -> None: ...
    def stateChanged(self, finish: bool = True) -> None:
        """Process changes to the state of the ROI.
        If there are any changes, then the positions of handles are updated accordingly
        and sigRegionChanged is emitted. If finish is True, then
        sigRegionChangeFinished will also be emitted."""
    def stateChangeFinished(self) -> None: ...
    def stateRect(self, state): ...
    def getSnapPosition(self, pos, snap: Incomplete | None = None): ...
    def boundingRect(self): ...
    def paint(self, p, opt, widget) -> None: ...
    def getArraySlice(self, data, img, axes=(0, 1), returnSlice: bool = True):
        """Return a tuple of slice objects that can be used to slice the region
        from *data* that is covered by the bounding rectangle of this ROI.
        Also returns the transform that maps the ROI into data coordinates.

        If returnSlice is set to False, the function returns a pair of tuples with the values that would have
        been used to generate the slice objects. ((ax0Start, ax0Stop), (ax1Start, ax1Stop))

        If the slice cannot be computed (usually because the scene/transforms are not properly
        constructed yet), then the method returns None.
        """
    def getArrayRegion(self, data, img, axes=(0, 1), returnMappedCoords: bool = False, **kwds):
        """Use the position and orientation of this ROI relative to an imageItem
        to pull a slice from an array.

        =================== ====================================================
        **Arguments**
        data                The array to slice from. Note that this array does
                            *not* have to be the same data that is represented
                            in *img*.
        img                 (ImageItem or other suitable QGraphicsItem)
                            Used to determine the relationship between the
                            ROI and the boundaries of *data*.
        axes                (length-2 tuple) Specifies the axes in *data* that
                            correspond to the (x, y) axes of *img*. If the
                            image's axis order is set to
                            'row-major', then the axes are instead specified in
                            (y, x) order.
        returnMappedCoords  (bool) If True, the array slice is returned along
                            with a corresponding array of coordinates that were
                            used to extract data from the original array.
        \\**kwds             All keyword arguments are passed to
                            :func:`affineSlice <pyqtgraph.affineSlice>`.
        =================== ====================================================

        This method uses :func:`affineSlice <pyqtgraph.affineSlice>` to generate
        the slice from *data* and uses :func:`getAffineSliceParams <pyqtgraph.ROI.getAffineSliceParams>`
        to determine the parameters to pass to :func:`affineSlice <pyqtgraph.affineSlice>`.

        If *returnMappedCoords* is True, then the method returns a tuple (result, coords)
        such that coords is the set of coordinates used to interpolate values from the original
        data, mapped into the parent coordinate system of the image. This is useful, when slicing
        data from images that have been transformed, for determining the location of each value
        in the sliced data.

        All extra keyword arguments are passed to :func:`affineSlice <pyqtgraph.affineSlice>`.
        """
    def getAffineSliceParams(self, data, img, axes=(0, 1), fromBoundingRect: bool = False):
        """
        Returns the parameters needed to use :func:`affineSlice <pyqtgraph.affineSlice>`
        (shape, vectors, origin) to extract a subset of *data* using this ROI
        and *img* to specify the subset.

        If *fromBoundingRect* is True, then the ROI's bounding rectangle is used
        rather than the shape of the ROI.

        See :func:`getArrayRegion <pyqtgraph.ROI.getArrayRegion>` for more information.
        """
    def renderShapeMask(self, width, height):
        """Return an array of 0.0-1.0 into which the shape of the item has been drawn.

        This can be used to mask array selections.
        """
    def getGlobalTransform(self, relativeTo: Incomplete | None = None):
        """Return global transformation (rotation angle+translation) required to move
        from relative state to current state. If relative state isn't specified,
        then we use the state of the ROI when mouse is pressed."""
    def applyGlobalTransform(self, tr) -> None: ...

class Handle(UIGraphicsItem):
    """
    Handle represents a single user-interactable point attached to an ROI. They
    are usually created by a call to one of the ROI.add___Handle() methods.

    Handles are represented as a square, diamond, or circle, and are drawn with
    fixed pixel size regardless of the scaling of the view they are displayed in.

    Handles may be dragged to change the position, size, orientation, or other
    properties of the ROI they are attached to.
    """
    types: Incomplete
    sigClicked: Incomplete
    sigRemoveRequested: Incomplete
    rois: Incomplete
    radius: Incomplete
    typ: Incomplete
    pen: Incomplete
    hoverPen: Incomplete
    currentPen: Incomplete
    isMoving: bool
    menu: Incomplete
    deletable: Incomplete
    def __init__(self, radius, typ: Incomplete | None = None, pen=(200, 200, 220), hoverPen=(255, 255, 0), parent: Incomplete | None = None, deletable: bool = False, antialias: bool = True) -> None: ...
    def connectROI(self, roi) -> None: ...
    def disconnectROI(self, roi) -> None: ...
    def setDeletable(self, b) -> None: ...
    def removeClicked(self) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    removeAction: Incomplete
    def buildMenu(self): ...
    def getMenu(self): ...
    def raiseContextMenu(self, ev) -> None: ...
    startPos: Incomplete
    cursorOffset: Incomplete
    def mouseDragEvent(self, ev) -> None: ...
    def movePoint(self, pos, modifiers: Incomplete | None = None, finish: bool = True) -> None: ...
    path: Incomplete
    def buildPath(self) -> None: ...
    def paint(self, p, opt, widget) -> None: ...
    def shape(self): ...
    def boundingRect(self): ...
    def generateShape(self): ...
    def viewTransformChanged(self) -> None: ...

class MouseDragHandler:
    """Implements default mouse drag behavior for ROI (not for ROI handles).
    """
    roi: Incomplete
    dragMode: Incomplete
    startState: Incomplete
    snapModifier: Incomplete
    translateModifier: Incomplete
    rotateModifier: Incomplete
    scaleModifier: Incomplete
    rotateSpeed: float
    scaleSpeed: float
    def __init__(self, roi) -> None: ...
    startPos: Incomplete
    cursorOffset: Incomplete
    def mouseDragEvent(self, ev) -> None: ...

class TestROI(ROI):
    def __init__(self, pos, size, **args) -> None: ...

class RectROI(ROI):
    """
    Rectangular ROI subclass with a single scale handle at the top-right corner.

    ============== =============================================================
    **Arguments**
    pos            (length-2 sequence) The position of the ROI origin.
                   See ROI().
    size           (length-2 sequence) The size of the ROI. See ROI().
    centered       (bool) If True, scale handles affect the ROI relative to its
                   center, rather than its origin.
    sideScalers    (bool) If True, extra scale handles are added at the top and
                   right edges.
    \\**args        All extra keyword arguments are passed to ROI()
    ============== =============================================================

    """
    def __init__(self, pos, size, centered: bool = False, sideScalers: bool = False, **args) -> None: ...

class LineROI(ROI):
    '''
    Rectangular ROI subclass with scale-rotate handles on either side. This
    allows the ROI to be positioned as if moving the ends of a line segment.
    A third handle controls the width of the ROI orthogonal to its "line" axis.

    ============== =============================================================
    **Arguments**
    pos1           (length-2 sequence) The position of the center of the ROI\'s
                   left edge.
    pos2           (length-2 sequence) The position of the center of the ROI\'s
                   right edge.
    width          (float) The width of the ROI.
    \\**args        All extra keyword arguments are passed to ROI()
    ============== =============================================================

    '''
    def __init__(self, pos1, pos2, width, **args) -> None: ...

class MultiRectROI(QtWidgets.QGraphicsObject):
    """
    Chain of rectangular ROIs connected by handles.

    This is generally used to mark a curved path through
    an image similarly to PolyLineROI. It differs in that each segment
    of the chain is rectangular instead of linear and thus has width.

    ============== =============================================================
    **Arguments**
    points         (list of length-2 sequences) The list of points in the path.
    width          (float) The width of the ROIs orthogonal to the path.
    \\**args        All extra keyword arguments are passed to ROI()
    ============== =============================================================
    """
    sigRegionChangeFinished: Incomplete
    sigRegionChangeStarted: Incomplete
    sigRegionChanged: Incomplete
    pen: Incomplete
    roiArgs: Incomplete
    lines: Incomplete
    def __init__(self, points, width, pen: Incomplete | None = None, **args) -> None: ...
    def paint(self, *args) -> None: ...
    def boundingRect(self): ...
    def roiChangedEvent(self) -> None: ...
    def roiChangeStartedEvent(self) -> None: ...
    def roiChangeFinishedEvent(self) -> None: ...
    def getHandlePositions(self):
        """Return the positions of all handles in local coordinates."""
    def getArrayRegion(self, arr, img: Incomplete | None = None, axes=(0, 1), **kwds):
        """
        Return the result of :meth:`~pyqtgraph.ROI.getArrayRegion` for each rect
        in the chain concatenated into a single ndarray.

        See :meth:`~pyqtgraph.ROI.getArrayRegion` for a description of the
        arguments.

        Note: ``returnMappedCoords`` is not yet supported for this ROI type.
        """
    def addSegment(self, pos=(0, 0), scaleHandle: bool = False, connectTo: Incomplete | None = None) -> None:
        """
        Add a new segment to the ROI connecting from the previous endpoint to *pos*.
        (pos is specified in the parent coordinate system of the MultiRectROI)
        """
    def removeSegment(self, index: int = -1) -> None:
        """Remove a segment from the ROI."""

class MultiLineROI(MultiRectROI):
    def __init__(self, *args, **kwds) -> None: ...

class EllipseROI(ROI):
    """
    Elliptical ROI subclass with one scale handle and one rotation handle.


    ============== =============================================================
    **Arguments**
    pos            (length-2 sequence) The position of the ROI's origin.
    size           (length-2 sequence) The size of the ROI's bounding rectangle.
    \\**args        All extra keyword arguments are passed to ROI()
    ============== =============================================================

    """
    path: Incomplete
    def __init__(self, pos, size, **args) -> None: ...
    def paint(self, p, opt, widget) -> None: ...
    def getArrayRegion(self, arr, img: Incomplete | None = None, axes=(0, 1), returnMappedCoords: bool = False, **kwds):
        """
        Return the result of :meth:`~pyqtgraph.ROI.getArrayRegion` masked by the
        elliptical shape of the ROI. Regions outside the ellipse are set to 0.

        See :meth:`~pyqtgraph.ROI.getArrayRegion` for a description of the
        arguments.

        Note: ``returnMappedCoords`` is not yet supported for this ROI type.
        """
    def shape(self): ...

class CircleROI(EllipseROI):
    """
    Circular ROI subclass. Behaves exactly as EllipseROI, but may only be scaled
    proportionally to maintain its aspect ratio.

    ============== =============================================================
    **Arguments**
    pos            (length-2 sequence) The position of the ROI's origin.
    size           (length-2 sequence) The size of the ROI's bounding rectangle.
    \\**args        All extra keyword arguments are passed to ROI()
    ============== =============================================================

    """
    def __init__(self, pos, size: Incomplete | None = None, radius: Incomplete | None = None, **args) -> None: ...

class PolyLineROI(ROI):
    """
    Container class for multiple connected LineSegmentROIs.

    This class allows the user to draw paths of multiple line segments.

    ============== =============================================================
    **Arguments**
    positions      (list of length-2 sequences) The list of points in the path.
                   Note that, unlike the handle positions specified in other
                   ROIs, these positions must be expressed in the normal
                   coordinate system of the ROI, rather than (0 to 1) relative
                   to the size of the ROI.
    closed         (bool) if True, an extra LineSegmentROI is added connecting
                   the beginning and end points.
    \\**args        All extra keyword arguments are passed to ROI()
    ============== =============================================================

    """
    closed: Incomplete
    segments: Incomplete
    def __init__(self, positions, closed: bool = False, pos: Incomplete | None = None, **args) -> None: ...
    def setPoints(self, points, closed: Incomplete | None = None) -> None:
        """
        Set the complete sequence of points displayed by this ROI.

        ============= =========================================================
        **Arguments**
        points        List of (x,y) tuples specifying handle locations to set.
        closed        If bool, then this will set whether the ROI is closed
                      (the last point is connected to the first point). If
                      None, then the closed mode is left unchanged.
        ============= =========================================================

        """
    def clearPoints(self) -> None:
        """
        Remove all handles and segments.
        """
    def getState(self): ...
    def saveState(self): ...
    def setState(self, state) -> None: ...
    def addSegment(self, h1, h2, index: Incomplete | None = None) -> None: ...
    def setMouseHover(self, hover) -> None: ...
    def addHandle(self, info, index: Incomplete | None = None): ...
    def segmentClicked(self, segment, ev: Incomplete | None = None, pos: Incomplete | None = None) -> None: ...
    def removeHandle(self, handle, updateSegments: bool = True) -> None: ...
    def removeSegment(self, seg) -> None: ...
    def checkRemoveHandle(self, h): ...
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...
    def shape(self): ...
    def getArrayRegion(self, *args, **kwds): ...
    def setPen(self, *args, **kwds) -> None: ...

class LineSegmentROI(ROI):
    """
    ROI subclass with two freely-moving handles defining a line.

    ============== =============================================================
    **Arguments**
    positions      (list of two length-2 sequences) The endpoints of the line
                   segment. Note that, unlike the handle positions specified in
                   other ROIs, these positions must be expressed in the normal
                   coordinate system of the ROI, rather than (0 to 1) relative
                   to the size of the ROI.
    \\**args        All extra keyword arguments are passed to ROI()
    ============== =============================================================
    """
    def __init__(self, positions=(None, None), pos: Incomplete | None = None, handles=(None, None), **args) -> None: ...
    @property
    def endpoints(self): ...
    def listPoints(self): ...
    def getState(self): ...
    def saveState(self): ...
    def setState(self, state) -> None: ...
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...
    def shape(self): ...
    def getArrayRegion(self, data, img, axes=(0, 1), order: int = 1, returnMappedCoords: bool = False, **kwds):
        """
        Use the position of this ROI relative to an imageItem to pull a slice
        from an array.

        Since this pulls 1D data from a 2D coordinate system, the return value
        will have ndim = data.ndim-1

        See :meth:`~pyqtgraph.ROI.getArrayRegion` for a description of the
        arguments.
        """

class _PolyLineSegment(LineSegmentROI):
    def __init__(self, *args, **kwds) -> None: ...
    def setParentHover(self, hover) -> None: ...
    def hoverEvent(self, ev): ...

class CrosshairROI(ROI):
    """A crosshair ROI whose position is at the center of the crosshairs. By default, it is scalable, rotatable and translatable."""
    def __init__(self, pos: Incomplete | None = None, size: Incomplete | None = None, **kargs) -> None: ...
    def invalidate(self) -> None: ...
    def boundingRect(self): ...
    def shape(self): ...
    def paint(self, p, *args) -> None: ...

class RulerROI(LineSegmentROI):
    def paint(self, p, *args) -> None: ...
    def boundingRect(self): ...

class TriangleROI(ROI):
    """
    Equilateral triangle ROI subclass with one scale handle and one rotation handle.
    Arguments
    pos            (length-2 sequence) The position of the ROI's origin.
    size           (float) The length of an edge of the triangle.
    \\**args        All extra keyword arguments are passed to ROI()
    ============== =============================================================
    """
    poly: Incomplete
    def __init__(self, pos, size, **args) -> None: ...
    def paint(self, p, *args) -> None: ...
    path: Incomplete
    def shape(self): ...
    def getArrayRegion(self, *args, **kwds): ...
