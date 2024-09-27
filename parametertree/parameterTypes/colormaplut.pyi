from ... import colormap as colormap
from ...widgets.ColorMapButton import ColorMapButton as ColorMapButton
from .basetypes import Parameter as Parameter, WidgetParameterItem as WidgetParameterItem

class ColorMapLutParameterItem(WidgetParameterItem):
    hideWidget: bool
    def makeWidget(self): ...

class ColorMapLutParameter(Parameter):
    itemClass = ColorMapLutParameterItem
