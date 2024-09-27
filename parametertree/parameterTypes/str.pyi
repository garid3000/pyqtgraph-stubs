from ...Qt import QtWidgets as QtWidgets
from .basetypes import WidgetParameterItem as WidgetParameterItem

class StrParameterItem(WidgetParameterItem):
    """Registered parameter type which displays a QLineEdit"""
    def makeWidget(self): ...
