from ...Qt import QtWidgets as QtWidgets
from ..Parameter import Parameter as Parameter
from .basetypes import WidgetParameterItem as WidgetParameterItem
from _typeshed import Incomplete

class ListParameterItem(WidgetParameterItem):
    """
    WidgetParameterItem subclass providing comboBox that lets the user select from a list of options.

    """
    targetValue: Incomplete
    def __init__(self, param, depth) -> None: ...
    widget: Incomplete
    def makeWidget(self): ...
    def value(self): ...
    def setValue(self, val) -> None: ...
    def limitsChanged(self, param, limits) -> None: ...
    def updateDisplayLabel(self, value: Incomplete | None = None) -> None: ...

class ListParameter(Parameter):
    """Parameter with a list of acceptable values.

    By default, this parameter is represtented by a :class:`ListParameterItem`,
    displaying a combo box to select a value from the list.

    In addition to the generic :class:`~pyqtgraph.parametertree.Parameter`
    options, this parameter type accepts a ``limits`` argument specifying the
    list of allowed values.

    The values may generally be of any data type, as long as they can be
    represented as a string. If the string representation provided is
    undesirable, the values may be given as a dictionary mapping the desired
    string representation to the value.
    """
    itemClass = ListParameterItem
    forward: Incomplete
    reverse: Incomplete
    def __init__(self, **opts) -> None: ...
    def setLimits(self, limits) -> None:
        """Change the list of allowed values."""
    @staticmethod
    def mapping(limits): ...
