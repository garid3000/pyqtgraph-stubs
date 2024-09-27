from .Qt import QtGui as QtGui
from .Vector import Vector as Vector

class Transform3D(QtGui.QMatrix4x4):
    """
    Extension of QMatrix4x4 with some helpful methods added.
    """
    def __init__(self, *args) -> None: ...
    def matrix(self, nd: int = 3): ...
    def map(self, obj):
        """
        Extends QMatrix4x4.map() to allow mapping (3, ...) arrays of coordinates
        """
    def inverted(self): ...
