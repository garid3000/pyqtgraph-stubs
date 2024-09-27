from ..Qt import QtWidgets
from _typeshed import Incomplete


__all__ = ['GraphicsView']

class GraphicsView(QtWidgets.QGraphicsView):
    """Re-implementation of QGraphicsView that removes scrollbars and allows unambiguous control of the
    viewed coordinate range. Also automatically creates a GraphicsScene and a central QGraphicsWidget
    that is automatically scaled to the full view geometry.

    This widget is the basis for :class:`PlotWidget <pyqtgraph.PlotWidget>`,
    :class:`GraphicsLayoutWidget <pyqtgraph.GraphicsLayoutWidget>`, and the view widget in
    :class:`ImageView <pyqtgraph.ImageView>`.

    By default, the view coordinate system matches the widget's pixel coordinates and
    automatically updates when the view is resized. This can be overridden by setting
    autoPixelRange=False. The exact visible range can be set with setRange().
The view can be panned using the middle mouse button and scaled using the right mouse button if enabled via enableMouse()  (but ordinarily, we use ViewBox for this functionality)."""
    sigDeviceRangeChanged: Incomplete
    sigDeviceTransformChanged: Incomplete
    sigMouseReleased: Incomplete
    sigSceneMouseMoved: Incomplete
    sigScaleChanged: Incomplete
    lastFileDir: Incomplete
    closed: bool
    lockedViewports: Incomplete
    lastMousePos: Incomplete
    aspectLocked: bool
    range: Incomplete
    autoPixelRange: bool
    currentItem: Incomplete
    sceneObj: Incomplete
    centralWidget: Incomplete
    centralLayout: Incomplete
    mouseEnabled: bool
    scaleCenter: bool
    clickAccepted: bool
    def __init__(self, parent: Incomplete | None = None, useOpenGL: Incomplete | None = None, background: str = 'default') -> None:
        """
        ==============  ============================================================
        **Arguments:**
        parent          Optional parent widget
        useOpenGL       If True, the GraphicsView will use OpenGL to do all of its
                        rendering. This can improve performance on some systems,
                        but may also introduce bugs (the combination of
                        QGraphicsView and QOpenGLWidget is still an 'experimental'
                        feature of Qt)
        background      Set the background color of the GraphicsView. Accepts any
                        single argument accepted by
                        :func:`mkColor <pyqtgraph.mkColor>`. By
                        default, the background color is determined using the
                        'backgroundColor' configuration option (see
                        :func:`setConfigOptions <pyqtgraph.setConfigOptions>`).
        ==============  ============================================================
        """
    def setAntialiasing(self, aa) -> None:
        """Enable or disable default antialiasing.
        Note that this will only affect items that do not specify their own antialiasing options."""
    def setBackground(self, background) -> None:
        """
        Set the background color of the GraphicsView.
        To use the defaults specified py pyqtgraph.setConfigOption, use background='default'.
        To make the background transparent, use background=None.
        """
    def paintEvent(self, ev): ...
    def render(self, *args, **kwds): ...
    def close(self) -> None: ...
    def useOpenGL(self, b: bool = True) -> None: ...
    def keyPressEvent(self, ev) -> None: ...
    def setCentralItem(self, item): ...
    def setCentralWidget(self, item) -> None:
        """Sets a QGraphicsWidget to automatically fill the entire view (the item will be automatically
        resize whenever the GraphicsView is resized)."""
    def addItem(self, *args: QtWidgets.QGraphicsItem | None ) -> None : ...
    def removeItem(self, *args): ...
    def enableMouse(self, b: bool = True) -> None: ...
    mouseTrail: Incomplete
    lastButtonReleased: Incomplete
    def clearMouse(self) -> None: ...
    def resizeEvent(self, ev) -> None: ...
    def updateMatrix(self, propagate: bool = True) -> None: ...
    def viewRect(self):
        """Return the boundaries of the view in scene coordinates"""
    def visibleRange(self): ...
    def translate(self, dx, dy) -> None: ...
    def scale(self, sx, sy, center: Incomplete | None = None) -> None: ...
    def setRange(self, newRect: Incomplete | None = None, padding: float = 0.05, lockAspect: Incomplete | None = None, propagate: bool = True, disableAutoPixel: bool = True) -> None: ...
    def scaleToImage(self, image) -> None:
        """Scales such that pixels in image are the same size as screen pixels. This may result in a significant performance increase."""
    def lockXRange(self, v1) -> None: ...
    def setXRange(self, r, padding: float = 0.05) -> None: ...
    def setYRange(self, r, padding: float = 0.05) -> None: ...
    def wheelEvent(self, ev) -> None: ...
    def setAspectLocked(self, s) -> None: ...
    def leaveEvent(self, ev) -> None: ...
    mousePressPos: Incomplete
    def mousePressEvent(self, ev) -> None: ...
    def mouseReleaseEvent(self, ev) -> None: ...
    def mouseMoveEvent(self, ev) -> None: ...
    def pixelSize(self):
        """Return vector with the length and width of one view pixel in scene coordinates"""
    def dragEnterEvent(self, ev) -> None: ...
