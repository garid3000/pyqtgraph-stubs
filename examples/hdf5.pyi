import pyqtgraph as pg
from _typeshed import Incomplete
from pyqtgraph.Qt import QtWidgets as QtWidgets

plt: Incomplete

class HDF5Plot(pg.PlotCurveItem):
    hdf5: Incomplete
    limit: int
    def __init__(self, *args, **kwds) -> None: ...
    def setHDF5(self, data) -> None: ...
    def viewRangeChanged(self) -> None: ...
    def updateHDF5Plot(self) -> None: ...

def createFile(finalSize: int = 2000000000) -> None:
    """Create a large HDF5 data file for testing.
    Data consists of 1M random samples tiled through the end of the array.
    """

fileName: Incomplete
size: Incomplete
ok: Incomplete
f: Incomplete
curve: Incomplete
