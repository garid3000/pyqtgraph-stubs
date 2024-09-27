from ..Qt import QtCore as QtCore
from _typeshed import Incomplete

class GarbageCollector:
    """
    Disable automatic garbage collection and instead collect manually
    on a timer.

    This is done to ensure that garbage collection only happens in the GUI
    thread, as otherwise Qt can crash.

    Credit:  Erik Janssens
    Source:  http://pydev.blogspot.com/2014/03/should-python-garbage-collector-be.html
    """
    debug: Incomplete
    timer: Incomplete
    threshold: Incomplete
    def __init__(self, interval: float = 1.0, debug: bool = False) -> None: ...
    def check(self) -> None: ...
    def debug_cycles(self) -> None: ...
