from ...Qt import QT_LIB as QT_LIB, QtCore as QtCore
from .list import ListParameter as ListParameter
from _typeshed import Incomplete

class QtEnumParameter(ListParameter):
    enum: Incomplete
    searchObj: Incomplete
    enumMap: Incomplete
    def __init__(self, enum, searchObj=..., **opts) -> None:
        """
        Constructs a list of allowed enum values from the enum class provided
        `searchObj` is only needed for PyQt5 compatibility, where it must be the module holding the enum.
        For instance, if making a QtEnumParameter out of QtWidgets.QFileDialog.Option, `searchObj` would
        be QtWidgets.QFileDialog
        """
    def setValue(self, value, blockSignal: Incomplete | None = None) -> None: ...
    def formattedLimits(self): ...
    def saveState(self, filter: Incomplete | None = None): ...
