from ...Qt import QtGui as QtGui, QtWidgets as QtWidgets
from ..Parameter import Parameter as Parameter
from .basetypes import WidgetParameterItem as WidgetParameterItem
from _typeshed import Incomplete

class FontParameterItem(WidgetParameterItem):
    hideWidget: bool
    def makeWidget(self): ...
    def updateDisplayLabel(self, value: Incomplete | None = None) -> None: ...

class FontParameter(Parameter):
    """
    Creates and controls a QFont value. Be careful when selecting options from the font dropdown. since not all
    fonts are available on all systems
    """
    itemClass = FontParameterItem
    def saveState(self, filter: Incomplete | None = None): ...
