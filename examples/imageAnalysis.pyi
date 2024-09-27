from _typeshed import Incomplete
from pyqtgraph.Qt import QtGui as QtGui

win: Incomplete
p1: Incomplete
img: Incomplete
roi: Incomplete
iso: Incomplete
hist: Incomplete
isoLine: Incomplete
p2: Incomplete
data: Incomplete
tr: Incomplete

def updatePlot() -> None: ...
def updateIsocurve() -> None: ...
def imageHoverEvent(event) -> None:
    """Show the position, pixel, and value under the mouse cursor.
    """
