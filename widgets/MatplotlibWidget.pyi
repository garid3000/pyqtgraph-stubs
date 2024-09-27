import typing
from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['MatplotlibWidget']

class MatplotlibWidget(QtWidgets.QWidget):
    """
    Implements a Matplotlib figure inside a QWidget.
    Use getFigure() and redraw() to interact with matplotlib.

    Example::

        mw = MatplotlibWidget()
        subplot = mw.getFigure().add_subplot(111)
        subplot.plot(x,y)
        mw.draw()
    """
    parent_default: Incomplete
    figsize_default: Incomplete
    dpi_default: int
    @typing.overload
    def __init__(self, figsize=(5.0, 4.0), dpi: int = 100, parent: Incomplete | None = None) -> None: ...
    @typing.overload
    def __init__(self, parent: Incomplete | None = None, figsize=(5.0, 4.0), dpi: int = 100) -> None: ...
    def getFigure(self): ...
    def draw(self) -> None: ...
