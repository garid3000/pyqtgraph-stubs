from ...Qt import QtCore as QtCore, QtWidgets as QtWidgets
from ..Parameter import Parameter as Parameter
from .basetypes import WidgetParameterItem as WidgetParameterItem
from _typeshed import Incomplete

class TextParameterItem(WidgetParameterItem):
    """ParameterItem displaying a QTextEdit widget."""
    hideWidget: bool
    asSubItem: bool
    textBox: Incomplete
    def makeWidget(self): ...

class TextParameter(Parameter):
    """Editable string, displayed as large text box in the tree."""
    itemClass = TextParameterItem
