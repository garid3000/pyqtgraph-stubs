from ...Qt import QtWidgets as QtWidgets
from ..Parameter import Parameter as Parameter
from .basetypes import WidgetParameterItem as WidgetParameterItem

class ProgressBarParameterItem(WidgetParameterItem):
    hideWidget: bool
    def makeWidget(self): ...

class ProgressBarParameter(Parameter):
    """
    Displays a progress bar whose value can be set between 0 and 100
    """
    itemClass = ProgressBarParameterItem
