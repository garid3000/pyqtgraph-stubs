from .Qt import QtCore as QtCore

class Point(QtCore.QPointF):
    """Extension of QPointF which adds a few missing methods."""
    def __init__(self, *args) -> None: ...
    def __len__(self) -> int: ...
    def __reduce__(self): ...
    def __getitem__(self, i): ...
    def __iter__(self): ...
    def __setitem__(self, i, x) -> None: ...
    def __radd__(self, a): ...
    def __add__(self, a): ...
    def __rsub__(self, a): ...
    def __sub__(self, a): ...
    def __rmul__(self, a): ...
    def __mul__(self, a): ...
    def __rdiv__(self, a): ...
    def __div__(self, a): ...
    def __truediv__(self, a): ...
    def __rtruediv__(self, a): ...
    def __rpow__(self, a): ...
    def __pow__(self, a): ...
    def length(self):
        """Returns the vector length of this Point."""
    def norm(self):
        """Returns a vector in the same direction with unit length."""
    def angle(self, a, units: str = 'degrees'):
        '''
        Returns the angle in degrees from the vector a to self.
        
        Parameters
        ----------
        a : Point, QPointF or QPoint
            The Point to return the angle with
        units : str, optional
            The units with which to compute the angle with, "degrees" or "radians",
            default "degrees"
        
        Returns
        -------
        float
            The angle between two vectors
        '''
    def dot(self, a):
        """Returns the dot product of a and this Point."""
    def cross(self, a):
        """Returns the cross product of a and this Point"""
    def proj(self, b):
        """Return the projection of this vector onto the vector b"""
    def min(self): ...
    def max(self): ...
    def copy(self): ...
    def toQPoint(self): ...
