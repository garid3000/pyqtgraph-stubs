from ..Qt import QtCore, QtWidgets
from .PlotCurveItem import PlotCurveItem
from .PlotDataItem import PlotDataItem
from _typeshed import Incomplete

__all__ = ['FillBetweenItem']

class FillBetweenItem(QtWidgets.QGraphicsPathItem):
    """
    GraphicsItem filling the space between two PlotDataItems.
    """
    curves: Incomplete
    def __init__(self, curve1: PlotDataItem | PlotCurveItem, curve2: PlotDataItem | PlotCurveItem, brush: Incomplete | None = None, pen: Incomplete | None = None, fillRule: QtCore.Qt.FillRule = ...) -> None:
        """FillBetweenItem fills a region between two curves with a specified
        :class:`~QtGui.QBrush`. 

        Parameters
        ----------
        curve1 : :class:`~pyqtgraph.PlotDataItem` | :class:`~pyqtgraph.PlotCurveItem`
            Line to draw fill from
        curve2 : :class:`~pyqtgraph.PlotDataItem` | :class:`~pyqtgraph.PlotCurveItem`
            Line to draw fill to
        brush : color_like, optional
            Arguments accepted by :func:`~pyqtgraph.mkBrush`, used
            to create the :class:`~QtGui.QBrush` instance used to draw the item
            by default None
        pen : color_like, optional
            Arguments accepted by :func:`~pyqtgraph.mkColor`, used
            to create the :class:`~QtGui.QPen` instance used to draw the item
            by default ``None``
        fillRule : QtCore.Qt.FillRule, optional
            FillRule to be applied to the underlying :class:`~QtGui.QPainterPath`
            instance, by default ``QtCore.Qt.FillRule.OddEvenFill``

        Raises
        ------
        ValueError
            Raised when ``None`` is passed in as either ``curve1``
            or ``curve2``
        TypeError
            Raised when either ``curve1`` or ``curve2`` is not either
            :class:`~pyqtgraph.PlotDataItem` or :class:`~pyqtgraph.PlotCurveItem`
        """
    def fillRule(self): ...
    def setFillRule(self, fillRule: QtCore.Qt.FillRule = ...):
        """Set the underlying :class:`~QtGui.QPainterPath` to the specified 
        :class:`~QtCore.Qt.FillRule`

        This can be useful for allowing in the filling of voids.

        Parameters
        ----------
        fillRule : QtCore.Qt.FillRule
            A member of the :class:`~QtCore.Qt.FillRule` enum
        """
    def setBrush(self, *args, **kwds) -> None:
        """Change the fill brush. Accepts the same arguments as :func:`~pyqtgraph.mkBrush`
        """
    def setPen(self, *args, **kwds) -> None:
        """Change the fill pen. Accepts the same arguments as :func:`~pyqtgraph.mkColor`
        """
    def setCurves(self, curve1: PlotDataItem | PlotCurveItem, curve2: PlotDataItem | PlotCurveItem):
        """Method to set the Curves to draw the FillBetweenItem between

        Parameters
        ----------
        curve1 : :class:`~pyqtgraph.PlotDataItem` | :class:`~pyqtgraph.PlotCurveItem`
            Line to draw fill from
        curve2 : :class:`~pyqtgraph.PlotDataItem` | :class:`~pyqtgraph.PlotCurveItem`
            Line to draw fill to
    
        Raises
        ------
        TypeError
            Raised when input arguments are not either :class:`~pyqtgraph.PlotDataItem` or
            :class:`~pyqtgraph.PlotCurveItem`
        """
    def curveChanged(self) -> None: ...
    def updatePath(self) -> None: ...
