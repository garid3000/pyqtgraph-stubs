import pyqtgraph as pg
from _typeshed import Incomplete
from pyqtgraph.Qt import QtCore as QtCore, QtWidgets as QtWidgets
from pyqtgraph.graphicsItems.ScatterPlotItem import name_list as name_list
from pyqtgraph.parametertree import Parameter as Parameter, ParameterTree as ParameterTree, interact as interact

rng: Incomplete

def sortedRandint(low, high, size): ...
def isNoneOrScalar(value): ...

values: Incomplete

def next_plot(xtype: str = 'random', ytype: str = 'random', symbol: str = 'o', symbolBrush: str = '#f00') -> None: ...

cmap: Incomplete
widget: Incomplete
pltItem: pg.PlotItem
xytype: Incomplete
topParam: Incomplete
tree: Incomplete
textbox: Incomplete
win: Incomplete
