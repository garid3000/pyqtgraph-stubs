from . import SRTTransform3D as SRTTransform3D
from .Point import Point as Point
from .Qt import QtGui as QtGui
from _typeshed import Incomplete

class SRTTransform(QtGui.QTransform):
    """Transform that can always be represented as a combination of 3 matrices: scale * rotate * translate
    This transform has no shear; angles are always preserved.
    """
    def __init__(self, init: Incomplete | None = None) -> None: ...
    def getScale(self): ...
    def getRotation(self): ...
    def getTranslation(self): ...
    def reset(self) -> None: ...
    def setFromQTransform(self, tr) -> None: ...
    def setFromMatrix4x4(self, m) -> None: ...
    def translate(self, *args) -> None:
        """Acceptable arguments are: 
           x, y
           [x, y]
           Point(x,y)"""
    def setTranslate(self, *args) -> None:
        """Acceptable arguments are: 
           x, y
           [x, y]
           Point(x,y)"""
    def scale(self, *args) -> None:
        """Acceptable arguments are: 
           x, y
           [x, y]
           Point(x,y)"""
    def setScale(self, *args) -> None:
        """Acceptable arguments are: 
           x, y
           [x, y]
           Point(x,y)"""
    def rotate(self, angle) -> None:
        """Rotate the transformation by angle (in degrees)"""
    def setRotate(self, angle) -> None:
        """Set the transformation rotation to angle (in degrees)"""
    def __truediv__(self, t):
        """A / B  ==  B^-1 * A"""
    def __div__(self, t): ...
    def __mul__(self, t): ...
    def saveState(self): ...
    def __reduce__(self): ...
    def restoreState(self, state) -> None: ...
    def update(self) -> None: ...
    def matrix(self): ...
