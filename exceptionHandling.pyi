from _typeshed import Incomplete

callbacks: Incomplete
old_callbacks: Incomplete
clear_tracebacks: bool

def registerCallback(fn) -> None:
    """Register a callable to be invoked when there is an unhandled exception.
    The callback will be passed an object with attributes: [exc_type, exc_value, exc_traceback, thread]
    (see threading.excepthook).
    Multiple callbacks will be invoked in the order they were registered.
    """
def unregisterCallback(fn) -> None:
    """Unregister a previously registered callback.
    """
def register(fn) -> None:
    """Deprecated; see registerCallback

    Register a callable to be invoked when there is an unhandled exception.
    The callback will be passed the output of sys.exc_info(): (exception type, exception, traceback)
    Multiple callbacks will be invoked in the order they were registered.
    """
def unregister(fn) -> None:
    """Deprecated; see unregisterCallback

    Unregister a previously registered callback.
    """
def setTracebackClearing(clear: bool = True) -> None:
    """
    Enable or disable traceback clearing.
    By default, clearing is disabled and Python will indefinitely store unhandled exception stack traces.
    This function is provided since Python's default behavior can cause unexpected retention of 
    large memory-consuming objects.
    """

class ExceptionHandler:
    orig_sys_excepthook: Incomplete
    orig_threading_excepthook: Incomplete
    def __init__(self) -> None: ...
    def remove(self) -> None:
        """Restore original exception hooks, deactivating this exception handler
        """
    def sys_excepthook(self, *args): ...
    def threading_excepthook(self, args): ...
    def implements(self, interface: Incomplete | None = None): ...

handler: Incomplete
original_excepthook: Incomplete
original_threading_excepthook: Incomplete
