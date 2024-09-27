from .. import getConfigOption as getConfigOption
from ..Qt import QtCore as QtCore, QtWidgets as QtWidgets
from .exception_widget import ExceptionHandlerWidget as ExceptionHandlerWidget
from .repl_widget import ReplWidget as ReplWidget
from _typeshed import Incomplete

class ConsoleWidget(QtWidgets.QWidget):
    """
    Widget displaying console output and accepting command input.
    Implements:
        
      - eval python expressions / exec python statements
      - storable history of commands
      - exception handling allowing commands to be interpreted in the context of any level in the exception stack frame
    
    Why not just use python in an interactive shell (or ipython) ? There are a few reasons:
       
      - pyside does not yet allow Qt event processing and interactive shell at the same time
      - on some systems, typing in the console _blocks_ the qt event loop until the user presses enter. This can
        be baffling and frustrating to users since it would appear the program has frozen.
      - some terminals (eg windows cmd.exe) have notoriously unfriendly interfaces
      - ability to add extra features like exception stack introspection
      - ability to have multiple interactive prompts, including for spawned sub-processes
    """
    localNamespace: Incomplete
    editor: Incomplete
    output: Incomplete
    input: Incomplete
    historyFile: Incomplete
    currentTraceback: Incomplete
    def __init__(self, parent: Incomplete | None = None, namespace: Incomplete | None = None, historyFile: Incomplete | None = None, text: Incomplete | None = None, editor: Incomplete | None = None) -> None:
        """
        ==============  =============================================================================
        **Arguments:**
        namespace       dictionary containing the initial variables present in the default namespace
        historyFile     optional file for storing command history
        text            initial text to display in the console window
        editor          optional string for invoking code editor (called when stack trace entries are 
                        double-clicked). May contain {fileName} and {lineNum} format keys. Example:: 
                      
                            editorCommand --loadfile {fileName} --gotoline {lineNum}
        ==============  =============================================================================
        """
    def catchAllExceptions(self, catch: bool = True) -> None: ...
    def catchNextException(self, catch: bool = True) -> None: ...
    def setStack(self, frame: Incomplete | None = None) -> None: ...
    def loadHistory(self):
        """Return the list of previously-invoked command strings (or None)."""
    def saveHistory(self, history) -> None:
        """Store the list of previously-invoked command strings."""
    def globals(self): ...
    def locals(self): ...
    def cmdSelected(self, item) -> None: ...
    def cmdDblClicked(self, item) -> None: ...
