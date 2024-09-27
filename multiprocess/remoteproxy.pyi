from ..util import cprint as cprint
from _typeshed import Incomplete

class ClosedError(Exception):
    """Raised when an event handler receives a request to close the connection
    or discovers that the connection has been closed."""
class NoResultError(Exception):
    """Raised when a request for the return value of a remote call fails
    because the call has not yet returned."""
class RemoteExceptionWarning(UserWarning):
    """Emitted when a request to a remote object results in an Exception """

class RemoteEventHandler:
    """
    This class handles communication between two processes. One instance is present on 
    each process and listens for communication from the other process. This enables
    (amongst other things) ObjectProxy instances to look up their attributes and call 
    their methods.
    
    This class is responsible for carrying out actions on behalf of the remote process.
    Each instance holds one end of a Connection which allows python
    objects to be passed between processes.
    
    For the most common operations, see _import(), close(), and transfer()
    
    To handle and respond to incoming requests, RemoteEventHandler requires that its
    processRequests method is called repeatedly (this is usually handled by the Process
    classes defined in multiprocess.processes).
    
    
    
    
    """
    handlers: Incomplete
    debug: Incomplete
    conn: Incomplete
    name: Incomplete
    results: Incomplete
    resultLock: Incomplete
    proxies: Incomplete
    proxyLock: Incomplete
    proxyOptions: Incomplete
    optsLock: Incomplete
    nextRequestId: int
    exited: bool
    processLock: Incomplete
    sendLock: Incomplete
    def __init__(self, connection, name, pid, debug: bool = False) -> None: ...
    @classmethod
    def getHandler(cls, pid): ...
    def debugMsg(self, msg, *args) -> None: ...
    def getProxyOption(self, opt): ...
    def setProxyOptions(self, **kwds) -> None:
        """
        Set the default behavior options for object proxies.
        See ObjectProxy._setProxyOptions for more info.
        """
    def processRequests(self):
        """Process all pending requests from the pipe, return
        after no more events are immediately available. (non-blocking)
        Returns the number of events processed.
        """
    def handleRequest(self) -> None:
        """Handle a single request from the remote process. 
        Blocks until a request is available."""
    def replyResult(self, reqId, result) -> None: ...
    def replyError(self, reqId, *exc) -> None: ...
    def send(self, request, opts: Incomplete | None = None, reqId: Incomplete | None = None, callSync: str = 'sync', timeout: int = 10, returnType: Incomplete | None = None, byteData: Incomplete | None = None, **kwds):
        """Send a request or return packet to the remote process.
        Generally it is not necessary to call this method directly; it is for internal use.
        (The docstring has information that is nevertheless useful to the programmer
        as it describes the internal protocol used to communicate between processes)
        
        ==============  ====================================================================
        **Arguments:**
        request         String describing the type of request being sent (see below)
        reqId           Integer uniquely linking a result back to the request that generated
                        it. (most requests leave this blank)
        callSync        'sync':  return the actual result of the request
                        'async': return a Request object which can be used to look up the
                                result later
                        'off':   return no result
        timeout         Time in seconds to wait for a response when callSync=='sync'
        opts            Extra arguments sent to the remote process that determine the way
                        the request will be handled (see below)
        returnType      'proxy', 'value', or 'auto'
        byteData        If specified, this is a list of objects to be sent as byte messages
                        to the remote process.
                        This is used to send large arrays without the cost of pickling.
        ==============  ====================================================================
        
        Description of request strings and options allowed for each:
        
        =============  =============  ========================================================
        request        option         description
        -------------  -------------  --------------------------------------------------------
        getObjAttr                    Request the remote process return (proxy to) an
                                      attribute of an object.
                       obj            reference to object whose attribute should be 
                                      returned
                       attr           string name of attribute to return
                       returnValue    bool or 'auto' indicating whether to return a proxy or
                                      the actual value. 
                       
        callObj                       Request the remote process call a function or 
                                      method. If a request ID is given, then the call's
                                      return value will be sent back (or information
                                      about the error that occurred while running the
                                      function)
                       obj            the (reference to) object to call
                       args           tuple of arguments to pass to callable
                       kwds           dict of keyword arguments to pass to callable
                       returnValue    bool or 'auto' indicating whether to return a proxy or
                                      the actual value. 
                       
        getObjValue                   Request the remote process return the value of
                                      a proxied object (must be picklable)
                       obj            reference to object whose value should be returned
                       
        transfer                      Copy an object to the remote process and request
                                      it return a proxy for the new object.
                       obj            The object to transfer.
                       
        import                        Request the remote process import new symbols
                                      and return proxy(ies) to the imported objects
                       module         the string name of the module to import
                       fromlist       optional list of string names to import from module
                       
        del                           Inform the remote process that a proxy has been 
                                      released (thus the remote process may be able to 
                                      release the original object)
                       proxyId        id of proxy which is no longer referenced by 
                                      remote host
                                      
        close                         Instruct the remote process to stop its event loop
                                      and exit. Optionally, this request may return a 
                                      confirmation.
            
        result                        Inform the remote process that its request has 
                                      been processed                        
                       result         return value of a request
                       
        error                         Inform the remote process that its request failed
                       exception      the Exception that was raised (or None if the 
                                      exception could not be pickled)
                       excString      string-formatted version of the exception and 
                                      traceback
        =============  =====================================================================
        """
    def close(self, callSync: str = 'off', noCleanup: bool = False, **kwds) -> None: ...
    def getResult(self, reqId): ...
    def getObjAttr(self, obj, attr, **kwds): ...
    def getObjValue(self, obj, **kwds): ...
    def callObj(self, obj, args, kwds, **opts): ...
    def registerProxy(self, proxy) -> None: ...
    def deleteProxy(self, ref) -> None: ...
    def transfer(self, obj, **kwds):
        """
        Transfer an object by value to the remote host (the object must be picklable) 
        and return a proxy for the new remote object.
        """
    def autoProxy(self, obj, noProxyTypes): ...

