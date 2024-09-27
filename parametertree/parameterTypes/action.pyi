from ...Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from ..Parameter import Parameter as Parameter
from ..ParameterItem import ParameterItem as ParameterItem
from _typeshed import Incomplete

class ParameterControlledButton(QtWidgets.QPushButton):
    settableAttributes: Incomplete
    def __init__(self, parameter: Incomplete | None = None, parent: Incomplete | None = None) -> None: ...
    def updateOpts(self, param, opts) -> None: ...
    def onNameChange(self, param, name) -> None: ...

class ActionParameterItem(ParameterItem):
    """ParameterItem displaying a clickable button."""
    layoutWidget: Incomplete
    layout: Incomplete
    button: Incomplete
    def __init__(self, param, depth) -> None: ...
    def treeWidgetChanged(self) -> None: ...
    def titleChanged(self) -> None: ...

class ActionParameter(Parameter):
    """
    Used for displaying a button within the tree.

    ``sigActivated(self)`` is emitted when the button is clicked.

    Parameters
    ----------
    icon: str
        Icon to display in the button. Can be any argument accepted
        by :class:`QIcon <QtGui.QIcon>`.
    shortcut: str
        Key sequence to use as a shortcut for the button. Note that this shortcut is
        associated with spawned parameters, i.e. the shortcut will only work when this
        parameter has an item in a tree that is visible. Can be set to any string
        accepted by :class:`QKeySequence <QtGui.QKeySequence>`.
    """
    itemClass = ActionParameterItem
    sigActivated: Incomplete
    def activate(self) -> None: ...
