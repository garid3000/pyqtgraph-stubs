from ...Qt import QtCore as QtCore
from ...colormap import ColorMap as ColorMap
from ...widgets.GradientWidget import GradientWidget as GradientWidget
from .basetypes import SimpleParameter as SimpleParameter, WidgetParameterItem as WidgetParameterItem

class ColorMapParameterItem(WidgetParameterItem):
    """Registered parameter type which displays a :class:`GradientWidget <pyqtgraph.GradientWidget>`"""
    hideWidget: bool
    asSubItem: bool
    def makeWidget(self): ...

class ColorMapParameter(SimpleParameter):
    itemClass = ColorMapParameterItem
