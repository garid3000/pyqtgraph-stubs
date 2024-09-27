from .processes import ForkedProcess as ForkedProcess
from .remoteproxy import ClosedError as ClosedError
from _typeshed import Incomplete

class CanceledError(Exception):
    """Raised when the progress dialog is canceled during a processing operation."""

class Parallelize:
    """
    Class for ultra-simple inline parallelization on multi-core CPUs
    
    Example::
    
        ## Here is the serial (single-process) task:
        
        tasks = [1, 2, 4, 8]
        results = []
        for task in tasks:
            result = processTask(task)
            results.append(result)
        print(results)
        
        
        ## Here is the parallelized version:
        
        tasks = [1, 2, 4, 8]
        results = []
        with Parallelize(tasks, workers=4, results=results) as tasker:
            for task in tasker:
                result = processTask(task)
                tasker.results.append(result)
        print(results)
        
        
    The only major caveat is that *result* in the example above must be picklable,
    since it is automatically sent via pipe back to the parent process.
    """
    showProgress: bool
    progressDlg: Incomplete
    workers: Incomplete
    tasks: Incomplete
    reseed: Incomplete
    kwds: Incomplete
    def __init__(self, tasks: Incomplete | None = None, workers: Incomplete | None = None, block: bool = True, progressDialog: Incomplete | None = None, randomReseed: bool = True, **kwds) -> None:
        """
        ===============  ===================================================================
        **Arguments:**
        tasks            list of objects to be processed (Parallelize will determine how to 
                         distribute the tasks). If unspecified, then each worker will receive
                         a single task with a unique id number.
        workers          number of worker processes or None to use number of CPUs in the 
                         system
        progressDialog   optional dict of arguments for ProgressDialog
                         to update while tasks are processed
        randomReseed     If True, each forked process will reseed its random number generator
                         to ensure independent results. Works with the built-in random
                         and numpy.random.
        kwds             objects to be shared by proxy with child processes (they will 
                         appear as attributes of the tasker)
        ===============  ===================================================================
        """
    proc: Incomplete
    def __enter__(self): ...
    def __exit__(self, *exc_info) -> None: ...
    progress: Incomplete
    def runSerial(self): ...
    childs: Incomplete
    exitCodes: Incomplete
    def runParallel(self): ...
    @staticmethod
    def suggestedWorkerCount(): ...

class Tasker:
    proc: Incomplete
    par: Incomplete
    tasks: Incomplete
    def __init__(self, parallelizer, process, tasks, kwds) -> None: ...
    index: Incomplete
    def __iter__(self): ...
    def process(self) -> None:
        """
        Process requests from parent.
        Usually it is not necessary to call this unless you would like to 
        receive messages (such as exit requests) during an iteration.
        """
    def numWorkers(self):
        """
        Return the number of parallel workers
        """
