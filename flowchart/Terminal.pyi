from ..Qt import QtWidgets
from ..graphicsItems.GraphicsObject import GraphicsObject
from _typeshed import Incomplete

__all__ = ['Terminal', 'TerminalGraphicsItem']

class Terminal:
    valueOk: Incomplete
    def __init__(self, node, name, io, optional: bool = False, multi: bool = False, pos: Incomplete | None = None, renamable: bool = False, removable: bool = False, multiable: bool = False, bypass: Incomplete | None = None) -> None:
        """
        Construct a new terminal. 
        
        ==============  =================================================================================
        **Arguments:**
        node            the node to which this terminal belongs
        name            string, the name of the terminal
        io              'in' or 'out'
        optional        bool, whether the node may process without connection to this terminal
        multi           bool, for inputs: whether this terminal may make multiple connections
                        for outputs: whether this terminal creates a different value for each connection
        pos             [x, y], the position of the terminal within its node's boundaries
        renamable       (bool) Whether the terminal can be renamed by the user
        removable       (bool) Whether the terminal can be removed by the user
        multiable       (bool) Whether the user may toggle the *multi* option for this terminal
        bypass          (str) Name of the terminal from which this terminal's value is derived
                        when the Node is in bypass mode.
        ==============  =================================================================================
        """
    def value(self, term: Incomplete | None = None):
        """Return the value this terminal provides for the connected terminal"""
    def bypassValue(self): ...
    def setValue(self, val, process: bool = True) -> None:
        """If this is a single-value terminal, val should be a single value.
        If this is a multi-value terminal, val should be a dict of terminal:value pairs"""
    def setOpts(self, **opts) -> None: ...
    def connected(self, term) -> None:
        """Called whenever this terminal has been connected to another. (note--this function is called on both terminals)"""
    def disconnected(self, term) -> None:
        """Called whenever this terminal has been disconnected from another. (note--this function is called on both terminals)"""
    def inputChanged(self, term, process: bool = True) -> None:
        """Called whenever there is a change to the input value to this terminal.
        It may often be useful to override this function."""
    def valueIsAcceptable(self):
        """Returns True->acceptable  None->unknown  False->Unacceptable"""
    def setValueAcceptable(self, v: bool = True) -> None: ...
    def connections(self): ...
    def node(self): ...
    def isInput(self): ...
    def isMultiValue(self): ...
    def setMultiValue(self, multi) -> None:
        """Set whether this is a multi-value terminal."""
    def isOutput(self): ...
    def isRenamable(self): ...
    def isRemovable(self): ...
    def isMultiable(self): ...
    def name(self): ...
    def graphicsItem(self): ...
    def isConnected(self): ...
    def connectedTo(self, term): ...
    def hasInput(self): ...
    def inputTerminals(self):
        """Return the terminal(s) that give input to this one."""
    def dependentNodes(self):
        """Return the list of nodes which receive input from this terminal."""
    def connectTo(self, term, connectionItem: Incomplete | None = None): ...
    def disconnectFrom(self, term) -> None: ...
    def disconnectAll(self) -> None: ...
    def recolor(self, color: Incomplete | None = None, recurse: bool = True) -> None: ...
    def rename(self, name) -> None: ...
    def __hash__(self): ...
    def close(self) -> None: ...
    def saveState(self): ...
    def __lt__(self, other):
        """When the terminal is multi value, the data passed to the DatTreeWidget for each input or output, is {Terminal: value}.
        To make this sortable, we provide the < operator.
        """

class TextItem(QtWidgets.QGraphicsTextItem):
    on_update: Incomplete
    def __init__(self, text, parent, on_update) -> None: ...
    def focusOutEvent(self, ev) -> None: ...
    def keyPressEvent(self, ev) -> None: ...

class TerminalGraphicsItem(GraphicsObject):
    term: Incomplete
    brush: Incomplete
    box: Incomplete
    label: Incomplete
    newConnection: Incomplete
    menu: Incomplete
    def __init__(self, term, parent: Incomplete | None = None) -> None: ...
    def labelChanged(self) -> None: ...
    def termRenamed(self, name) -> None: ...
    def setBrush(self, brush) -> None: ...
    def disconnect(self, target) -> None: ...
    def boundingRect(self): ...
    def paint(self, p, *args) -> None: ...
    anchorPos: Incomplete
    def setAnchor(self, x, y) -> None: ...
    def updateConnections(self) -> None: ...
    def mousePressEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def raiseContextMenu(self, ev) -> None: ...
    def getMenu(self): ...
    def toggleMulti(self) -> None: ...
    def removeSelf(self) -> None: ...
    def mouseDragEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def connectPoint(self): ...
    def nodeMoved(self) -> None: ...

class ConnectionItem(GraphicsObject):
    source: Incomplete
    target: Incomplete
    length: int
    hovered: bool
    path: Incomplete
    shapePath: Incomplete
    style: Incomplete
    def __init__(self, source, target: Incomplete | None = None) -> None: ...
    def close(self) -> None: ...
    def setTarget(self, target) -> None: ...
    def setStyle(self, **kwds) -> None: ...
    def updateLine(self) -> None: ...
    def generatePath(self, start, stop): ...
    def keyPressEvent(self, ev) -> None: ...
    def mousePressEvent(self, ev) -> None: ...
    def mouseClickEvent(self, ev) -> None: ...
    def hoverEvent(self, ev) -> None: ...
    def boundingRect(self): ...
    def viewRangeChanged(self) -> None: ...
    def shape(self): ...
    def paint(self, p, *args) -> None: ...
