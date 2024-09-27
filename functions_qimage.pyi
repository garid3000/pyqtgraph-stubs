from . import functions as functions
from .Qt import QtGui as QtGui
from .util.cupy_helper import getCupy as getCupy
from .util.numba_helper import getNumbaFunctions as getNumbaFunctions
from _typeshed import Incomplete

def try_make_qimage(image, *, levels, lut, transparentLocations: Incomplete | None = None):
    """
    Internal function to make an QImage from an ndarray without going
    through the full generality of makeARGB().
    Only certain combinations of input arguments are supported.
    """
