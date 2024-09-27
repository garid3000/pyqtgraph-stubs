from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['SpinBox']

class SpinBox(QtWidgets.QAbstractSpinBox):
    '''
    **Bases:** QtWidgets.QAbstractSpinBox
    
    Extension of QSpinBox widget for selection of a numerical value.     
    Adds many extra features:
    
      * SI prefix notation (eg, automatically display "300 mV" instead of "0.003 V")
      * Float values with linear and decimal stepping (1-9, 10-90, 100-900, etc.)
      * Option for unbounded values
      * Delayed signals (allows multiple rapid changes with only one change signal)
      * Customizable text formatting
    
    =============================  ==============================================
    **Signals:**
    valueChanged(value)            Same as QSpinBox; emitted every time the value 
                                   has changed.
    sigValueChanged(self)          Emitted when value has changed, but also combines
                                   multiple rapid changes into one signal (eg, 
                                   when rolling the mouse wheel).
    sigValueChanging(self, value)  Emitted immediately for all value changes.
    =============================  ==============================================
    '''
    valueChanged: Incomplete
    sigValueChanged: Incomplete
    sigValueChanging: Incomplete
    lastValEmitted: Incomplete
    lastText: str
    textValid: bool
    errorBox: Incomplete
    opts: Incomplete
    decOpts: Incomplete
    val: Incomplete
    skipValidate: bool
    proxy: Incomplete
    def __init__(self, parent: Incomplete | None = None, value: float = 0.0, **kwargs) -> None:
        """
        ============== ========================================================================
        **Arguments:**
        parent         Sets the parent widget for this SpinBox (optional). Default is None.
        value          (float/int) initial value. Default is 0.0.
        ============== ========================================================================
        
        All keyword arguments are passed to :func:`setOpts`.
        """
    def setOpts(self, **opts) -> None:
        '''Set options affecting the behavior of the SpinBox.
        
        ============== ========================================================================
        **Arguments:**
        bounds         (min,max) Minimum and maximum values allowed in the SpinBox. 
                       Either may be None to leave the value unbounded. By default, values are
                       unbounded.
        suffix         (str) suffix (units) to display after the numerical value. By default,
                       suffix is an empty str.
        siPrefix       (bool) If True, then an SI prefix is automatically prepended
                       to the units and the value is scaled accordingly. For example,
                       if value=0.003 and suffix=\'V\', then the SpinBox will display
                       "300 mV" (but a call to SpinBox.value will still return 0.003). In case
                       the value represents a dimensionless quantity that might span many
                       orders of magnitude, such as a Reynolds number, an SI
                       prefix is allowed with no suffix. Default is False.
        prefix         (str) String to be prepended to the spin box value. Default is an empty string.
        scaleAtZero    (float) If siPrefix is also True, this option then sets the default SI prefix
                       that a value of 0 will have applied (and thus the default scale of the first
                       number the user types in after the SpinBox has been zeroed out).
        step           (float) The size of a single step. This is used when clicking the up/
                       down arrows, when rolling the mouse wheel, or when pressing 
                       keyboard arrows while the widget has keyboard focus. Note that
                       the interpretation of this value is different when specifying
                       the \'dec\' argument. If \'int\' is True, \'step\' is rounded to the nearest integer.
                       Default is 0.01 if \'int\' is False and 1 otherwise.
        dec            (bool) If True, then the step value will be adjusted to match 
                       the current size of the variable (for example, a value of 15
                       might step in increments of 1 whereas a value of 1500 would
                       step in increments of 100). In this case, the \'step\' argument
                       is interpreted *relative* to the current value. The most common
                       \'step\' values when dec=True are 0.1, 0.2, 0.5, and 1.0. Default is
                       False.
        minStep        (float) When dec=True, this specifies the minimum allowable step size.
        int            (bool) If True, the value is forced to integer type.
                       If True, \'step\' is rounded to the nearest integer or defaults to 1.
                       Default is False
        finite         (bool) When False and int=False, infinite values (nan, inf, -inf) are
                       permitted. Default is True.
        wrapping       (bool) If True and both bounds are not None, spin box has circular behavior.
        decimals       (int) Number of decimal values to display. Default is 6. 
        format         (str) Formatting string used to generate the text shown. Formatting is
                       done with ``str.format()`` and makes use of several arguments:
                       
                         * *value* - the unscaled value of the spin box
                         * *prefix* - the prefix string
                         * *prefixGap* - a single space if a prefix is present, or an empty
                           string otherwise
                         * *suffix* - the suffix string
                         * *scaledValue* - the scaled value to use when an SI prefix is present
                         * *siPrefix* - the SI prefix string (if any), or an empty string if
                           this feature has been disabled
                         * *suffixGap* - a single space if a suffix is present, or an empty
                           string otherwise.
        regex          (str or RegexObject) Regular expression used to parse the spinbox text.
                       May contain the following group names:
                       
                       * *number* - matches the numerical portion of the string (mandatory)
                       * *siPrefix* - matches the SI prefix string
                       * *suffix* - matches the suffix string
                       
                       Default is defined in ``pyqtgraph.functions.FLOAT_REGEX``.
        evalFunc       (callable) Fucntion that converts a numerical string to a number,
                       preferrably a Decimal instance. This function handles only the numerical
                       of the text; it does not have access to the suffix or SI prefix.
        compactHeight  (bool) if True, then set the maximum height of the spinbox based on the
                       height of its font. This allows more compact packing on platforms with
                       excessive widget decoration. Default is True.
        ============== ========================================================================
        '''
    def setMaximum(self, m, update: bool = True) -> None:
        """Set the maximum allowed value (or None for no limit)"""
    def setMinimum(self, m, update: bool = True) -> None:
        """Set the minimum allowed value (or None for no limit)"""
    def wrapping(self):
        """Return whether or not the spin box is circular."""
    def setWrapping(self, s) -> None:
        """Set whether spin box is circular.
        
        Both bounds must be set for this to have an effect."""
    def setPrefix(self, p) -> None:
        """Set a string prefix.
        """
    def setRange(self, r0, r1) -> None:
        """Set the upper and lower limits for values in the spinbox.
        """
    def setProperty(self, prop, val) -> None: ...
    def setSuffix(self, suf) -> None:
        """Set the string suffix appended to the spinbox text.
        """
    def setSingleStep(self, step) -> None:
        """Set the step size used when responding to the mouse wheel, arrow
        buttons, or arrow keys.
        """
    def setDecimals(self, decimals) -> None:
        """Set the number of decimals to be displayed when formatting numeric
        values.
        """
    def selectNumber(self) -> None:
        """
        Select the numerical portion of the text to allow quick editing by the user.
        """
    def focusInEvent(self, ev) -> None: ...
    def value(self):
        """
        Return the value of this SpinBox.
        
        """
    def setValue(self, value: Incomplete | None = None, update: bool = True, delaySignal: bool = False):
        """Set the value of this SpinBox.
        
        If the value is out of bounds, it will be clipped to the nearest boundary
        or wrapped if wrapping is enabled.
        
        If the spin is integer type, the value will be coerced to int.
        Returns the actual value set.
        
        If value is None, then the current value is used (this is for resetting
        the value after bounds, etc. have changed)
        """
    def emitChanged(self) -> None: ...
    def delayedChange(self) -> None: ...
    def widgetGroupInterface(self): ...
    def sizeHint(self): ...
    def stepEnabled(self): ...
    def stepBy(self, n) -> None: ...
    def valueInRange(self, value): ...
    def updateText(self, **kwargs) -> None: ...
    def formatText(self, **kwargs): ...
    def validate(self, strn, pos): ...
    def fixup(self, strn): ...
    def interpret(self):
        """Return value of text or False if text is invalid."""
    def editingFinishedEvent(self) -> None:
        """Edit has finished; set value."""
    def paintEvent(self, ev) -> None: ...

class ErrorBox(QtWidgets.QWidget):
    """Red outline to draw around lineedit when value is invalid.
    (for some reason, setting border from stylesheet does not work)
    """
    def __init__(self, parent) -> None: ...
    def eventFilter(self, obj, ev): ...
    def paintEvent(self, ev) -> None: ...
