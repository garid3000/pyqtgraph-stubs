from . import GroupParameterItem as GroupParameterItem, WidgetParameterItem as WidgetParameterItem
from ...Qt import QtCore as QtCore, QtWidgets as QtWidgets
from ...SignalProxy import SignalProxy as SignalProxy
from ...widgets.PenPreviewLabel import PenPreviewLabel as PenPreviewLabel
from .basetypes import GroupParameter as GroupParameter, Parameter as Parameter, ParameterItem as ParameterItem
from .qtenum import QtEnumParameter as QtEnumParameter
from _typeshed import Incomplete

class PenParameterItem(GroupParameterItem):
    defaultBtn: Incomplete
    itemWidget: Incomplete
    penLabel: Incomplete
    def __init__(self, param, depth) -> None: ...
    def optsChanged(self, param, opts) -> None: ...
    def treeWidgetChanged(self) -> None: ...
    defaultClicked: Incomplete
    makeDefaultButton: Incomplete
    def valueChanged(self, param, val) -> None: ...
    def updateDefaultBtn(self) -> None: ...

def cap_first(s: str): ...

class PenParameter(GroupParameter):
    """
    Controls the appearance of a QPen value.

    When `saveState` is called, the value is encoded as (color, width, style, capStyle, joinStyle, cosmetic)

    ============== ========================================================
    **Options:**
    color          pen color, can be any argument accepted by :func:`~pyqtgraph.mkColor` (defaults to black)
    width          integer width >= 0 (defaults to 1)
    style          String version of QPenStyle enum, i.e. 'SolidLine' (default), 'DashLine', etc.
    capStyle       String version of QPenCapStyle enum, i.e. 'SquareCap' (default), 'RoundCap', etc.
    joinStyle      String version of QPenJoinStyle enum, i.e. 'BevelJoin' (default), 'RoundJoin', etc.
    cosmetic       Boolean, whether or not the pen is cosmetic (defaults to True)
    ============== ========================================================
    """
    itemClass = PenParameterItem
    pen: Incomplete
    valChangingProxy: Incomplete
    def __init__(self, **opts) -> None: ...
    def setDefault(self, val, **kwargs): ...
    def saveState(self, filter: Incomplete | None = None): ...
    def restoreState(self, state, recursive: bool = True, addChildren: bool = True, removeChildren: bool = True, blockSignals: bool = True): ...
    def setValue(self, value, blockSignal: Incomplete | None = None): ...
    def applyOptsToPen(self, **opts): ...
    def setOpts(self, **opts): ...
    def mkPen(self, *args, **kwargs):
        """Thin wrapper around fn.mkPen which accepts the serialized state from saveState"""
    def penPropertySetter(self, p, value) -> None: ...
    @staticmethod
    def updateFromPen(param, pen) -> None:
        """
        Applies settings from a pen to either a Parameter or dict. The Parameter or dict must already
        be populated with the relevant keys that can be found in `PenSelectorDialog.mkParam`.
        """
