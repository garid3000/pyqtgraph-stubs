import numpy as np
from ...Qt import QtCore as QtCore, QtWidgets as QtWidgets
from ..Parameter import Parameter as Parameter
from .basetypes import Emitter as Emitter, WidgetParameterItem as WidgetParameterItem
from _typeshed import Incomplete

class SliderParameterItem(WidgetParameterItem):
    slider: QtWidgets.QSlider
    span: np.ndarray
    charSpan: np.ndarray
    emitter: Incomplete
    sigChanging: Incomplete
    def __init__(self, param, depth) -> None: ...
    def updateDisplayLabel(self, value: Incomplete | None = None) -> None: ...
    def setSuffix(self, suffix) -> None: ...
    def makeWidget(self): ...
    def spanToSliderValue(self, v): ...
    def prettyTextValue(self, v): ...
    def optsChanged(self, param, opts) -> None: ...
    def limitsChanged(self, param, limits) -> None: ...

class SliderParameter(Parameter):
    """
    ============== ========================================================
    **Options**
    limits         [start, stop] numbers
    step:          Defaults to 1, the spacing between each slider tick
    span:          Instead of limits + step, span can be set to specify
                   the range of slider options (e.g. np.linspace(-pi, pi, 100))
    format:        Format string to determine number of decimals to show, etc.
                   Defaults to display based on span dtype
    precision:     int number of decimals to keep for float tick spaces
    ============== ========================================================
    """
    itemClass = SliderParameterItem
