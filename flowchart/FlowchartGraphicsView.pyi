from ..Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from ..graphicsItems.ViewBox import ViewBox as ViewBox
from ..widgets.GraphicsView import GraphicsView as GraphicsView
from _typeshed import Incomplete

translate: Incomplete

class FlowchartGraphicsView(GraphicsView):
    sigHoverOver: Incomplete
    sigClicked: Incomplete
    def __init__(self, widget, *args) -> None: ...
    def viewBox(self): ...

class FlowchartViewBox(ViewBox):
    widget: Incomplete
    def __init__(self, widget, *args, **kwargs) -> None: ...
    def getMenu(self, ev): ...
    def getContextMenus(self, ev): ...
