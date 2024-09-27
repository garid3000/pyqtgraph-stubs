import pyqtgraph as pg
from _typeshed import Incomplete
from pyqtgraph.Qt import QtWidgets as QtWidgets
from pyqtgraph.debug import threadName as threadName

def raiseException() -> None:
    """Raise an exception
    """
def raiseNested() -> None:
    """Raise an exception while handling another
    """
def raiseFrom() -> None:
    """Raise an exception from another
    """
def raiseCaughtException() -> None:
    """Raise and catch an exception
    """
def captureStack():
    """Inspect the curent call stack
    """

threadRunQueue: Incomplete

def threadRunner() -> None: ...

thread: Incomplete

def runInStack(func): ...
def runInStack2(func): ...
def runInStack3(func): ...
def runInStack4(func): ...

class SignalEmitter(pg.QtCore.QObject):
    signal: Incomplete
    def __init__(self, queued) -> None: ...
    def run(self, func, args) -> None: ...

signalEmitter: Incomplete
queuedSignalEmitter: Incomplete

def runFunc(func) -> None: ...

funcs: Incomplete
app: Incomplete
win: Incomplete
ctrl: Incomplete
ctrlLayout: Incomplete
btns: Incomplete
btn: Incomplete
threadCheck: Incomplete
signalCheck: Incomplete
queuedSignalCheck: Incomplete
console: Incomplete
