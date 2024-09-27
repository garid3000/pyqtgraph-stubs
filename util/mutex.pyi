from ..Qt import QtCore as QtCore
from _typeshed import Incomplete

class Mutex(QtCore.QMutex):
    '''
    Subclass of QMutex that provides useful debugging information during
    deadlocks--tracebacks are printed for both the code location that is 
    attempting to lock the mutex as well as the location that has already
    acquired the lock.
    
    Also provides __enter__ and __exit__ methods for use in "with" statements.
    '''
    l: Incomplete
    tb: Incomplete
    debug: Incomplete
    def __init__(self, *args, **kargs) -> None: ...
    def tryLock(self, timeout: Incomplete | None = None, id: Incomplete | None = None): ...
    def lock(self, id: Incomplete | None = None) -> None: ...
    def unlock(self) -> None: ...
    def acquire(self, blocking: bool = True):
        """Mimics threading.Lock.acquire() to allow this class as a drop-in replacement.
        """
    def release(self) -> None:
        """Mimics threading.Lock.release() to allow this class as a drop-in replacement.
        """
    def depth(self): ...
    def traceback(self): ...
    def __exit__(self, *args) -> None: ...
    def __enter__(self): ...

class RecursiveMutex(Mutex):
    """Mimics threading.RLock class.
    """
    def __init__(self, **kwds) -> None: ...
