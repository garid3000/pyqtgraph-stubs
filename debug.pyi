from .Qt import QT_LIB as QT_LIB, QtCore as QtCore
from .util import cprint as cprint
from .util.mutex import Mutex as Mutex
from _typeshed import Incomplete
from collections.abc import Generator

def open_maybe_console(filename: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
def ftrace(func):
    """Decorator used for marking the beginning and end of function calls.
    Automatically indents nested calls.
    """

class Tracer:
    """
    Prints every function enter/exit. Useful for debugging crashes / lockups.
    """
    count: int
    stack: Incomplete
    def __init__(self) -> None: ...
    def trace(self, frame, event, arg): ...
    def stop(self) -> None: ...
    def start(self) -> None: ...
    def frameInfo(self, fr): ...

def warnOnException(func):
    """Decorator that catches/ignores exceptions and prints a stack trace."""
def getExc(indent: int = 4, prefix: str = '|  ', skip: int = 1): ...
def printExc(msg: str = '', indent: int = 4, prefix: str = '|') -> None:
    """Print an error message followed by an indented exception backtrace
    (This function is intended to be called within except: blocks)"""
def printTrace(msg: str = '', indent: int = 4, prefix: str = '|') -> None:
    """Print an error message followed by an indented stack trace"""
def backtrace(skip: int = 0): ...
def formatException(exctype, value, tb, skip: int = 0):
    """Return a list of formatted exception strings.
    
    Similar to traceback.format_exception, but displays the entire stack trace
    rather than just the portion downstream of the point where the exception is
    caught. In particular, unhandled exceptions that occur during Qt signal
    handling do not usually show the portion of the stack that emitted the
    signal.
    """
def printException(exctype, value, traceback) -> None:
    """Print an exception with its full traceback.
    
    Set `sys.excepthook = printException` to ensure that exceptions caught
    inside Qt signal handlers are printed with their full stack trace.
    """
def listObjs(regex: str = 'Q', typ: Incomplete | None = None):
    """List all objects managed by python gc with class name matching regex.
    Finds 'Q...' classes by default."""
def findRefPath(startObj, endObj, maxLen: int = 8, restart: bool = True, seen: Incomplete | None = None, path: Incomplete | None = None, ignore: Incomplete | None = None):
    """Determine all paths of object references from startObj to endObj"""
def objString(obj):
    """Return a short but descriptive string for any object"""
def refPathString(chain):
    """Given a list of adjacent objects in a reference path, print the 'natural' path
    names (ie, attribute names, keys, and indexes) that follow from one object to the next ."""
def objectSize(obj, ignore: Incomplete | None = None, verbose: bool = False, depth: int = 0, recursive: bool = False):
    """Guess how much memory an object is using"""

class GarbageWatcher:
    """
    Convenient dictionary for holding weak references to objects.
    Mainly used to check whether the objects have been collect yet or not.
    
    Example:
        gw = GarbageWatcher()
        gw['objName'] = obj
        gw['objName2'] = obj2
        gw.check()  
        
    
    """
    objs: Incomplete
    allNames: Incomplete
    def __init__(self) -> None: ...
    def add(self, obj, name) -> None: ...
    def __setitem__(self, name, obj) -> None: ...
    def check(self) -> None:
        """Print a list of all watched objects and whether they have been collected."""
    def __getitem__(self, item): ...

class Profiler:
    '''Simple profiler allowing measurement of multiple time intervals.

    By default, profilers are disabled.  To enable profiling, set the
    environment variable `PYQTGRAPHPROFILE` to a comma-separated list of
    fully-qualified names of profiled functions.

    Calling a profiler registers a message (defaulting to an increasing
    counter) that contains the time elapsed since the last call.  When the
    profiler is about to be garbage-collected, the messages are passed to the
    outer profiler if one is running, or printed to stdout otherwise.

    If `delayed` is set to False, messages are immediately printed instead.

    Example:
        def function(...):
            profiler = Profiler()
            ... do stuff ...
            profiler(\'did stuff\')
            ... do other stuff ...
            profiler(\'did other stuff\')
            # profiler is garbage-collected and flushed at function end

    If this function is a method of class C, setting `PYQTGRAPHPROFILE` to
    "C.function" (without the module name) will enable this profiler.

    For regular functions, use the qualified name of the function, stripping
    only the initial "pyqtgraph." prefix from the module.
    '''
    disable: bool
    class DisabledProfiler:
        def __init__(self, *args, **kwds) -> None: ...
        def __call__(self, *args) -> None: ...
        def finish(self) -> None: ...
        def mark(self, msg: Incomplete | None = None) -> None: ...
    def __new__(cls, msg: Incomplete | None = None, disabled: str = 'env', delayed: bool = True):
        """Optionally create a new profiler based on caller's qualname.
        """
    def __call__(self, msg: Incomplete | None = None) -> None:
        """Register or print a new message with timing information.
        """
    def mark(self, msg: Incomplete | None = None) -> None: ...
    def __del__(self) -> None: ...
    def finish(self, msg: Incomplete | None = None) -> None:
        """Add a final message; flush the message list if no parent profiler.
        """
    def flush(self) -> None: ...

def profile(code, name: str = 'profile_run', sort: str = 'cumulative', num: int = 30):
    """Common-use for cProfile"""
def get_all_objects():
    """Return a list of all live Python objects (excluding int and long), not including the list itself."""
def lookup(oid, objects: Incomplete | None = None):
    """Return an object given its ID, if it exists."""

class ObjTracker:
    """
    Tracks all objects under the sun, reporting the changes between snapshots: what objects are created, deleted, and persistent.
    This class is very useful for tracking memory leaks. The class goes to great (but not heroic) lengths to avoid tracking 
    its own internal objects.
    
    Example:
        ot = ObjTracker()   # takes snapshot of currently existing objects
           ... do stuff ...
        ot.diff()           # prints lists of objects created and deleted since ot was initialized
           ... do stuff ...
        ot.diff()           # prints lists of objects created and deleted since last call to ot.diff()
                            # also prints list of items that were created since initialization AND have not been deleted yet
                            #   (if done correctly, this list can tell you about objects that were leaked)
           
        arrays = ot.findPersistent('ndarray')  ## returns all objects matching 'ndarray' (string match, not instance checking)
                                               ## that were considered persistent when the last diff() was run
                                               
        describeObj(arrays[0])    ## See if we can determine who has references to this array
    """
    allObjs: Incomplete
    startRefs: Incomplete
    startCount: Incomplete
    newRefs: Incomplete
    persistentRefs: Incomplete
    objTypes: Incomplete
    objs: Incomplete
    def __init__(self) -> None: ...
    def findNew(self, regex):
        """Return all objects matching regex that were considered 'new' when the last diff() was run."""
    def findPersistent(self, regex):
        """Return all objects matching regex that were considered 'persistent' when the last diff() was run."""
    def start(self) -> None:
        """
        Remember the current set of objects as the comparison for all future calls to diff()
        Called automatically on init, but can be called manually as well.
        """
    def diff(self, **kargs):
        """
        Compute all differences between the current object set and the reference set.
        Print a set of reports for created, deleted, and persistent objects
        """
    def __del__(self) -> None: ...
    @classmethod
    def isObjVar(cls, o): ...
    def collect(self): ...
    def forgetRef(self, ref) -> None: ...
    def rememberRef(self, ref) -> None: ...
    def lookup(self, oid, ref, objs: Incomplete | None = None): ...
    def report(self, refs, allobjs: Incomplete | None = None, showIDs: bool = False): ...
    def findTypes(self, refs, regex): ...

def describeObj(obj, depth: int = 4, path: Incomplete | None = None, ignore: Incomplete | None = None) -> None:
    '''
    Trace all reference paths backward, printing a list of different ways this object can be accessed.
    Attempts to answer the question "who has a reference to this object"
    '''
def typeStr(obj):
    """Create a more useful type string by making <instance> types report their class."""
def searchRefs(obj, *args):
    """Pseudo-interactive function for tracing references backward.
    **Arguments:**
    
        obj:   The initial object from which to start searching
        args:  A set of string or int arguments.
               each integer selects one of obj's referrers to be the new 'obj'
               each string indicates an action to take on the current 'obj':
                  t:  print the types of obj's referrers
                  l:  print the lengths of obj's referrers (if they have __len__)
                  i:  print the IDs of obj's referrers
                  o:  print obj
                  ro: return obj
                  rr: return list of obj's referrers
    
    Examples::
    
       searchRefs(obj, 't')                    ## Print types of all objects referring to obj
       searchRefs(obj, 't', 0, 't')            ##   ..then select the first referrer and print the types of its referrers
       searchRefs(obj, 't', 0, 't', 'l')       ##   ..also print lengths of the last set of referrers
       searchRefs(obj, 0, 1, 'ro')             ## Select index 0 from obj's referrer, then select index 1 from the next set of referrers, then return that object
       
    """
def allFrameObjs():
    """Return list of frame objects in current stack. Useful if you want to ignore these objects in refernece searches"""
def findObj(regex):
    """Return a list of objects whose typeStr matches regex"""
def listRedundantModules() -> None:
    """List modules that have been imported more than once via different paths."""
def walkQObjectTree(obj, counts: Incomplete | None = None, verbose: bool = False, depth: int = 0):
    """
    Walk through a tree of QObjects, doing nothing to them.
    The purpose of this function is to find dead objects and generate a crash
    immediately rather than stumbling upon them later.
    Prints a count of the objects encountered, for fun. (or is it?)
    """

QObjCache: Incomplete

def qObjectReport(verbose: bool = False) -> None:
    """Generate a report counting all QObjects and their types"""

class PrintDetector:
    """Find code locations that print to stdout."""
    stdout: Incomplete
    def __init__(self) -> None: ...
    def remove(self) -> None: ...
    def __del__(self) -> None: ...
    def write(self, x) -> None: ...
    def flush(self) -> None: ...

def listQThreads() -> None:
    """Prints Thread IDs (Qt's, not OS's) for all QThreads."""
def pretty(data, indent: str = ''):
    """Format nested dict/list/tuple structures into a more human-readable string
    This function is a bit better than pprint for displaying OrderedDicts.
    """

class ThreadTrace:
    """ 
    Used to debug freezing by starting a new thread that reports on the 
    location of other threads periodically.
    """
    interval: Incomplete
    lock: Incomplete
    logFile: Incomplete
    def __init__(self, interval: float = 10.0, logFile: Incomplete | None = None) -> None: ...
    def stop(self) -> None: ...
    thread: Incomplete
    def start(self, interval: Incomplete | None = None) -> None: ...
    def run(self) -> None: ...

def threadName(threadId: Incomplete | None = None):
    '''Return a string name for a thread id.

    If *threadId* is None, then the current thread\'s id is used.

    This attempts to look up thread names either from `threading._active`, or from
    QThread._names. However, note that the latter does not exist by default; rather
    you must manually add id:name pairs to a dictionary there::

        # for python threads:
        t1 = threading.Thread(name="mythread")

        # for Qt threads:
        class Thread(Qt.QThread):
            def __init__(self, name):
                self._threadname = name
                if not hasattr(Qt.QThread, \'_names\'):
                    Qt.QThread._names = {}
                Qt.QThread.__init__(self, *args, **kwds)
            def run(self):
                Qt.QThread._names[threading.current_thread().ident] = self._threadname
    '''

class ThreadColor:
    """
    Wrapper on stdout/stderr that colors text by the current thread ID.

    *stream* must be 'stdout' or 'stderr'.
    """
    colors: Incomplete
    lock: Incomplete
    stream: Incomplete
    err: Incomplete
    def __init__(self, stream) -> None: ...
    def write(self, msg) -> None: ...
    def flush(self) -> None: ...
    def color(self): ...

def enableFaulthandler():
    """ Enable faulthandler for all threads. 
    
    If the faulthandler package is available, this function disables and then 
    re-enables fault handling for all threads (this is necessary to ensure any
    new threads are handled correctly), and returns True.

    If faulthandler is not available, then returns False.
    """
