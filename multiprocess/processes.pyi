import threading
from .remoteproxy import ClosedError as ClosedError, NoResultError as NoResultError, RemoteEventHandler
from _typeshed import Incomplete

__all__ = ['Process', 'QtProcess', 'ForkedProcess', 'ClosedError', 'NoResultError']

class Process(RemoteEventHandler):
    """
    Bases: RemoteEventHandler
    
    This class is used to spawn and control a new python interpreter.
    It uses subprocess.Popen to start the new process and communicates with it
    using multiprocessing.Connection objects over a network socket.
    
    By default, the remote process will immediately enter an event-processing
    loop that carries out requests send from the parent process.
    
    Remote control works mainly through proxy objects::
    
        proc = Process()              ## starts process, returns handle
        rsys = proc._import('sys')    ## asks remote process to import 'sys', returns
                                      ## a proxy which references the imported module
        rsys.stdout.write('hello
')  ## This message will be printed from the remote 
                                      ## process. Proxy objects can usually be used
                                      ## exactly as regular objects are.
        proc.close()                  ## Request the remote process shut down
    
    Requests made via proxy objects may be synchronous or asynchronous and may
    return objects either by proxy or by value (if they are picklable). See
    ProxyObject for more information.
    """
    debug: Incomplete
    proc: Incomplete
    def __init__(self, name: Incomplete | None = None, target: Incomplete | None = None, executable: Incomplete | None = None, copySysPath: bool = True, debug: bool = False, timeout: int = 20, wrapStdout: Incomplete | None = None, pyqtapis: Incomplete | None = None) -> None:
        """
        ==============  =============================================================
        **Arguments:**
        name            Optional name for this process used when printing messages
                        from the remote process.
        target          Optional function to call after starting remote process.
                        By default, this is startEventLoop(), which causes the remote
                        process to handle requests from the parent process until it
                        is asked to quit. If you wish to specify a different target,
                        it must be picklable (bound methods are not).
        copySysPath     If True, copy the contents of sys.path to the remote process.
                        If False, then only the path required to import pyqtgraph is
                        added.
        debug           If True, print detailed information about communication
                        with the child process.
        wrapStdout      If True (default on windows) then stdout and stderr from the
                        child process will be caught by the parent process and
                        forwarded to its stdout/stderr. This provides a workaround
                        for a python bug: http://bugs.python.org/issue3905
                        but has the side effect that child output is significantly
                        delayed relative to the parent output.
        pyqtapis        Formerly optional dictionary of PyQt API version numbers to set
                        before importing pyqtgraph in the remote process.
                        No longer has any effect.
        ==============  =============================================================
        """
    def join(self, timeout: int = 10) -> None: ...
    def debugMsg(self, msg, *args) -> None: ...

class ForkedProcess(RemoteEventHandler):
    """
    ForkedProcess is a substitute for Process that uses os.fork() to generate a new process.
    This is much faster than starting a completely new interpreter and child processes
    automatically have a copy of the entire program state from before the fork. This
    makes it an appealing approach when parallelizing expensive computations. (see
    also Parallelizer)
    
    However, fork() comes with some caveats and limitations:

      - fork() is not available on Windows.
      - It is not possible to have a QApplication in both parent and child process
        (unless both QApplications are created _after_ the call to fork())
        Attempts by the forked process to access Qt GUI elements created by the parent
        will most likely cause the child to crash.
      - Likewise, database connections are unlikely to function correctly in a forked child.
      - Threads are not copied by fork(); the new process
        will have only one thread that starts wherever fork() was called in the parent process.
      - Forked processes are unceremoniously terminated when join() is called; they are not
        given any opportunity to clean up. (This prevents them calling any cleanup code that
        was only intended to be used by the parent process)
      - Normally when fork()ing, open file handles are shared with the parent process,
        which is potentially dangerous. ForkedProcess is careful to close all file handles
        that are not explicitly needed--stdout, stderr, and a single pipe to the parent
        process.
      
    """
    hasJoined: bool
    isParent: bool
    forkedProxies: Incomplete
    childPid: Incomplete
    def __init__(self, name: Incomplete | None = None, target: int = 0, preProxy: Incomplete | None = None, randomReseed: bool = True) -> None:
        """
        When initializing, an optional target may be given. 
        If no target is specified, self.eventLoop will be used.
        If None is given, no target will be called (and it will be up 
        to the caller to properly shut down the forked process)
        
        preProxy may be a dict of values that will appear as ObjectProxy
        in the remote process (but do not need to be sent explicitly since 
        they are available immediately before the call to fork().
        Proxies will be availabe as self.proxies[name].
        
        If randomReseed is True, the built-in random and numpy.random generators
        will be reseeded in the child process.
        """
    def eventLoop(self) -> None: ...
    def join(self, timeout: int = 10) -> None: ...
    def kill(self) -> None:
        """Immediately kill the forked remote process. 
        This is generally safe because forked processes are already
        expected to _avoid_ any cleanup at exit."""

class RemoteQtEventHandler(RemoteEventHandler):
    def __init__(self, *args, **kwds) -> None: ...
    timer: Incomplete
    def startEventTimer(self) -> None: ...
    def processRequests(self) -> None: ...

class QtProcess(Process):
    """
    QtProcess is essentially the same as Process, with two major differences:
    
      - The remote process starts by running startQtEventLoop() which creates a
        QApplication in the remote process and uses a QTimer to trigger
        remote event processing. This allows the remote process to have its own
        GUI.
      - A QTimer is also started on the parent process which polls for requests
        from the child process. This allows Qt signals emitted within the child
        process to invoke slots on the parent process and vice-versa. This can
        be disabled using processRequests=False in the constructor.
      
    Example::
    
        proc = QtProcess()            
        rQtGui = proc._import('PyQt4.QtGui')
        btn = rQtWidgets.QPushButton('button on child process')
        btn.show()
        
        def slot():
            print('slot invoked on parent process')
        btn.clicked.connect(proxy(slot))   # be sure to send a proxy of the slot
    """
    def __init__(self, **kwds) -> None: ...
    timer: Incomplete
    def startEventTimer(self) -> None: ...
    def startRequestProcessing(self, interval: float = 0.01) -> None:
        """Start listening for requests coming from the child process.
        This allows signals to be connected from the child process to the parent.
        """
    def stopRequestProcessing(self) -> None: ...
    def processRequests(self) -> None: ...

class FileForwarder(threading.Thread):
    """
    Background thread that forwards data from one pipe to another. 
    This is used to catch data from stdout/stderr of the child process
    and print it back out to stdout/stderr. We need this because this
    bug: http://bugs.python.org/issue3905  _requires_ us to catch
    stdout/stderr.

    *output* may be a file or 'stdout' or 'stderr'. In the latter cases,
    sys.stdout/stderr are retrieved once for every line that is output,
    which ensures that the correct behavior is achieved even if 
    sys.stdout/stderr are replaced at runtime.
    """
    input: Incomplete
    output: Incomplete
    lock: Incomplete
    daemon: bool
    color: Incomplete
    finish: Incomplete
    def __init__(self, input, output, color) -> None: ...
    def run(self) -> None: ...
