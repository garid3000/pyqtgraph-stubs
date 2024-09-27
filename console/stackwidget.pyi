from ..Qt import QtGui as QtGui, QtWidgets as QtWidgets
from _typeshed import Incomplete

class StackWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent: Incomplete | None = None) -> None: ...
    def selectedFrame(self):
        """Return the currently selected stack frame (or None if there is no selection)
        """
    frames: Incomplete
    def clear(self) -> None: ...
    def setException(self, exc: Incomplete | None = None, lastFrame: Incomplete | None = None) -> None:
        """Display an exception chain with its tracebacks and call stack.
        """
    def setStack(self, frame: Incomplete | None = None, expand: bool = True, lastFrame: Incomplete | None = None) -> None:
        """Display a call stack and exception traceback.

        This allows the user to probe the contents of any frame in the given stack.

        *frame* may either be a Frame instance or None, in which case the current 
        frame is retrieved from ``sys._getframe()``. 

        If *tb* is provided then the frames in the traceback will be appended to 
        the end of the stack list. If *tb* is None, then sys.exc_info() will 
        be checked instead.
        """

def stackFromFrame(frame, lastFrame: Incomplete | None = None):
    """Return (text, stack_frame) for the entire stack ending at *frame*

    If *lastFrame* is given and present in the stack, then the stack is truncated 
    at that frame.
    """
def stacksFromTraceback(tb, lastFrame: Incomplete | None = None):
    """Return (text, stack_frame) for a traceback and the stack preceding it

    If *lastFrame* is given and present in the stack, then the stack is truncated 
    at that frame.
    """
def makeItemTree(stack, title): ...
def exceptionChain(exc):
    """Return a list of (exception, 'cause'|'context') pairs for exceptions
    leading up to *exc*
    """
def textItem(text):
    """Return a tree item with no associated stack frame and a darker background color
    """
