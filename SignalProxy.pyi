from .Qt import QtCore
from _typeshed import Incomplete

__all__ = ['SignalProxy']

class SignalProxy(QtCore.QObject):
    """Object which collects rapid-fire signals and condenses them
    into a single signal or a rate-limited stream of signals.
    Used, for example, to prevent a SpinBox from generating multiple
    signals when the mouse wheel is rolled over it.

    Emits sigDelayed after input signals have stopped for a certain period of
    time.
    """
    sigDelayed: Incomplete
    delay: Incomplete
    rateLimit: Incomplete
    args: Incomplete
    timer: Incomplete
    lastFlushTime: Incomplete
    signal: Incomplete
    blockSignal: bool
    slot: Incomplete
    def __init__(self, signal, delay: float = 0.3, rateLimit: int = 0, slot: Incomplete | None = None, *, threadSafe: bool = True) -> None:
        """Initialization arguments:
        signal - a bound Signal or pyqtSignal instance
        delay - Time (in seconds) to wait for signals to stop before emitting (default 0.3s)
        slot - Optional function to connect sigDelayed to.
        rateLimit - (signals/sec) if greater than 0, this allows signals to stream out at a
                    steady rate while they are being received.
        threadSafe - Specify if thread-safety is required. For backwards compatibility, it
                     defaults to True.
        """
    def setDelay(self, delay) -> None: ...
    def signalReceived(self, *args) -> None:
        """Received signal. Cancel previous timer and store args to be
        forwarded later."""
    def flush(self):
        """If there is a signal queued up, send it now."""
    def disconnect(self) -> None: ...
    def connectSlot(self, slot) -> None:
        """Connect the `SignalProxy` to an external slot"""
    def block(self):
        """Return a SignalBlocker that temporarily blocks input signals to
        this proxy.
        """
