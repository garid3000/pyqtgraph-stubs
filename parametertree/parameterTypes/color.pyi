from ...widgets.ColorButton import ColorButton as ColorButton
from .basetypes import SimpleParameter as SimpleParameter, WidgetParameterItem as WidgetParameterItem
from _typeshed import Incomplete

class ColorParameterItem(WidgetParameterItem):
    """Registered parameter type which displays a :class:`ColorButton <pyqtgraph.ColorButton>` """
    hideWidget: bool
    def makeWidget(self): ...

class ColorParameter(SimpleParameter):
    itemClass = ColorParameterItem
    def value(self): ...
    def saveState(self, filter: Incomplete | None = None): ...