class Request:
    """
    Request objects are returned when calling an ObjectProxy in asynchronous mode
    or if a synchronous call has timed out. Use hasResult() to ask whether
    the result of the call has been returned yet. Use result() to get
    the returned value.
    """
    proc: Incomplete
    description: Incomplete
    reqId: Incomplete
    gotResult: bool
    timeout: Incomplete
    def __init__(self, process, reqId, description: Incomplete | None = None, timeout: int = 10) -> None: ...
    def result(self, block: bool = True, timeout: Incomplete | None = None):
        """
        Return the result for this request. 
        
        If block is True, wait until the result has arrived or *timeout* seconds passes.
        If the timeout is reached, raise NoResultError. (use timeout=None to disable)
        If block is False, raise NoResultError immediately if the result has not arrived yet.
        
        If the process's connection has closed before the result arrives, raise ClosedError.
        """
    def hasResult(self):
        """Returns True if the result for this request has arrived."""

class LocalObjectProxy:
    """
    Used for wrapping local objects to ensure that they are send by proxy to a remote host.
    Note that 'proxy' is just a shorter alias for LocalObjectProxy.
    
    For example::
    
        data = [1,2,3,4,5]
        remotePlot.plot(data)         ## by default, lists are pickled and sent by value
        remotePlot.plot(proxy(data))  ## force the object to be sent by proxy
    
    """
    nextProxyId: int
    proxiedObjects: Incomplete
    @classmethod
    def registerObject(cls, obj): ...
    @classmethod
    def lookupProxyId(cls, pid): ...
    @classmethod
    def releaseProxyId(cls, pid) -> None: ...
    processId: Incomplete
    typeStr: Incomplete
    obj: Incomplete
    opts: Incomplete
    def __init__(self, obj, **opts) -> None:
        """
        Create a 'local' proxy object that, when sent to a remote host,
        will appear as a normal ObjectProxy to *obj*. 
        Any extra keyword arguments are passed to proxy._setProxyOptions()
        on the remote side.
        """
    def __reduce__(self): ...
proxy = LocalObjectProxy

def unpickleObjectProxy(processId, proxyId, typeStr, attributes: Incomplete | None = None, opts: Incomplete | None = None): ...

