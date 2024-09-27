from .Qt import QT_LIB as QT_LIB, QtCore as QtCore, QtGui as QtGui

class Vector(QtGui.QVector3D):
    """Extension of QVector3D which adds a few helpful methods."""
    def __init__(self, *args) -> None:
        """
        Handle additional constructions of a Vector

        ==============  ================================================================================================
        **Arguments:**
        *args*          Could be any of:

                         * 3 numerics (x, y, and z)
                         * 2 numerics (x, y, and `0` assumed for z)
                         * Either of the previous in a list-like collection
                         * 1 QSizeF (`0` assumed for z)
                         * 1 QPointF (`0` assumed for z)
                         * Any other valid QVector3D init args.
        ==============  ================================================================================================
        """
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __setitem__(self, i, x) -> None: ...
    def __iter__(self): ...
    def angle(self, a):
        """Returns the angle in degrees between this vector and the vector a."""
    def __abs__(self): ...
