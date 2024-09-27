from ..Qt import QtWidgets
from _typeshed import Incomplete

__all__ = ['ProgressDialog']

class ProgressDialog(QtWidgets.QProgressDialog):
    '''
    Extends QProgressDialog:
    
      * Adds context management so the dialog may be used in `with` statements
      * Allows nesting multiple progress dialogs

    Example::

        with ProgressDialog("Processing..", minVal, maxVal) as dlg:
            # do stuff
            dlg.setValue(i)   ## could also use dlg += 1
            if dlg.wasCanceled():
                raise Exception("Processing canceled by user")
    '''
    allDialogs: Incomplete
    nestedLayout: Incomplete
    nested: Incomplete
    disabled: Incomplete
    busyCursor: Incomplete
    def __init__(self, labelText, minimum: int = 0, maximum: int = 100, cancelText: str = 'Cancel', parent: Incomplete | None = None, wait: int = 250, busyCursor: bool = False, disable: bool = False, nested: bool = False) -> None:
        """
        ============== ================================================================
        **Arguments:**
        labelText      (required)
        cancelText     Text to display on cancel button, or None to disable it.
        minimum
        maximum
        parent       
        wait           Length of time (im ms) to wait before displaying dialog
        busyCursor     If True, show busy cursor until dialog finishes
        disable        If True, the progress dialog will not be displayed
                       and calls to wasCanceled() will always return False.
                       If ProgressDialog is entered from a non-gui thread, it will
                       always be disabled.
        nested         (bool) If True, then this progress bar will be displayed inside
                       any pre-existing progress dialogs that also allow nesting.
        ============== ================================================================
        """
    def __enter__(self): ...
    def __exit__(self, exType: type[BaseException] | None, exValue: BaseException | None, exTrace: types.TracebackType | None) -> None: ...
    def __iadd__(self, val):
        """Use inplace-addition operator for easy incrementing."""
    def resizeEvent(self, ev): ...
    def setValue(self, val) -> None: ...
    def setLabelText(self, val) -> None: ...
    def setMaximum(self, val) -> None: ...
    def setMinimum(self, val) -> None: ...
    def wasCanceled(self): ...
    def maximum(self): ...
    def minimum(self): ...

class ProgressWidget(QtWidgets.QWidget):
    """Container for a label + progress bar that also allows its child widgets
    to be hidden without changing size.
    """
    hidden: bool
    layout: Incomplete
    label: Incomplete
    bar: Incomplete
    def __init__(self, label, bar) -> None: ...
    def eventFilter(self, obj, ev): ...
    def hide(self) -> None: ...
