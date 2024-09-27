from ...Qt import QtCore as QtCore, QtWidgets as QtWidgets
from ..ParameterItem import ParameterItem as ParameterItem
from .action import ParameterControlledButton as ParameterControlledButton
from .basetypes import GroupParameter as GroupParameter, GroupParameterItem as GroupParameterItem
from _typeshed import Incomplete

class ActionGroupParameterItem(GroupParameterItem):
    """
    Wraps a :class:`GroupParameterItem` to manage function parameters created by
    an interactor. Provies a button widget which mimics an ``action`` parameter.
    """
    itemWidget: Incomplete
    button: Incomplete
    def __init__(self, param, depth) -> None: ...
    def treeWidgetChanged(self) -> None: ...
    def optsChanged(self, param, opts) -> None: ...

class ActionGroupParameter(GroupParameter):
    itemClass = ActionGroupParameterItem
    sigActivated: Incomplete
    def __init__(self, **opts) -> None: ...
    def activate(self) -> None: ...
    def setButtonOpts(self, **opts) -> None:
        """
        Update individual button options without replacing the entire
        button definition.
        """

class ActionGroup(ActionGroupParameter):
    sigActivated: Incomplete
    def __init__(self, **opts) -> None: ...
    def activate(self) -> None: ...
