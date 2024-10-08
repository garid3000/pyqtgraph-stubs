from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['ValueLabel']

class ValueLabel(QtWidgets.QLabel):
    """
    QLabel specifically for displaying numerical values.
    Extends QLabel adding some extra functionality:

      - displaying units with si prefix
      - built-in exponential averaging
    """
    values: Incomplete
    averageTime: Incomplete
    suffix: Incomplete
    siPrefix: Incomplete
    formatStr: Incomplete
    def __init__(self, parent: Incomplete | None = None, suffix: str = '', siPrefix: bool = False, averageTime: int = 0, formatStr: Incomplete | None = None) -> None:
        """
        ==============      ==================================================================================
        **Arguments:**
        suffix              (str or None) The suffix to place after the value
        siPrefix            (bool) Whether to add an SI prefix to the units and display a scaled value
        averageTime         (float) The length of time in seconds to average values. If this value
                            is 0, then no averaging is performed. As this value increases
                            the display value will appear to change more slowly and smoothly.
        formatStr           (str) Optionally, provide a format string to use when displaying text. The text
                            will be generated by calling formatStr.format(value=, avgValue=, suffix=)
                            (see Python documentation on str.format)
                            This option is not compatible with siPrefix
        ==============      ==================================================================================
        """
    def setValue(self, value) -> None: ...
    def setFormatStr(self, text) -> None: ...
    def setAverageTime(self, t) -> None: ...
    def averageValue(self): ...
    def paintEvent(self, ev): ...
    def generateText(self): ...