class ObjectProxy:
    """
    Proxy to an object stored by the remote process. Proxies are created
    by calling Process._import(), Process.transfer(), or by requesting/calling
    attributes on existing proxy objects.
    
    For the most part, this object can be used exactly as if it
    were a local object::
    
        rsys = proc._import('sys')   # returns proxy to sys module on remote process
        rsys.stdout                  # proxy to remote sys.stdout
        rsys.stdout.write            # proxy to remote sys.stdout.write
        rsys.stdout.write('hello')   # calls sys.stdout.write('hello') on remote machine
                                     # and returns the result (None)
    
    When calling a proxy to a remote function, the call can be made synchronous
    (result of call is returned immediately), asynchronous (result is returned later),
    or return can be disabled entirely::
    
        ros = proc._import('os')
        
        ## synchronous call; result is returned immediately
        pid = ros.getpid()
        
        ## asynchronous call
        request = ros.getpid(_callSync='async')
        while not request.hasResult():
            time.sleep(0.01)
        pid = request.result()
        
        ## disable return when we know it isn't needed
        rsys.stdout.write('hello', _callSync='off')
    
    Additionally, values returned from a remote function call are automatically
    returned either by value (must be picklable) or by proxy. 
    This behavior can be forced::
    
        rnp = proc._import('numpy')
        arrProxy = rnp.array([1,2,3,4], _returnType='proxy')
        arrValue = rnp.array([1,2,3,4], _returnType='value')
    
    The default callSync and returnType behaviors (as well as others) can be set 
    for each proxy individually using ObjectProxy._setProxyOptions() or globally using 
    proc.setProxyOptions(). 
    
    """
    def __init__(self, processId, proxyId, typeStr: str = '', parent: Incomplete | None = None) -> None: ...
    def __reduce__(self): ...
    def __getattr__(self, attr, **kwds):
        """
        Calls __getattr__ on the remote object and returns the attribute
        by value or by proxy depending on the options set (see
        ObjectProxy._setProxyOptions and RemoteEventHandler.setProxyOptions)
        
        If the option 'deferGetattr' is True for this proxy, then a new proxy object
        is returned _without_ asking the remote object whether the named attribute exists.
        This can save time when making multiple chained attribute requests,
        but may also defer a possible AttributeError until later, making
        them more difficult to debug.
        """
    def __call__(self, *args, **kwds):
        """
        Attempts to call the proxied object from the remote process.
        Accepts extra keyword arguments:
        
            _callSync    'off', 'sync', or 'async'
            _returnType   'value', 'proxy', or 'auto'
        
        If the remote call raises an exception on the remote process,
        it will be re-raised on the local process.
        
        """
    def __getitem__(self, *args): ...
    def __setitem__(self, *args) -> None: ...
    def __setattr__(self, *args): ...
    def __len__(self, *args) -> int: ...
    def __add__(self, *args): ...
    def __sub__(self, *args): ...
    def __div__(self, *args): ...
    def __truediv__(self, *args): ...
    def __floordiv__(self, *args): ...
    def __mul__(self, *args): ...
    def __pow__(self, *args): ...
    def __iadd__(self, *args): ...
    def __isub__(self, *args): ...
    def __idiv__(self, *args): ...
    def __itruediv__(self, *args): ...
    def __ifloordiv__(self, *args): ...
    def __imul__(self, *args): ...
    def __ipow__(self, *args): ...
    def __rshift__(self, *args): ...
    def __lshift__(self, *args): ...
    def __irshift__(self, *args): ...
    def __ilshift__(self, *args): ...
    def __eq__(self, *args): ...
    def __ne__(self, *args): ...
    def __lt__(self, *args): ...
    def __gt__(self, *args): ...
    def __le__(self, *args): ...
    def __ge__(self, *args): ...
    def __and__(self, *args): ...
    def __or__(self, *args): ...
    def __xor__(self, *args): ...
    def __iand__(self, *args): ...
    def __ior__(self, *args): ...
    def __ixor__(self, *args): ...
    def __mod__(self, *args): ...
    def __radd__(self, *args): ...
    def __rsub__(self, *args): ...
    def __rdiv__(self, *args): ...
    def __rfloordiv__(self, *args): ...
    def __rtruediv__(self, *args): ...
    def __rmul__(self, *args): ...
    def __rpow__(self, *args): ...
    def __rrshift__(self, *args): ...
    def __rlshift__(self, *args): ...
    def __rand__(self, *args): ...
    def __ror__(self, *args): ...
    def __rxor__(self, *args): ...
    def __rmod__(self, *args): ...
    def __hash__(self): ...

class DeferredObjectProxy(ObjectProxy):
    """
    This class represents an attribute (or sub-attribute) of a proxied object.
    It is used to speed up attribute requests. Take the following scenario::
    
        rsys = proc._import('sys')
        rsys.stdout.write('hello')
        
    For this simple example, a total of 4 synchronous requests are made to 
    the remote process: 
    
    1) import sys
    2) getattr(sys, 'stdout')
    3) getattr(stdout, 'write')
    4) write('hello')
    
    This takes a lot longer than running the equivalent code locally. To
    speed things up, we can 'defer' the two attribute lookups so they are
    only carried out when neccessary::
    
        rsys = proc._import('sys')
        rsys._setProxyOptions(deferGetattr=True)
        rsys.stdout.write('hello')
        
    This example only makes two requests to the remote process; the two 
    attribute lookups immediately return DeferredObjectProxy instances 
    immediately without contacting the remote process. When the call 
    to write() is made, all attribute requests are processed at the same time.
    
    Note that if the attributes requested do not exist on the remote object, 
    making the call to write() will raise an AttributeError.
    """
    def __init__(self, parentProxy, attribute) -> None: ...
