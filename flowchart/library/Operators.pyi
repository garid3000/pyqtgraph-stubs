from ..Node import Node as Node
from .common import CtrlNode as CtrlNode
from _typeshed import Incomplete

class UniOpNode(Node):
    """Generic node for performing any operation like Out = In.fn()"""
    fn: Incomplete
    def __init__(self, name, fn) -> None: ...
    def process(self, **args): ...

class BinOpNode(CtrlNode):
    """Generic node for performing any operation like A.fn(B)"""
    uiTemplate: Incomplete
    fn: Incomplete
    def __init__(self, name, fn) -> None: ...
    def process(self, **args): ...

class AbsNode(UniOpNode):
    """Returns abs(Inp). Does not check input types."""
    nodeName: str
    def __init__(self, name) -> None: ...

class AddNode(BinOpNode):
    """Returns A + B. Does not check input types."""
    nodeName: str
    def __init__(self, name) -> None: ...

class SubtractNode(BinOpNode):
    """Returns A - B. Does not check input types."""
    nodeName: str
    def __init__(self, name) -> None: ...

class MultiplyNode(BinOpNode):
    """Returns A * B. Does not check input types."""
    nodeName: str
    def __init__(self, name) -> None: ...

class DivideNode(BinOpNode):
    """Returns A / B. Does not check input types."""
    nodeName: str
    def __init__(self, name) -> None: ...

class FloorDivideNode(BinOpNode):
    """Returns A // B. Does not check input types."""
    nodeName: str
    def __init__(self, name) -> None: ...
