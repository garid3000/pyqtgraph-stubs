from .Qt import QtCore
from _typeshed import Incomplete

__all__ = ['ThreadsafeTimer']

class ThreadsafeTimer(QtCore.QObject):
    """
    Thread-safe replacement for QTimer.
    """
    timeout: Incomplete
    sigTimerStopRequested: Incomplete
    sigTimerStartRequested: Incomplete
    timer: Incomplete
    def __init__(self) -> None: ...
    def start(self, timeout) -> None: ...
    def stop(self) -> None: ...
    def timerFinished(self) -> None: ...
