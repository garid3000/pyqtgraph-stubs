from .SystemSolver import SystemSolver as SystemSolver
from .parameterTypes import GroupParameter

__all__ = ['ParameterSystem', 'SystemSolver']

class ParameterSystem(GroupParameter):
    """
    ParameterSystem is a subclass of GroupParameter that manages a tree of 
    sub-parameters with a set of interdependencies--changing any one parameter
    may affect other parameters in the system.
    
    See parametertree/SystemSolver for more information.
    
    NOTE: This API is experimental and may change substantially across minor 
    version numbers. 
    """
    def __init__(self, *args, **kwds) -> None: ...
    def setSystem(self, sys) -> None: ...
    def updateSystem(self, param, changes) -> None: ...
    def updateAllParams(self) -> None: ...
    def updateParamState(self, param, state) -> None: ...
