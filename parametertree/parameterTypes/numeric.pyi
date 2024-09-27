from ...widgets.SpinBox import SpinBox as SpinBox
from .basetypes import WidgetParameterItem as WidgetParameterItem
from _typeshed import Incomplete

class NumericParameterItem(WidgetParameterItem):
    """
    Subclasses `WidgetParameterItem` to provide the following types:

    ==========================  =============================================================
    **Registered Types:**
    int                         Displays a :class:`SpinBox <pyqtgraph.SpinBox>` in integer
                                mode.
    float                       Displays a :class:`SpinBox <pyqtgraph.SpinBox>`.
    ==========================  =============================================================
    """
    def makeWidget(self): ...
    def updateDisplayLabel(self, value: Incomplete | None = None) -> None: ...
    def showEditor(self) -> None: ...
    def limitsChanged(self, param, limits) -> None: ...
    def optsChanged(self, param, opts) -> None: ...
