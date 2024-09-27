from ...Qt import QtWidgets as QtWidgets
from .basetypes import WidgetParameterItem as WidgetParameterItem

class BoolParameterItem(WidgetParameterItem):
    """
    Registered parameter type which displays a QCheckBox
    """
    hideWidget: bool
    def makeWidget(self): ...
