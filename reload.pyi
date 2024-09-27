from .debug import printExc as printExc
from _typeshed import Incomplete

orig_reload = reload

def reloadAll(prefix: Incomplete | None = None, debug: bool = False):
    """Automatically reload all modules whose __file__ begins with *prefix*.

    Skips reload if the file has not been updated (if .pyc is newer than .py)
    If *prefix* is None, then all loaded modules are checked.

    Returns a dictionary {moduleName: (reloaded, reason)} describing actions taken
    for each module.
    """
def reload(module, debug: bool = False, lists: bool = False, dicts: bool = False) -> None:
    """Replacement for the builtin reload function:
    - Reloads the module as usual
    - Updates all old functions and class methods to use the new code
    - Updates all instances of each modified class to use the new class
    - Can update lists and dicts, but this is disabled by default
    - Requires that class and function names have not changed
    """
def updateFunction(old, new, debug, depth: int = 0, visited: Incomplete | None = None): ...
def updateClass(old, new, debug) -> None: ...
def safeStr(obj): ...
def getPreviousVersion(obj):
    """Return the previous version of *obj*, or None if this object has not
    been reloaded.
    """
