from .Node import Node as Node
from _typeshed import Incomplete

def isNodeClass(cls): ...

class NodeLibrary:
    """
    A library of flowchart Node types. Custom libraries may be built to provide 
    each flowchart with a specific set of allowed Node types.
    """
    nodeList: Incomplete
    nodeTree: Incomplete
    def __init__(self) -> None: ...
    def addNodeType(self, nodeClass, paths, override: bool = False) -> None:
        """
        Register a new node type. If the type's name is already in use,
        an exception will be raised (unless override=True).
        
        ============== =========================================================
        **Arguments:**
        
        nodeClass      a subclass of Node (must have typ.nodeName)
        paths          list of tuples specifying the location(s) this 
                       type will appear in the library tree.
        override       if True, overwrite any class having the same name
        ============== =========================================================
        """
    def getNodeType(self, name): ...
    def getNodeTree(self): ...
    def copy(self):
        """
        Return a copy of this library.
        """
    @staticmethod
    def treeCopy(tree): ...
    def reload(self) -> None:
        """
        Reload Node classes in this library.
        """
