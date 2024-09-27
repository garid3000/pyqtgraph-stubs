from OpenGL.GL import *
from .. import Vector as Vector, getConfigOption as getConfigOption
from ..Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from _typeshed import Incomplete

class GLViewMixin:
    opts: Incomplete
    items: Incomplete
    noRepeatKeys: Incomplete
    keysPressed: Incomplete
    keyTimer: Incomplete
    def __init__(self, *args, rotationMethod: str = 'euler', **kwargs) -> None:
        """
        Mixin class providing functionality for GLViewWidget

        ================ ==============================================================
        **Arguments:**
        rotationMethod   (str): Mechanism to drive the rotation method, options are
                         'euler' and 'quaternion'. Defaults to 'euler'.
        ================ ==============================================================
        """
    def deviceWidth(self): ...
    def deviceHeight(self): ...
    def reset(self) -> None:
        """
        Initialize the widget state or reset the current state to the original state.
        """
    def addItem(self, item) -> None: ...
    def removeItem(self, item) -> None:
        """
        Remove the item from the scene.
        """
    def clear(self) -> None:
        """
        Remove all items from the scene.
        """
    def initializeGL(self) -> None:
        """
        Initialize items that were not initialized during addItem().
        """
    def setBackgroundColor(self, *args, **kwds) -> None:
        """
        Set the background color of the widget. Accepts the same arguments as
        :func:`~pyqtgraph.mkColor`.
        """
    def getViewport(self): ...
    def setProjection(self, region: Incomplete | None = None) -> None: ...
    def projectionMatrix(self, region: Incomplete | None = None): ...
    def setModelview(self) -> None: ...
    def viewMatrix(self): ...
    def itemsAt(self, region: Incomplete | None = None):
        """
        Return a list of the items displayed in the region (x, y, w, h)
        relative to the widget.        
        """
    def paintGL(self, region: Incomplete | None = None, viewport: Incomplete | None = None, useItemNames: bool = False) -> None:
        """
        viewport specifies the arguments to glViewport. If None, then we use self.opts['viewport']
        region specifies the sub-region of self.opts['viewport'] that should be rendered.
        Note that we may use viewport != self.opts['viewport'] when exporting.
        """
    def drawItemTree(self, item: Incomplete | None = None, useItemNames: bool = False): ...
    def setCameraPosition(self, pos: Incomplete | None = None, distance: Incomplete | None = None, elevation: Incomplete | None = None, azimuth: Incomplete | None = None, rotation: Incomplete | None = None) -> None: ...
    def cameraPosition(self):
        """Return current position of camera based on center, dist, elevation, and azimuth"""
    def setCameraParams(self, **kwds) -> None: ...
    def cameraParams(self): ...
    def orbit(self, azim, elev) -> None:
        """Orbits the camera around the center position. *azim* and *elev* are given in degrees."""
    def pan(self, dx, dy, dz, relative: str = 'global') -> None:
        '''
        Moves the center (look-at) position while holding the camera in place. 
        
        ==============  =======================================================
        **Arguments:**
        *dx*            Distance to pan in x direction
        *dy*            Distance to pan in y direction
        *dz*            Distance to pan in z direction
        *relative*      String that determines the direction of dx,dy,dz. 
                        If "global", then the global coordinate system is used.
                        If "view", then the z axis is aligned with the view
                        direction, and x and y axes are in the plane of the
                        view: +x points right, +y points up. 
                        If "view-upright", then x is in the global xy plane and
                        points to the right side of the view, y is in the
                        global xy plane and orthogonal to x, and z points in
                        the global z direction.
        ==============  =======================================================
        
        Distances are scaled roughly such that a value of 1.0 moves
        by one pixel on screen.
        '''
    def pixelSize(self, pos):
        """
        Return the approximate size of a screen pixel at the location pos
        Pos may be a Vector or an (N,3) array of locations
        """
    mousePos: Incomplete
    def mousePressEvent(self, ev) -> None: ...
    def mouseMoveEvent(self, ev) -> None: ...
    def mouseReleaseEvent(self, ev) -> None: ...
    def wheelEvent(self, ev) -> None: ...
    def keyPressEvent(self, ev) -> None: ...
    def keyReleaseEvent(self, ev) -> None: ...
    def evalKeyState(self) -> None: ...
    def readQImage(self):
        """
        Read the current buffer pixels out as a QImage.
        """
    def renderToArray(self, size, format=..., type=..., textureSize: int = 1024, padding: int = 256): ...

class GLViewWidget(GLViewMixin, QtWidgets.QOpenGLWidget):
    def __init__(self, *args, devicePixelRatio: Incomplete | None = None, **kwargs) -> None:
        """
        Basic widget for displaying 3D data
          - Rotation/scale controls
          - Axis/grid display
          - Export options

        ================ ==============================================================
        **Arguments:**
        parent           (QObject, optional): Parent QObject. Defaults to None.
        devicePixelRatio No longer in use. High-DPI displays should automatically
                         detect the correct resolution.
        rotationMethod   (str): Mechanism to drive the rotation method, options are
                         'euler' and 'quaternion'. Defaults to 'euler'.
        ================ ==============================================================
        """
