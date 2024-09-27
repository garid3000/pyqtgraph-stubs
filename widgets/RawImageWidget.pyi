from OpenGL.GL import *
from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['RawImageWidget', 'RawImageGLWidget']

class RawImageWidget(QtWidgets.QWidget):
    """
    Widget optimized for very fast video display.
    Generally using an ImageItem inside GraphicsView is fast enough.
    On some systems this may provide faster video. See the VideoSpeedTest example for benchmarking.
    """
    scaled: Incomplete
    opts: Incomplete
    image: Incomplete
    def __init__(self, parent: Incomplete | None = None, scaled: bool = False) -> None:
        """
        Setting scaled=True will cause the entire image to be displayed within the boundaries of the widget.
        This also greatly reduces the speed at which it will draw frames.
        """
    def setImage(self, img, *args, **kargs) -> None:
        """
        img must be ndarray of shape (x,y), (x,y,3), or (x,y,4).
        Extra arguments are sent to functions.makeARGB
        """
    def paintEvent(self, ev) -> None: ...

class RawImageGLWidget(QOpenGLWidget):
    """
        Similar to RawImageWidget, but uses a GL widget to do all drawing.
        Performance varies between platforms; see examples/VideoSpeedTest for benchmarking.

        Checks if setConfigOptions(imageAxisOrder='row-major') was set.
        """
    scaled: Incomplete
    image: Incomplete
    uploaded: bool
    smooth: bool
    opts: Incomplete
    def __init__(self, parent: Incomplete | None = None, scaled: bool = False) -> None: ...
    def setImage(self, img, *args, **kargs) -> None:
        """
            img must be ndarray of shape (x,y), (x,y,3), or (x,y,4).
            Extra arguments are sent to functions.makeARGB
            """
    texture: Incomplete
    def initializeGL(self) -> None: ...
    def uploadTexture(self) -> None: ...
    def paintGL(self) -> None: ...
