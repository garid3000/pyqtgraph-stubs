from ..Qt import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets
from ..functions import mkBrush as mkBrush
from .CmdInput import CmdInput as CmdInput
from _typeshed import Incomplete

class ReplWidget(QtWidgets.QWidget):
    sigCommandEntered: Incomplete
    sigCommandRaisedException: Incomplete
    globals: Incomplete
    locals: Incomplete
    stdoutInterceptor: Incomplete
    ps1: str
    ps2: str
    textStyles: Incomplete
    def __init__(self, globals, locals, parent: Incomplete | None = None) -> None: ...
    def runCmd(self, cmd) -> None: ...
    def write(self, strn, style: str = 'output', scrollToBottom: str = 'auto') -> None:
        """Write a string into the console.

        If scrollToBottom is 'auto', then the console is automatically scrolled
        to fit the new text only if it was already at the bottom.
        """
    def displayException(self) -> None:
        """
        Display the current exception and stack.
        """

class StdoutInterceptor:
    """Used to temporarily redirect writes meant for sys.stdout and sys.stderr to a new location
    """
    writeFn: Incomplete
    def __init__(self, writeFn) -> None: ...
    def realOutputFiles(self):
        """Return the real sys.stdout and stderr (which are sometimes masked while running commands)
        """
    def print(self, *args) -> None:
        """Print to real stdout (for debugging)
        """
    def flush(self) -> None: ...
    def fileno(self): ...
    def write(self, strn) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
