from . import SRTTransform as SRTTransform
from .Qt import QtGui as QtGui
from .Transform3D import Transform3D as Transform3D
from .Vector import Vector as Vector
from _typeshed import Incomplete

class SRTTransform3D(Transform3D):
    """4x4 Transform matrix that can always be represented as a combination of 3 matrices: scale * rotate * translate
    This transform has no shear; angles are always preserved.
    """
    def __init__(self, init: Incomplete | None = None) -> None: ...
    def getScale(self): ...
    def getRotation(self):
        """Return (angle, axis) of rotation"""
    def getTranslation(self): ...
    def reset(self) -> None: ...
    def translate(self, *args) -> None:
        """Adjust the translation of this transform"""
    def setTranslate(self, *args) -> None:
        """Set the translation of this transform"""
    def scale(self, *args) -> None:
        """adjust the scale of this transform"""
    def setScale(self, *args) -> None:
        """Set the scale of this transform"""
    def rotate(self, angle, axis=(0, 0, 1)) -> None:
        """Adjust the rotation of this transform"""
    def setRotate(self, angle, axis=(0, 0, 1)) -> None:
        """Set the transformation rotation to angle (in degrees)"""
    def setFromMatrix(self, m) -> None:
        """
        Set this transform based on the elements of *m*
        The input matrix must be affine AND have no shear,
        otherwise the conversion will most likely fail.
        """
    def as2D(self):
        """Return a QTransform representing the x,y portion of this transform (if possible)"""
    def saveState(self): ...
    def restoreState(self, state) -> None: ...
    def update(self) -> None: ...
    def matrix(self, nd: int = 3): ...
    def __reduce__(self): ...
