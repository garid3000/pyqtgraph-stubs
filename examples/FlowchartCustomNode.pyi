from _typeshed import Incomplete
from pyqtgraph.Qt import QtWidgets as QtWidgets
from pyqtgraph.flowchart import Flowchart as Flowchart, Node as Node
from pyqtgraph.flowchart.library.common import CtrlNode as CtrlNode

app: Incomplete
win: Incomplete
cw: Incomplete
layout: Incomplete
fc: Incomplete
w: Incomplete
v1: Incomplete
v2: Incomplete
data: Incomplete

class ImageViewNode(Node):
    """Node that displays image data in an ImageView widget"""
    nodeName: str
    view: Incomplete
    def __init__(self, name) -> None: ...
    def setView(self, view) -> None: ...
    def process(self, data, display: bool = True) -> None: ...

class UnsharpMaskNode(CtrlNode):
    """Return the input data passed through an unsharp mask."""
    nodeName: str
    uiTemplate: Incomplete
    def __init__(self, name) -> None: ...
    def process(self, dataIn, display: bool = True): ...

library: Incomplete
v1Node: Incomplete
v2Node: Incomplete
fNode: Incomplete
