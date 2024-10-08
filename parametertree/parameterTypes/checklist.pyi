from . import BoolParameterItem as BoolParameterItem, SimpleParameter as SimpleParameter
from ...Qt import QtWidgets as QtWidgets
from ...SignalProxy import SignalProxy as SignalProxy
from ..ParameterItem import ParameterItem as ParameterItem
from .basetypes import Emitter as Emitter, GroupParameter as GroupParameter, GroupParameterItem as GroupParameterItem, WidgetParameterItem as WidgetParameterItem
from .list import ListParameter as ListParameter
from _typeshed import Incomplete

class ChecklistParameterItem(GroupParameterItem):
    """
    Wraps a :class:`GroupParameterItem` to manage ``bool`` parameter children. Also provides convenience buttons to
    select or clear all values at once. Note these conveniences are disabled when ``exclusive`` is *True*.
    """
    btnGrp: Incomplete
    def __init__(self, param, depth) -> None: ...
    def treeWidgetChanged(self) -> None: ...
    def selectAllClicked(self) -> None: ...
    def clearAllClicked(self) -> None: ...
    def insertChild(self, pos, item): ...
    def addChild(self, item): ...
    def takeChild(self, i) -> None: ...
    def optsChanged(self, param, opts) -> None: ...
    def expandedChangedEvent(self, expanded) -> None: ...
    def valueChanged(self, param, val) -> None: ...
    def updateDefaultBtn(self) -> None: ...
    makeDefaultButton: Incomplete
    defaultClicked: Incomplete

class RadioParameterItem(BoolParameterItem):
    """
    Allows radio buttons to function as booleans when `exclusive` is *True*
    """
    emitter: Incomplete
    def __init__(self, param, depth) -> None: ...
    hideWidget: bool
    def makeWidget(self): ...
    def maybeSigChanged(self, val) -> None:
        '''
        Make sure to only activate on a "true" value, since an exclusive button group fires once to deactivate
        the old option and once to activate the new selection
        '''

class BoolOrRadioParameter(SimpleParameter):
    @property
    def itemClass(self): ...

class ChecklistParameter(GroupParameter):
    '''
    Can be set just like a :class:`ListParameter`, but allows for multiple values to be selected simultaneously.

    ============== ========================================================
    **Options**
    exclusive      When *False*, any number of options can be selected. The resulting ``value()`` is a list of
                   all checked values. When *True*, it behaves like a ``list`` type -- only one value can be selected.
                   If no values are selected and ``exclusive`` is set to *True*, the first available limit is selected.
                   The return value of an ``exclusive`` checklist is a single value rather than a list with one element.
    delay          Controls the wait time between editing the checkboxes/radio button children and firing a "value changed"
                   signal. This allows users to edit multiple boxes at once for a single value update.
    ============== ========================================================
    '''
    itemClass = ChecklistParameterItem
    targetValue: Incomplete
    valChangingProxy: Incomplete
    def __init__(self, **opts) -> None: ...
    def childrenValue(self): ...
    def updateLimits(self, _param, limits) -> None: ...
    def optsChanged(self, param, opts) -> None: ...
    def setValue(self, value, blockSignal: Incomplete | None = None) -> None: ...
    def setToDefault(self) -> None: ...
    def saveState(self, filter: Incomplete | None = None): ...
    def restoreState(self, state, recursive: bool = True, addChildren: bool = True, removeChildren: bool = True, blockSignals: bool = True): ...
